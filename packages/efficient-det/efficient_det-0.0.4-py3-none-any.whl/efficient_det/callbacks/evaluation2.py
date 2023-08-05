import tensorflow as tf
import wandb
from utils.eval import evaluate


class Evaluate(tf.keras.callbacks.Callback):
    def __init__(self, generator, iou_threshold=0.5, score_threshold=0.01,
                 verbose=1, w_and_b=False):
        super(Evaluate, self).__init__()
        self.iou_threshold = iou_threshold
        self.generator = generator
        self.verbose = verbose
        self.score_threshold = score_threshold
        self.w_and_b = w_and_b

    def on_epoch_end(self, epoch, logs=None):
        average_precisions, num_objects = evaluate(self.model, self.generator,
                                     self.iou_threshold, self.score_threshold)

        ap_all = []
        num_objects_all = []

        for i in range(self.generator.num_classes):
            if self.verbose:
                print(f'{num_objects[i]} objects of class {self.generator.get_label_name(i)} with average precision {round(average_precisions[i], 4)}')
            ap_all.append(average_precisions[i])
            num_objects_all.append(num_objects[i])

        mean_ap = sum(ap_all) / sum(num_objects_all)
        if self.verbose:
            print(f'mAP: {round(mean_ap, 4)}')
        if self.w_and_b is True:
            wandb.log({'mean_ap':mean_ap})

