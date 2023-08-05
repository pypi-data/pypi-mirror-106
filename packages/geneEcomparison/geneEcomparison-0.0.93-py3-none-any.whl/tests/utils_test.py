import unittest
import numpy as np
from numpy import testing as nptest

from geneEcomparison import Utils

class TestViewFunctions(unittest.TestCase):

  def test_zscore(self):
    result = Utils.z_score(np.asarray([1, 3 , 5]))
    
    # https://stackoverflow.com/questions/3302949/best-way-to-assert-for-numpy-array-equality
    nptest.assert_allclose(result, np.asarray([-1.22474487,  0,  1.22474487]))
    
