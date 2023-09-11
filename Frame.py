import random
import numpy as np
from Rectangle import Rectangle


class Frame:
    def __init__(self, outer_rectangle: Rectangle, inner_rectangle: Rectangle):
        self.outer_rectangle = outer_rectangle
        self.inner_rectangle = inner_rectangle

    @staticmethod
    def generate_random_frame() -> "Frame":
        outer_rectangle = Rectangle.generate_random_rectangle([0, 1], [0, 1])
        outer_rectangle_x_bounds = [
            outer_rectangle.top_left_point[0],
            outer_rectangle.bottom_right_point[0],
        ]
        outer_rectangle_y_bounds = [
            outer_rectangle.bottom_right_point[1],
            outer_rectangle.top_left_point[1],
        ]

        inner_rectangle = Rectangle.generate_random_rectangle(
            outer_rectangle_x_bounds, outer_rectangle_y_bounds
        )
        return Frame(outer_rectangle, inner_rectangle)

    def is_positive(self, p: list[float]) -> bool:
        # to be positive, the point must be inside the top rectangle but outside the bottom one
        is_in_outer_rectangle = self.outer_rectangle.is_contained(p)
        is_out_inner_rectangle = not self.inner_rectangle.is_contained(p)

        return is_in_outer_rectangle and is_out_inner_rectangle

    def generate_positive_point(self) -> list[float]:
        """Generates a [x,y] random positive point within the boundaries of the frame"""
        x = np.random.uniform(
            self.outer_rectangle.top_left_point[0],
            self.outer_rectangle.bottom_right_point[0],
        )
        y = 0.0

        x_doesnt_intersect_inner_rectangle = (
            x < self.inner_rectangle.top_left_point[0]
            or x > self.inner_rectangle.bottom_right_point[0]
        )
        if x_doesnt_intersect_inner_rectangle:
            y = np.random.uniform(
                self.outer_rectangle.top_left_point[1],
                self.outer_rectangle.bottom_right_point[1],
            )
            return [x, y]

        y_generates_at_top = random.randint(0, 1) == 1
        if y_generates_at_top:
            y = np.random.uniform(
                self.outer_rectangle.top_left_point[1],
                self.inner_rectangle.top_left_point[1],
            )
        else:
            y = np.random.uniform(
                self.inner_rectangle.bottom_right_point[1],
                self.outer_rectangle.bottom_right_point[1],
            )

        return [x, y]
