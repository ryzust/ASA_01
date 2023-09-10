import random
import numpy as np


class Frame:
    @staticmethod
    def generate_rectangle(
        x_bounds: list[float], y_bounds: list[float]
    ) -> list[list[float]]:
        # Generate random points and sort them in ascendent form
        x_coords = np.sort(np.random.uniform(x_bounds[0], x_bounds[1], 2))
        y_coords = np.sort(np.random.uniform(y_bounds[0], y_bounds[1], 2))

        top_left_p = [x_coords[0], y_coords[1]]
        bottom_right_p = [x_coords[1], y_coords[0]]

        return [top_left_p, bottom_right_p]

    def __init__(self):
        tr_top_left_p, tr_bottom_right_p = Frame.generate_rectangle([0, 1], [0, 1])
        br_top_left_p, br_bottom_right_p = Frame.generate_rectangle(
            [tr_top_left_p[0], tr_bottom_right_p[0]],
            [tr_top_left_p[1], tr_bottom_right_p[1]],
        )

        self.top_rectangle = [tr_top_left_p, tr_bottom_right_p]
        self.bottom_rectangle = [br_top_left_p, br_bottom_right_p]

    def is_positive(self, p: list[float]) -> bool:
        x, y = p

        # to be positive, the point must be inside the top rectangle but outside the bottom one
        is_in_top_rectangle_x_bounds = (
            x >= self.top_rectangle[0][0] and x <= self.top_rectangle[1][0]
        )
        is_in_top_rectangle_y_bounds = (
            y <= self.top_rectangle[0][1] and y >= self.top_rectangle[1][1]
        )
        is_inside_top_rectangle = (
            is_in_top_rectangle_x_bounds and is_in_top_rectangle_y_bounds
        )

        is_in_bottom_rectangle_x_bounds = (
            x >= self.bottom_rectangle[0][0] and x <= self.bottom_rectangle[1][0]
        )
        is_in_bottom_rectangle_y_bounds = (
            y <= self.bottom_rectangle[0][1] and y >= self.bottom_rectangle[1][1]
        )
        is_out_bottom_rectangle = not (
            is_in_bottom_rectangle_x_bounds and is_in_bottom_rectangle_y_bounds
        )

        return is_inside_top_rectangle and is_out_bottom_rectangle

    def generate_positive_point(self) -> list[list[float]]:
        x = np.random.uniform(self.top_rectangle[0][0], self.top_rectangle[1][0])
        y = 0.0

        x_doesnt_intersect_bottom_rectangle = (
            x < self.bottom_rectangle[0][0] or x > self.bottom_rectangle[1][0]
        )
        if x_doesnt_intersect_bottom_rectangle:
            y = np.random.uniform(self.top_rectangle[0][0], self.top_rectangle[1][0])
        else:
            y_generates_at_top = random.randint(0, 1) == 1
            if y_generates_at_top:
                y = np.random.uniform(
                    self.top_rectangle[0][1], self.bottom_rectangle[0][1]
                )
            else:
                y = np.random.uniform(
                    self.bottom_rectangle[1][1], self.top_rectangle[1][1]
                )

        return [x, y]
