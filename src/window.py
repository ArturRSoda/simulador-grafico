from transformator import Transformator

class Window:
    def __init__(self, coordinates: list[tuple[float, float]]):
        # p0, p1, p2, p3 | p0 -> w_min, p2 -> w_max
        self.coordinates : list[tuple[float, float]]

        self.coordinates = coordinates


    def get_center(self):
        coordinates = self.coordinates
        coords = [tuple(t) for t in coordinates]
        if (coords[0] == coords[-1]) and (len(coords) > 1):
            coords.pop()

        average_x, average_y = 0, 0
        for x, y in coords:
            average_x += x
            average_y += y
        points_num = len(coords)
        average_x /= points_num
        average_y /= points_num

        return (average_x, average_y)


    def set_coordinates(self, new_coord: list[tuple[float, float]]):
        self.coordinates = new_coord


    def rotate(self, transformator: Transformator, degrees: int):
        transformation_list = []
        transformator.add_rotation(transformation_list, degrees, self.get_center())
        self.coordinates = transformator.transform(self.coordinates, transformation_list)


    def zoom(self, transformator: Transformator, factor: float):
        transformation_list = []
        transformator.add_scaling(transformation_list, factor)
        self.coordinates = transformator.transform(self.coordinates, transformation_list)


    def move(self, transformator: Transformator, offset_x: float, offset_y: float):
        transformation_list = []
        transformator.add_translation(transformation_list, offset_x, offset_y)
        self.coordinates = transformator.transform(self.coordinates, transformation_list)

