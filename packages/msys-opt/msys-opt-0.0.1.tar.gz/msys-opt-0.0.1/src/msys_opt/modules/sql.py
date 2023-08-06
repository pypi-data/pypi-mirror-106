from ..core import Module
from ..core.optimizable import Input, Output


class SQL(Module):
    def __init__(self):
        super().__init__(inputs=[Input(), Input()], outputs=[Output()])