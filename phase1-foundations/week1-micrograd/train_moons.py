"""Train an MLP on sklearn's make_moons and plot the decision boundary.

Loosely follows: https://github.com/karpathy/micrograd/blob/master/demo.ipynb

Goal: 200 points, 2D input, hinge or MSE loss, decision-boundary plot saved
to `decision_boundary.png` in this folder.

Pseudocode:
    X, y = make_moons(n_samples=200, noise=0.1)
    y = 2*y - 1                         # remap to {-1, 1}

    model = MLP(2, [16, 16, 1])

    for step in range(100):
        # forward — vectorize over batch
        ypred = [model([Value(xi[0]), Value(xi[1])]) for xi in X]

        # svm-style max-margin loss + L2 reg
        losses = [(1 + -yi*scorei).relu() for yi, scorei in zip(y, ypred)]
        data_loss = sum(losses) * (1.0 / len(losses))
        reg_loss = 1e-4 * sum((p*p for p in model.parameters()))
        total_loss = data_loss + reg_loss

        # accuracy
        accuracy = [
            (yi > 0) == (scorei.data > 0)
            for yi, scorei in zip(y, ypred)
        ]
        acc = sum(accuracy) / len(accuracy)

        # backward
        model.zero_grad()
        total_loss.backward()

        # SGD with decaying learning rate
        lr = 1.0 - 0.9 * step / 100
        for p in model.parameters():
            p.data -= lr * p.grad

        if step % 10 == 0:
            print(f"step {step:3d}  loss {total_loss.data:.4f}  acc {acc*100:.1f}%")

    # plot decision boundary — see karpathy's demo notebook for the snippet
"""

if __name__ == "__main__":
    raise NotImplementedError("implement training loop")
