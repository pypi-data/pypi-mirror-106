from efficient_det.utils.overlap import compute_intersection_over_union
import numpy as np


def compute_box_targets(anchors, img_batch, annotations_batch, num_classes):
    """ Compute annotations outputs for the network using annotations.

    Args:
        anchors: Default boxes.
        img_batch:
        annotations_batch: List of dictionaries containing boxes and
        corresponding labels.
        num_classes: Number of classes.

    Returns:
        labels: Containing hot encoded labels for each default box for
        each batch item.
        bboxes: Containing bounding box values for each default box
        for each batch item.

    """

    batch_size = len(img_batch)
    num_boxes = len(anchors)

    bboxes = np.zeros((batch_size, num_boxes, 4 + 1))
    labels = np.zeros((batch_size, num_boxes, num_classes + 1))

    for i, (img, annotations) in enumerate(zip(img_batch, annotations_batch)):
        positive_indexes, ignore_indexes, argmax_indexes = \
            assign_targets_to_anchors(
            anchors, annotations['boxes'])

        idx = one_hot_encoding(annotations, argmax_indexes, positive_indexes)
        labels[i, positive_indexes, idx] = 1

        corresponding_targets = annotations['boxes'][argmax_indexes, :]
        bboxes[i, :, :-1] = transform_targets(anchors, corresponding_targets)

        indexes_outside = get_box_indexes_outside_of_image_shape(anchors, img)

        labels[i, ignore_indexes, -1] = -1
        labels[i, positive_indexes, -1] = 1

        bboxes[i, ignore_indexes, -1] = -1
        bboxes[i, positive_indexes, -1] = 1

        labels[i, indexes_outside, -1] = -1
        bboxes[i, indexes_outside, -1] = -1

    return bboxes, labels


def get_box_indexes_outside_of_image_shape(anchors, image):
    centers = np.vstack([*get_box_center(anchors)]).T

    return np.logical_or(centers[:, 0] >= image.shape[1],
                         centers[:, 1] >= image.shape[0])


def get_box_center(boxes):
    center_x = (boxes[:, 0] + boxes[:, 2]) / 2.0
    center_y = (boxes[:, 1] + boxes[:, 3]) / 2.0

    return center_x, center_y


def one_hot_encoding(annotations, argmax_indexes, positive_indexes):
    labels = annotations['labels']

    return labels[argmax_indexes[positive_indexes]].astype(int)


def transform_targets(anchors, annotations):
    """ Prepare target boxes for loss calculation.

    Args:
        anchors: Default boxes with format (x_min, y_min, x_max, y_max).
        annotations: Target boxes with same format as anchor boxes.

    Returns: Target values.
    """

    std = np.array([0.2, 0.2, 0.2, 0.2])

    widths = anchors[:, 2] - anchors[:, 0]
    heights = anchors[:, 3] - anchors[:, 1]

    x_min = (annotations[:, 0] - anchors[:, 0]) / widths
    y_min = (annotations[:, 1] - anchors[:, 1]) / heights
    x_max = (annotations[:, 2] - anchors[:, 2]) / widths
    y_max = (annotations[:, 3] - anchors[:, 3]) / heights

    targets = np.stack((x_min, y_min, x_max, y_max), axis=1)

    return targets / std


def assign_targets_to_anchors(anchors, annotations, positive_overlap=0.5,
                              background_threshold=0.4):
    """ Assign ground truth boxes to default boxes.

    Args:
        anchors: Default boxes.
        annotations: Ground truth boxes representing an object in the image.
        positive_overlap: Default boxes are assigned to objects in the image.
        background_threshold: Default boxes where overlap with the corresponding
        target box is below that threshold will be considered as background
        boxes.

    Returns:
        positive_indexes: Indexes of those default boxes corresponding to
        objects in the image.
        ignore_indexes: Indexes of default boxes which will be ignored when
        computing loss.
        argmax_overlaps: Indexes for each default boxes with the
        corresponding target.

    """
    overlaps = compute_intersection_over_union(anchors, annotations)

    argmax_overlaps = np.argmax(overlaps, axis=1)
    max_overlaps = overlaps[np.arange(overlaps.shape[0]), argmax_overlaps]

    positive_indexes = max_overlaps >= positive_overlap
    ignore_indexes = (max_overlaps > background_threshold) & ~positive_indexes

    return positive_indexes, ignore_indexes, argmax_overlaps
