from .optimizable import OptimizableInterface
from .type import TypeInterface
from msys.core import Input


class Input(Input, OptimizableInterface):
    """A class to connect to one Output.

       Inputs can have multiple Types to be very flexible when trying to connect to an Output.
       On Input can only be connected to one Output but one Output can have multiple connected Inputs.

       Attributes:
           types (list): a list of types with which the input tries to parse the type of the output
           type_id (int): the index of the type, with which a successfull connection was made
           connection (Output): the connected output
    """
    def __init__(self, type: TypeInterface, output=None, optimized=False):
        """Input Constructor

        Note:
            Do not include the `self` parameter in the ``Args`` section
        Args:
            types (:obj:`list`, optional): Description of `param1`.
            connection (:obj:`Output`, optional): Description of `param2`.
        """
        self.optimized = optimized
        super().__init__(type, output)

    def is_optimized(self) -> bool:
        if self.output:
            return False
        return self.optimized

    def set_optimized(self, optimized: bool) -> bool:
        self.optimized = optimized
        return self.is_optimized()
