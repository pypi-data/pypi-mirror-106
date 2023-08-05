import numpy as np


def compute_intersection_over_union(anchors, annotations):
    """ Compute intersection over union for all default boxes with all target
    boxes.

    Args:
        anchors: Default boxes.
        annotations: Target boxes.
        transform: To change way of box coordinates are saved.

    Returns: With shape (num_anchors, num_annotations).

    """
    #num_annotations = len(annotations)
    #num_anchors = len(anchors)

    intersection, check = compute_intersection(anchors, annotations)

    #annotations_area = compute_area(annotations)
    #annotations_area = np.tile(annotations_area, num_anchors)
    #annotations_area = annotations_area.reshape((num_anchors, num_annotations))

    #anchors_area = compute_area(anchors)
    #anchors_area = np.repeat(anchors_area, num_annotations)
    #anchors_area = anchors_area.reshape((num_anchors, num_annotations))

    #denominator = (anchors_area + annotations_area - intersection)
    #denominator = np.where(denominator == 0, 1e-10, denominator)
    denominator = compute_union(anchors, annotations, intersection)

    intersection_over_union = intersection / denominator

    return np.where(check == False, 0, intersection_over_union)

def compute_union(anchors, annotations, intersection):
    num_annotations = len(annotations)
    num_anchors = len(anchors)

    annotations_area = compute_area(annotations)
    annotations_area = np.tile(annotations_area, num_anchors)
    annotations_area = annotations_area.reshape((num_anchors, num_annotations))

    anchors_area = compute_area(anchors)
    anchors_area = np.repeat(anchors_area, num_annotations)
    anchors_area = anchors_area.reshape((num_anchors, num_annotations))

    union = (anchors_area + annotations_area - intersection)
    union = np.where(union == 0, 1e-10, union)

    return union

def compute_area(boxes):
    """

    Args:
        boxes: Bounding boxes

    Returns: Compute box area.

    """
    return (boxes[:, 2] - boxes[:, 0]) * (boxes[:, 3] - boxes[:, 1])


def compute_intersection(anchors, annotations):
    """ Compute intersection between all default boxes to all target boxes.

    Args:
        anchors: Default boxes for all m feature maps.
        annotations: Target boxes.

    Returns: Array with shape (num_anchors, num_annotations).

    """
    num_annotations = len(annotations)
    num_anchors = len(anchors)

    anchors = np.repeat(anchors, num_annotations, axis=0)
    annotations = np.tile(annotations, (num_anchors, 1))

    x = compute_width_of_intersection(anchors, annotations)
    y = compute_height_of_intersection(anchors, annotations)

    x = x.reshape((num_anchors, num_annotations))
    y = y.reshape((num_anchors, num_annotations))

    intersection = x * y
    check = check_if_intersection_exists(num_anchors, num_annotations, x, y)

    return intersection, check


def compute_width_of_intersection(anchors, annotations):
    x_min = np.maximum(anchors[:, 0], annotations[:, 0])
    x_max = np.minimum(anchors[:, 2], annotations[:, 2])

    return x_max - x_min


def compute_height_of_intersection(anchors, annotations):
    y_min = np.maximum(anchors[:, 1], annotations[:, 1])
    y_max = np.minimum(anchors[:, 3], annotations[:, 3])

    return y_max - y_min


def check_if_intersection_exists(num_anchors, num_annotations, x, y):
    """ Check if there is an intersection between boxes.

    Args:
        num_anchors: Number of default boxes.
        num_annotations: Number of target boxes to compare with.
        x: Width of possible intersection area.
        y: Height of possible intersection area.

    Returns: Bool array with shape (num_anchors, num_annotations).

    """
    intersection_exists = np.ones((num_anchors, num_annotations), dtype=bool)

    intersection_exists = np.where(x <= 0, False, intersection_exists)
    intersection_exists = np.where(y <= 0, False, intersection_exists)

    return intersection_exists
