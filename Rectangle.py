import numpy as np


class Rectangle:
    def __init__(self, top_left_point: list[float], bottom_right_point: list[float]):
        """Creates a rectangle given the [x,y] coordinates of the top left point and the bottom right point"""
        self.top_left_point = top_left_point
        self.bottom_right_point = bottom_right_point

    @staticmethod
    def generate_random_rectangle(
        x_bounds: list[float], y_bounds: list[float]
    ) -> "Rectangle":
        """Generates a random rectangle within the boundaries given"""
        # Generate random points and sort them in ascendent form
        x_coords = np.sort(np.random.uniform(x_bounds[0], x_bounds[1], 2))
        y_coords = np.sort(np.random.uniform(y_bounds[0], y_bounds[1], 2))

        top_left_p = [x_coords[0], y_coords[1]]
        bottom_right_p = [x_coords[1], y_coords[0]]

        return Rectangle(top_left_p, bottom_right_p)

    def is_contained(self, point: list[float]) -> bool:
        """Given a point [x,y] returns if the point is contained in the rectangle"""
        x, y = point
        is_in_rectangle_x_bounds = (
            x >= self.top_left_point[0] and x <= self.bottom_right_point[0]
        )
        is_in_rectangle_y_bounds = (
            y <= self.top_left_point[1] and y >= self.bottom_right_point[1]
        )
        is_in_rectangle = is_in_rectangle_x_bounds and is_in_rectangle_y_bounds

        return is_in_rectangle

    def get_contained_points(self, points: np.ndarray) -> np.ndarray:
        """Returns the list of points contained within the rectangle"""
        contained_points = []
        for p in points:
            if self.is_contained(p):
                contained_points.append(p)
        return np.array(contained_points)
