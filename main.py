import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import Frame
from Model import Model


def draw_rectangle(ax, rectangle: Rectangle):
    p1, p2 = rectangle.top_left_point, rectangle.bottom_right_point
    w = p2[0] - p1[0]
    h = p1[1] - p2[1]
    ax.add_patch(Rectangle((p1[0], p2[1]), w, h, fill=False))


def plot_points_by_class(ax, points, labels):
    for i in range(len(points)):
        point = points[i]
        is_positive = labels[i]
        if is_positive:
            ax.plot(point[0], point[1], "g.")
            continue

        ax.plot(point[0], point[1], "rx")


if __name__ == "__main__":
    f = Frame.generate_random_frame()

    # n will be used as the number of samples in the training set (80%)
    n = 50
    # additionally, it'll have 20% as the testing set
    n += int((n * 0.2) / 0.8)

    points = np.random.random([n, 2])
    # true if positive, false if negative
    labels = np.array([f.is_positive(x) for x in points])
    n_positive_examples = len(labels[int(n * 0.8)][labels])

    while n_positive_examples < 4:
        points = np.concatenate(np.array([f.generate_positive_point()]), points)
        labels += np.concatenate(np.array([True]), labels)

    X_train = points[: int(n * 0.8)]
    y_train = labels[: int(n * 0.8)]

    X_test = points[int(n * 0.8) :]
    y_test = labels[int(n * 0.8) :]

    model = Model(f)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    fig, ax = plt.subplots()
    plt.tight_layout()
    plot_points_by_class(ax, points, labels)
    draw_rectangle(ax, f.outer_rectangle)
    draw_rectangle(ax, f.inner_rectangle)
    plt.show()
