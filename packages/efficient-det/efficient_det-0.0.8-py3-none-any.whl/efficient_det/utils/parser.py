import os
import sys
import random
import numpy as np
import xml.etree.ElementTree as ET


def get_num_objects(tree) -> int:
    """ Get number of objects in an image with name = filename.

    Args:
        tree:

    Returns:

    """
    num_obj = 0

    for e in tree.iter():
        if e.tag == "object":
            num_obj = num_obj + 1

    return num_obj


def parse_annotations(xml_file, annotations_path, names_to_labels):
    """ Parse all annotations in the xml file.

    Args:
        xml_file: Name of xml file.
        annotations_path: Path to annotations.
        names_to_labels:

    Returns: Boxes and corresponding labels in an image.

    """
    filepath = os.path.join(annotations_path, xml_file)
    tree = ET.parse(filepath)

    num_objects = get_num_objects(tree)

    annotations = {'labels': np.empty((num_objects,)),
                   'boxes': np.empty((num_objects, 4))}

    i = 0
    for elements in tree.iter():
        if elements.tag == "object":
            for element in elements:
                if element.tag == "name":
                    label = names_to_labels[str(element.text)]

                elif element.tag == "bndbox":
                    for e in element:
                        if e.tag == "xmin":
                            x_min = float(e.text)
                        elif e.tag == "ymin":
                            y_min = float(e.text)
                        elif e.tag == "xmax":
                            x_max = float(e.text)
                        elif e.tag == "ymax":
                            y_max = float(e.text)

                    annotations['labels'][i] = label
                    annotations['boxes'][i, 0] = x_min
                    annotations['boxes'][i, 1] = y_min
                    annotations['boxes'][i, 2] = x_max
                    annotations['boxes'][i, 3] = y_max
            i = i + 1

    return annotations
