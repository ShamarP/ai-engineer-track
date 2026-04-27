"""Scalar autograd engine — implement from scratch following Karpathy's micrograd video.

Reference: https://github.com/karpathy/micrograd/blob/master/micrograd/engine.py

You're implementing a `Value` that wraps a scalar and tracks a computational graph
for reverse-mode automatic differentiation.

Required:
- arithmetic: __add__, __mul__, __pow__, __neg__, __sub__, __truediv__ (and r-variants)
- nonlinearities: relu, tanh
- backprop: backward()

Don't peek at the reference until you've made an honest attempt.
"""


class Value:
    """A scalar value in the computational graph."""

    def __init__(self, data, _children=(), _op=""):
        raise NotImplementedError("implement Value.__init__")

    # arithmetic
    def __add__(self, other):
        raise NotImplementedError

    def __mul__(self, other):
        raise NotImplementedError

    def __pow__(self, other):
        raise NotImplementedError

    # nonlinearities
    def relu(self):
        raise NotImplementedError

    def tanh(self):
        raise NotImplementedError

    # backprop
    def backward(self):
        raise NotImplementedError

    # nice-to-haves you'll add along the way:
    # __neg__, __sub__, __radd__, __rmul__, __truediv__, __repr__
