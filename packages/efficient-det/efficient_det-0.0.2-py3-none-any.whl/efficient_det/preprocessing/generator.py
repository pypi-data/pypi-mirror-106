import os
import cv2
import xml.etree.ElementTree as ET
import numpy as np
import tensorflow as tf

from PIL import Image
from configuration.constants import NAMES_TO_LABELS
from utils.targets import compute_box_targets
from utils.anchors import generate_anchors
from utils.parser import get_num_objects, parse_annotations
from utils.image import normalize, resize_image


class FruitDatasetGenerator(tf.keras.utils.Sequence):
    def __init__(self, file_names, annotations_path, image_path, batch_size=1,
                 image_shape=(512, 512, 3), shuffle=True):
        """ Dataset generator object.

        Args:
            file_names: List of file names to choose from.
            annotations_path: Path to annotations.
            image_path: Path to png files.
            batch_size: Number of items in one batch.
            image_shape: Image shape.
            shuffle: To shuffle list of indexes.
        """
        super(FruitDatasetGenerator, self).__init__()
        self.file_names = file_names
        self.annotations_path = annotations_path
        self.image_path = image_path
        self.batch_size = batch_size
        self.image_shape = image_shape
        self.classes = NAMES_TO_LABELS
        self.num_classes = len(NAMES_TO_LABELS)
        self.shuffle = shuffle

        self.labels = {}
        for key, value in self.classes.items():
            self.labels[value] = key
        self.on_epoch_end()

        self.anchors = generate_anchors(img_shape=image_shape[0])

    def get_label_name(self, label):
        """
        Map label id to name.
        """
        return self.labels[label]

    def __len__(self):
        """ Number of batches in the Sequence.
        """
        return self.size() // self.batch_size

    def size(self):
        """ Size of the dataset.
        """
        return len(self.file_names)

    def on_epoch_end(self):
        """ Update indexes after each epoch so batches between epochs don't
        look alike.
        """
        self.indexes = np.arange(self.size())
        if self.shuffle:
            np.random.shuffle(self.indexes)

    def compute_targets(self, images, annotations):
        """ Compute target outputs for the network using their annotations.

        Args:
            images:
            annotations: List of dictionaries for each image in the batch
            containing labels and bounding boxes in the image.

        Returns: With shapes (batch_size, num_boxes, 15) and (batch_size,
            num_boxes, 5).

        """

        return compute_box_targets(self.anchors, images, annotations,
                                   self.num_classes)

    def load_images_for_batch(self, batch_indexes):
        """ Load images for all images in the batch.

        Args:
            batch_indexes: Indexes of files to use.

        """
        return [self.load_image(index) for index in batch_indexes]

    def load_annotations_for_batch(self, batch_indexes):
        """ Load annotations for all images in the batch.

        Args:
            batch_indexes: Indexes of files to use.

        """
        return [self.load_annotations(index) for index in batch_indexes]

    def load_image(self, index):
        """ Load image with index equals to index.

        Args:
            index: Image index.

        """
        path = os.path.join(self.image_path, self.file_names[index])
        image = Image.open(path)
        return np.asarray(image)

    def load_annotations(self, index):
        """ Load annotations for an image with index = index.

        Args:
            index: Image index.

        Returns:

        """
        filename = self.file_names[index]
        filename = filename.replace("png", "xml")

        return parse_annotations(filename, self.annotations_path,
                                 self.classes)

    def compute_scale(self, size):
        scale = self.image_shape[0] / size
        return scale

    def preprocess_image(self, image):
        """

        Args:
            image: Image to preprocess.

        Returns:

        """
        image_width = image.shape[1]
        image_height = image.shape[0]

        if image_height > image_width:
            scale = self.compute_scale(image_height)
            resized_height = self.image_shape[0]
            resized_width = int(image_width * scale)
        else:
            scale = self.compute_scale(image_width)
            resized_width = self.image_shape[1]
            resized_height = int(image_height * scale)

        image = cv2.resize(image, (resized_width, resized_height))
        new_image = np.ones(self.image_shape, dtype=np.float32) * 128

        offset_h = (self.image_shape[1] - resized_height) // 2
        offset_w = (self.image_shape[0] - resized_width) // 2

        new_image[offset_h:offset_h + resized_height,
        offset_w:offset_w + resized_width] = image.astype(np.float32)

        return normalize(new_image), scale, offset_w, offset_h

    def preprocess(self, image, annotation):
        """ Preprocess an image.

        Args:
            image: PNG image file.
            annotation: Annotation corresponding to the image.

        """
        image, scale, offset_h, offset_w = self.preprocess_image(image)

        annotation['boxes'] *= scale

        annotation['boxes'][:, 0] += offset_w
        annotation['boxes'][:, 2] += offset_w
        annotation['boxes'][:, 1] += offset_h
        annotation['boxes'][:, 3] += offset_h

        return image, annotation

    def preprocess_batch(self, images, annotations):
        """ Preprocess images for all images in the batch.

        Args:
            images: Batch containing images.
            annotations: Batch containing annotations (labels and boxes).

        """
        for i in range(self.batch_size):
            images[i], annotations[i] = self.preprocess(images[i],
                                                        annotations[i])
            annotations[i]['boxes'] = self.clip_boxes(annotations[i]['boxes'])

        return images, annotations

    def clip_boxes(self, boxes):
        height = self.image_shape[0]
        width = self.image_shape[1]

        return np.stack((np.clip(boxes[:, 0], 0, width - 1),
                         np.clip(boxes[:, 1], 0, height - 1),
                         np.clip(boxes[:, 2], 0, width - 1),
                         np.clip(boxes[:, 3], 0, height - 1)), axis=1)

    def data_generation(self, indexes):
        """ Generate data containing self.batch_size samples.

        Args:
            indexes: Indices to use.

        Returns: Batch containing images and targets.

        """
        images = self.load_images_for_batch(indexes)
        annotations = self.load_annotations_for_batch(indexes)

        images, annotations = self.preprocess_batch(images, annotations)

        targets = self.compute_targets(images, annotations)

        return np.array(images), targets

    def __getitem__(self, index):
        """ Generate one batch of data containing input (images) and targets
        (annotations).

        Args:
            index: Index where to start sampling self.batch_size items for
            the batch.

        Returns: Batch with images and corresponding targets.

        """
        begin = index * self.batch_size
        end = (index + 1) * self.batch_size
        indexes = self.indexes[begin:end]

        images, targets = self.data_generation(indexes)

        return images, targets
