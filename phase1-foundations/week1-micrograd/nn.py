"""Neural-net primitives built on top of Value.

Reference: https://github.com/karpathy/micrograd/blob/master/micrograd/nn.py

Implement:
- Neuron: w · x + b → activation
- Layer: a list of Neurons
- MLP:   a list of Layers

Each should expose `.parameters()` returning all trainable Values, so the training
loop can zero gradients and apply SGD updates.
"""

from value import Value  # noqa: F401  (you'll use this once you implement)


class Module:
    """Base class. Subclasses get `zero_grad` for free."""

    def zero_grad(self):
        for p in self.parameters():
            p.grad = 0

    def parameters(self):
        return []


class Neuron(Module):
    def __init__(self, nin, nonlin=True):
        raise NotImplementedError

    def __call__(self, x):
        raise NotImplementedError

    def parameters(self):
        raise NotImplementedError


class Layer(Module):
    def __init__(self, nin, nout, **kwargs):
        raise NotImplementedError

    def __call__(self, x):
        raise NotImplementedError

    def parameters(self):
        raise NotImplementedError


class MLP(Module):
    def __init__(self, nin, nouts):
        """nin = input dim, nouts = list of layer sizes."""
        raise NotImplementedError

    def __call__(self, x):
        raise NotImplementedError

    def parameters(self):
        raise NotImplementedError
