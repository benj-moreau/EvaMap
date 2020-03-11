from EvaMap.Dimensions.Dimension import Dimension
from EvaMap.Metrics.verticalCoverage import verticalCoverage


class Coverability(Dimension):

    def __init__(self, nom='Coverability', list_metrics=[verticalCoverage]):
        super().__init__(nom, list_metrics)
