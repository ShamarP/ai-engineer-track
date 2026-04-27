"""Verify our scalar autograd matches PyTorch to within 1e-6.

This is the Done-when test for Week 1. If these pass, your micrograd is correct.

Strategy:
  Build the same expression in Value-land and torch-land with identical inputs.
  Check forward output and all leaf gradients match.
"""

import math
import sys
from pathlib import Path

import pytest
import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from value import Value  # noqa: E402


def test_simple_add_mul():
    """f(a, b, c) = (a*b + c)"""
    a = Value(2.0)
    b = Value(-3.0)
    c = Value(10.0)
    out = a * b + c
    out.backward()

    ta = torch.tensor(2.0, requires_grad=True)
    tb = torch.tensor(-3.0, requires_grad=True)
    tc = torch.tensor(10.0, requires_grad=True)
    tout = ta * tb + tc
    tout.backward()

    assert math.isclose(out.data, tout.item(), abs_tol=1e-6)
    assert math.isclose(a.grad, ta.grad.item(), abs_tol=1e-6)
    assert math.isclose(b.grad, tb.grad.item(), abs_tol=1e-6)
    assert math.isclose(c.grad, tc.grad.item(), abs_tol=1e-6)


def test_relu_tanh():
    """nonlinearities should match torch."""
    x = Value(0.5)
    y = x.relu().tanh() + (Value(-1.2)).relu()
    y.backward()

    tx = torch.tensor(0.5, requires_grad=True)
    tneg = torch.tensor(-1.2, requires_grad=True)
    ty = torch.relu(tx).tanh() + torch.relu(tneg)
    ty.backward()

    assert math.isclose(y.data, ty.item(), abs_tol=1e-6)
    assert math.isclose(x.grad, tx.grad.item(), abs_tol=1e-6)


def test_3layer_mlp_matches_pytorch():
    """The Done-when criterion: a 3-layer MLP must match torch within 1e-6.

    You'll need to: (a) build an MLP in value-land, (b) build an equivalent
    nn.Sequential in torch with the SAME weights, (c) verify forward + backward.

    Implement when you've finished value.py and nn.py.
    """
    pytest.skip("implement after value.py + nn.py are complete")
