import numpy as np
from Frame import Frame
from Rectangle import Rectangle


class Model:
    def __init__(self, f: Frame):
        self.f = f

    def _update_border_coords(border_coords, example):
        for i, val in enumerate(example):
            # minimize
            if val < border_coords[(i * 2)]:
                border_coords[(i * 2)] = val
            # maximize
            if val > border_coords[(i * 2) + 1]:
                border_coords[(i * 2) + 1] = val

    def _get_border_coords(X: np.ndarray) -> np.ndarray:
        """returns a 2 * len(x[0]) dimensional array containing the minimum and maximum values for each dimension in X"""
        n_dimensions = len(X[0])
        border_coords = np.zeros(n_dimensions * 2)
        for example in X:
            Model._update_border_coords(border_coords, example)
        return border_coords

    def fit(self, X: np.ndarray, y: np.ndarray):
        """Fits the model with the X examples and y labels"""
        # Exploiting the fact that y is a boolean array
        positive_points = X[y]
        negative_points = X[~y]

        border_coords = Model._get_border_coords(positive_points)

        right_rectangle = Rectangle(
            [border_coords[1], border_coords[3]], [1, border_coords[2]]
        )
        left_rectangle = Rectangle(
            [0, border_coords[3]], [border_coords[0], border_coords[2]]
        )
        upper_rectangle = Rectangle(
            [border_coords[0], 1], [border_coords[1], border_coords[3]]
        )
        lower_rectangle = Rectangle(
            [border_coords[0], border_coords[2]], [border_coords[1], 1]
        )

        # right rectangle contained points...
        r_r_contained_points = right_rectangle.get_contained_points(negative_points)
        lf_r_contained_points = left_rectangle.get_contained_points(negative_points)
        u_r_contained_points = upper_rectangle.get_contained_points(negative_points)
        lw_r_contained_points = lower_rectangle.get_contained_points(negative_points)

        outer_min_x, _, _, _ = Model._get_border_coords(lf_r_contained_points)
        _, outer_max_x, _, _ = Model._get_border_coords(r_r_contained_points)
        _, _, outer_min_y, _ = Model._get_border_coords(lw_r_contained_points)
        _, _, _, outer_max_y = Model._get_border_coords(u_r_contained_points)

        outer_rectangle = Rectangle(
            [outer_min_x, outer_max_y], [outer_max_x, outer_min_y]
        )

        negative_points_in_inner_rect = outer_rectangle.get_contained_points(
            negative_points
        )
        if len(negative_points_in_inner_rect) == 0:
            inner_rectangle = Rectangle.generate_random_rectangle(
                [outer_min_x, outer_max_x], [outer_min_y, outer_max_y]
            )
        else:
            (
                inner_min_x,
                inner_max_x,
                inner_min_y,
                inner_max_y,
            ) = Model._get_border_coords(lf_r_contained_points)

            inner_rectangle = Rectangle(
                [inner_min_x, inner_max_y], [inner_max_x, inner_min_y]
            )

        self.f_h = Frame(outer_rectangle, inner_rectangle)

    def predict(self, X: np.ndarray):
        """Predicts the labels on a set based on the hypotesis obtained"""
        if self.f_h == None:
            raise Exception(
                "The frame hypothesis isn't defined. Make sure of training the model first"
            )

        y_pred = np.zeros(len(X))
        for i, x in enumerate(X):
            y_pred[i] = self.f_h.is_positive(x)

        return y_pred
