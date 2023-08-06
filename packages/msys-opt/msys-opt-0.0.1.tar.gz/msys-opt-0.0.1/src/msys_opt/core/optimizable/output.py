from .optimizable import OptimizableInterface
from .type import TypeInterface
import msys.core


class Output(msys.core.Output, OptimizableInterface):
    def __init__(self, type: TypeInterface, inputs=None, optimized=False):
        self.optimized = optimized
        super().__init__(type, inputs)

    def is_optimized(self) -> bool:
        return self.optimized

    def set_optimized(self, optimized: bool) -> bool:
        self.optimized = optimized
        return self.is_optimized()