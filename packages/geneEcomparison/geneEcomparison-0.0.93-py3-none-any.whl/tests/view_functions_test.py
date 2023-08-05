import unittest
from geneEcomparison import Visualisation

class TestViewFunctions(unittest.TestCase):
  def test_coexpressions(self):
    # https://docs.python-guide.org/writing/structure/
    # https://gist.github.com/tasdikrahman/2bdb3fb31136a3768fac
    webApp = Visualisation.WebInterface(__name__) 
    result = webApp.coexpressions(aggregation_function='mean', structure_level=3, species='human', gene1='Gabra4', gene2='Gabra1', side='left')

    self.assertIsNotNone(result)
