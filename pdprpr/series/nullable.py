import math

import numpy
from attr import attrs, attrib

from ._base import BaseSeriesPreprocessor


@attrs
class NullableSeriesPreprocessor(BaseSeriesPreprocessor):
    kind = 'nullable'

    nullval = attrib(default='AUTO')

    def process(self, series):
        return self._isnull(series).astype(numpy.uint8).to_frame('NULL')

    def _isnull(self, series):
        if self.nullval == 'AUTO':
            return series.isnull()
        elif self.nullval is None:
            return series.map(lambda x: x is None)
        elif isinstance(self.nullval, float) and math.isnan(self.nullval):
            return series.map(numpy.isnan)
        else:
            return series == self.nullval
