import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
from Frame import Frame


def draw_rectangle(ax, rect_points: list[list[float]]):
    p1, p2 = rect_points
    w = p2[0] - p1[0]
    h = p1[1] - p2[1]
    ax.add_patch(Rectangle((p1[0], p2[1]), w, h, fill=False))


if __name__ == "__main__":
    f = Frame()

    n = 50
    points = np.random.random([n, 2])
    p_is_positive = [f.is_positive(x) for x in points]
    positive_points = points[np.array(p_is_positive)]
    negative_points = points[~np.array(p_is_positive)]

    fig, ax = plt.subplots()
    plt.tight_layout()
    for p in negative_points:
        ax.plot(p[0], p[1], "rx")
    for p in positive_points:
        ax.plot(p[0], p[1], "g.")
    draw_rectangle(ax, f.bottom_rectangle)
    draw_rectangle(ax, f.top_rectangle)
    plt.show()
