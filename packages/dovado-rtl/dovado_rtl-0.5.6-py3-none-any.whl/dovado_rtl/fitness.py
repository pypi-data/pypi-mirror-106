from dovado_rtl.point_evaluation import DesignPointEvaluator
from dovado_rtl.config import Configuration
from typing import Tuple, List

from dovado_rtl.abstract_classes import AbstractFitnessEvaluator
from movado import approximate


class FitnessEvaluator(AbstractFitnessEvaluator):
    def __init__(
        self,
        evaluator: DesignPointEvaluator,
        config: Configuration,
    ):
        self.__evaluator: DesignPointEvaluator = evaluator
        self.__config: Configuration = config

    @approximate()
    def fitness(self, design_point: Tuple[int, ...]) -> List[float]:
        return list(self.__evaluator.evaluate(design_point).value.values())
