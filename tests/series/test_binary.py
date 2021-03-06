from unittest import TestCase

import numpy
from pandas import Series, DataFrame
from pandas.util.testing import assert_frame_equal

from pdprpr.series import BinarySeriesPreprocessor

from ..helper import array_uint8


class TestBinarySeriesPreprocessor(TestCase):
    def test_process(self):
        pp = BinarySeriesPreprocessor()
        target = Series([0, 1, numpy.nan])
        result = pp.process(target)
        expected = DataFrame({
            'TRUE': array_uint8([0, 1, 1]),
        })
        assert_frame_equal(result, expected)

    def test_process_fillna(self):
        pp = BinarySeriesPreprocessor(fillval=False)
        target = Series([0, 1, numpy.nan])
        result = pp.process(target)
        expected = DataFrame({
            'TRUE': array_uint8([0, 1, 0]),
        })
        assert_frame_equal(result, expected)
