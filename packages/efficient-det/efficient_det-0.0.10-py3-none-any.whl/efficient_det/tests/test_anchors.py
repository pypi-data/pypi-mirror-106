import unittest
import numpy as np

from utils.anchors import (default_boxes_for_all_feature_maps,
    default_boxes_for_batch, default_boxes_for_one_feature_map,
    generate_default_boxes_for_one_feature_map)


class TestAnchors(unittest.TestCase):
    def test_default_boxes_for_all_feature_maps_ssd300(self):
        aspect_ratios = [[1., 2., 3., .5], [1., 2., 3., .5, 1. / 3, 1.],
                         [1., 2., 3., .5, 1. / 3, 1.],
                         [1., 2., 3., .5, 1. / 3, 1.], [1., 2., 3., .5],
                         [1., 2., 3., .5]]

        feature_maps = [38, 19, 10, 5, 3, 1]

        strides = [8, 16, 32, 64, 128, 256, 512]

        bases = [1, 1, 1, 1, 1, 1]

        default_boxes = default_boxes_for_all_feature_maps(bases, feature_maps,
                                                           aspect_ratios,
                                                           strides=strides)

        self.assertEqual(8732, default_boxes.shape[0])

    def test_default_boxes_for_all_feature_maps_ssd512(self):
        aspect_ratios = [[1., 2., 3., .5], [1., 2., 3., .5, 1. / 3, 1.],
                         [1., 2., 3., .5, 1. / 3, 1.],
                         [1., 2., 3., .5, 1. / 3, 1.],
                         [1., 2., 3., .5, 1. / 3, 1.], [1., 2., 3., .5],
                         [1., 2., 3., .5]]

        feature_maps = [64, 32, 16, 8, 4, 2, 1]

        strides = [8, 16, 32, 64, 128, 256, 512]

        bases = [1, 1, 1, 1, 1, 1, 1]

        default_boxes = default_boxes_for_all_feature_maps(bases, feature_maps,
                                                           aspect_ratios,
                                                           strides=strides)

        self.assertEqual(24564, default_boxes.shape[0])

    def test_default_boxes_for_batch(self):
        batch_size = 32

        default_boxes = default_boxes_for_batch(batch_size)

        self.assertEqual(batch_size, default_boxes.shape[0])

    def test_default_boxes_for_one_feature_map(self):
        scale = 1.0
        aspect_ratios = [1.]

        base = 1.0

        width, height = default_boxes_for_one_feature_map(base, aspect_ratios,
                                                          scale)

        self.assertTrue((width == [1.]).all())
        self.assertTrue((height == [1.]).all())

    def test_default_boxes_for_one_feature_map_base10(self):
        scale = 1.0
        aspect_ratios = [1.]

        base = 10.0

        width, height = default_boxes_for_one_feature_map(base, aspect_ratios,
                                                          scale)

        self.assertTrue((width == [10.]).all())
        self.assertTrue((height == [10.]).all())

    def test_generate_default_boxes_for_one_feature_map(self):
        scale = 1.0
        aspect_ratios = [1.]

        base = 1.0

        width, height = default_boxes_for_one_feature_map(base, aspect_ratios,
                                                          scale)

        size = 4
        stride = 128

        boxes = np.array(
            generate_default_boxes_for_one_feature_map(size, stride,
                                                       (width, height)))

        expected = np.array(
            [[63.5, 63.5, 64.5, 64.5], [63.5, 191.5, 64.5, 192.5],
             [63.5, 319.5, 64.5, 320.5], [63.5, 447.5, 64.5, 448.5],
             [191.5, 63.5, 192.5, 64.5], [191.5, 191.5, 192.5, 192.5],
             [191.5, 319.5, 192.5, 320.5], [191.5, 447.5, 192.5, 448.5],
             [319.5, 63.5, 320.5, 64.5], [319.5, 191.5, 320.5, 192.5],
             [319.5, 319.5, 320.5, 320.5], [319.5, 447.5, 320.5, 448.5],
             [447.5, 63.5, 448.5, 64.5], [447.5, 191.5, 448.5, 192.5],
             [447.5, 319.5, 448.5, 320.5], [447.5, 447.5, 448.5, 448.5]])

        self.assertTrue(np.array_equiv(boxes, expected))

    def test_generate_default_boxes_for_one_feature_map_base10(self):
        scale = 1.0
        aspect_ratios = [1.]

        base = 10.0

        width, height = default_boxes_for_one_feature_map(base, aspect_ratios,
                                                          scale)

        size = 4
        stride = 128

        boxes = np.array(
            generate_default_boxes_for_one_feature_map(size, stride,
                                                       (width, height)))

        expected = np.array(
            [[59, 59, 69, 69], [59, 187, 69, 197], [59, 315, 69, 325],
             [59, 443, 69, 453], [187, 59, 197, 69], [187, 187, 197, 197],
             [187, 315, 197, 325], [187, 443, 197, 453], [315, 59, 325, 69],
             [315, 187, 325, 197], [315, 315, 325, 325], [315, 443, 325, 453],
             [443, 59, 453, 69], [443, 187, 453, 197], [443, 315, 453, 325],
             [443, 443, 453, 453]])

        self.assertTrue(np.array_equiv(boxes, expected))

    def test_default_boxes_for_all_feature_maps(self):
        aspect_ratios = [[1.], [1.]]

        feature_maps = [4, 2]
        strides = [128, 256]

        bases = [1, 1]

        boxes = default_boxes_for_all_feature_maps(bases, feature_maps,
                                                   aspect_ratios, strides)

        expected = np.array(
            [[63.5, 63.5, 64.5, 64.5], [63.5, 191.5, 64.5, 192.5],
             [63.5, 319.5, 64.5, 320.5], [63.5, 447.5, 64.5, 448.5],
             [191.5, 63.5, 192.5, 64.5], [191.5, 191.5, 192.5, 192.5],
             [191.5, 319.5, 192.5, 320.5], [191.5, 447.5, 192.5, 448.5],
             [319.5, 63.5, 320.5, 64.5], [319.5, 191.5, 320.5, 192.5],
             [319.5, 319.5, 320.5, 320.5], [319.5, 447.5, 320.5, 448.5],
             [447.5, 63.5, 448.5, 64.5], [447.5, 191.5, 448.5, 192.5],
             [447.5, 319.5, 448.5, 320.5], [447.5, 447.5, 448.5, 448.5],
             [127.5, 127.5, 128.5, 128.5], [127.5, 383.5, 128.5, 384.5],
             [383.5, 127.5, 384.5, 128.5], [383.5, 383.5, 384.5, 384.5]])

        self.assertTrue(np.array_equiv(boxes, expected))

    def test_default_boxes_for_all_feature_maps_base_values(self):
        aspect_ratios = [[1.], [1.]]

        feature_maps = [4, 2]
        strides = [128, 256]

        bases = [10, 100]

        boxes = default_boxes_for_all_feature_maps(bases, feature_maps,
                                                   aspect_ratios, strides)

        expected = np.array(
            [[59, 59, 69, 69], [59, 187, 69, 197], [59, 315, 69, 325],
             [59, 443, 69, 453], [187, 59, 197, 69], [187, 187, 197, 197],
             [187, 315, 197, 325], [187, 443, 197, 453], [315, 59, 325, 69],
             [315, 187, 325, 197], [315, 315, 325, 325], [315, 443, 325, 453],
             [443, 59, 453, 69], [443, 187, 453, 197], [443, 315, 453, 325],
             [443, 443, 453, 453], [78, 78, 178, 178], [78, 334, 178, 434],
             [334, 78, 434, 178], [334, 334, 434, 434]])

        self.assertTrue(np.array_equiv(boxes, expected))


if __name__ == "__main__":
    unittest.main()
