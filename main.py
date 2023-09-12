import random
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
from Frame import Frame
from Model import Model
from sklearn.metrics import accuracy_score, classification_report


def draw_rectangle(ax, rectangle: Rectangle, color: str = "blue", msg: str = ""):
    p1, p2 = rectangle.top_left_point, rectangle.bottom_right_point
    w = p2[0] - p1[0]
    h = p1[1] - p2[1]
    ax.text(p2[0], p2[1], msg, color=color)
    ax.add_patch(Rectangle((p1[0], p2[1]), w, h, fill=False, color=color))


def plot_points_by_class(ax, points, labels):
    for i in range(len(points)):
        point = points[i]
        is_positive = labels[i]
        if is_positive:
            ax.plot(point[0], point[1], "g.")
            continue

        ax.plot(point[0], point[1], "rx")


if __name__ == "__main__":
    # random.seed(0)
    # np.random.seed(0)
    flag = True
    while flag:
        f = Frame.generate_random_frame()

        # n will be used as the number of samples in the training set (80%)
        n = int(input("Insert the number of points in the set: "))
        # additionally, it'll have 20% as the testing set
        n += int((n * 0.2) / 0.8)

        points = np.random.random([n, 2])
        # true if positive, false if negative
        labels = np.array([f.is_positive(x) for x in points])
        n_positive_examples = len(labels[: int(n * 0.8)][labels[: int(n * 0.8)]])

        while n_positive_examples < 4:
            p = [f.generate_positive_point()]
            points = np.concatenate((np.array(p), points))
            labels = np.concatenate((np.array([True]), labels))
            n_positive_examples += 1

        add_more = input(
            f"{n_positive_examples} positive examples were generated. Do you want to add more? (y/n): "
        )
        if add_more.lower() == "y":
            new_n = int(input("How many?: "))
            limit = new_n + n_positive_examples
            while n_positive_examples < limit:
                p = [f.generate_positive_point()]
                points = np.concatenate((np.array(p), points))
                labels = np.concatenate((np.array([True]), labels))
                n_positive_examples += 1

        X_train = points[: int(n * 0.8)]
        y_train = labels[: int(n * 0.8)]

        X_test = points[int(n * 0.8) :]
        y_test = labels[int(n * 0.8) :]

        fig, ax = plt.subplots(ncols=2)
        plt.tight_layout()
        ax[0].set_title("Training set")
        ax[1].set_title("Test set")
        plot_points_by_class(ax[0], X_train, y_train)
        plot_points_by_class(ax[1], X_test, y_test)
        draw_rectangle(ax[0], f.outer_rectangle, msg="M")
        draw_rectangle(ax[0], f.inner_rectangle)
        draw_rectangle(ax[1], f.outer_rectangle, msg="M")
        draw_rectangle(ax[1], f.inner_rectangle)

        model = Model()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        print(
            f"Accuracy reached on training set: {accuracy_score(y_train,model.predict(X_train))}"
        )
        print(f"Accuracy reached on test set: {accuracy_score(y_test,y_pred)}")

        draw_rectangle(ax[0], model.f_h.outer_rectangle, color="purple", msg=r"$M_h$")
        draw_rectangle(ax[0], model.f_h.inner_rectangle, color="purple")
        draw_rectangle(ax[1], model.f_h.outer_rectangle, color="purple", msg=r"$M_h$")
        draw_rectangle(ax[1], model.f_h.inner_rectangle, color="purple")

        plt.show()
        flag = input("Do you want to try with another set? (y/n): ").lower() == "y"
