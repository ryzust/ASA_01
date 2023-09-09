import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from Frame import Frame


def draw_rectangle():
    pass


if __name__ == "__main__":
    f = Frame()
    fig, ax = plt.subplots()
    ax.plot(
        [f.top_rectangle[0][0], f.top_rectangle[1][0]],
        [f.top_rectangle[0][0], f.top_rectangle[0][0]],
    )
    w = f.top_rectangle[1][0] - f.top_rectangle[0][0]
    h = f.top_rectangle[0][1] - f.top_rectangle[1][1]
    ax.add_patch(
        Rectangle((f.top_rectangle[0][0], f.top_rectangle[1][1]), w, h, fill=False)
    )
    plt.show()
