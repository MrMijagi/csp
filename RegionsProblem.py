from Point import Point
from Region import Region
from random import randrange, choice
from copy import deepcopy


def get_regions(points: list[Point], connections: [list[list[int, int]]]) -> list[Region]:
    """ returns list of regions created by dividing original region by lines created by connections """
    return []


def is_connection_legal(p1: Point, p2: Point, points: list[Point], connections: list[list[int, int]]) -> bool:
    """ returns true if p1 and p2 can be connected """

    p1_index = points.index(p1)
    p2_index = points.index(p2)

    # same point
    if p1_index == p2_index:
        return False

    for connection in connections:
        # check if one end of connection is p1 or p2
        # (also if connection connects p1 and p2)
        if p1_index in connection or p2_index in connection:
            return False

        # check if connection between p1 and p2 will intersect with other connection
        connection_start = points[connection[0]]
        connection_end = points[connection[1]]

        if intersect(p1, p2, connection_start, connection_end):
            return False

    return True


def can_connect(point: Point, points: list[Point], connections: list[list[int, int]]) -> bool:
    """ returns true if point can be connected to any other point, false otherwise """

    for p in points:
        if is_connection_legal(p, point, points, connections):
            return True

    return False


def ccw(A: Point, B: Point, C: Point) -> int:
    return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)


def intersect(A: Point, B: Point, C: Point, D: Point) -> bool:
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


class RegionsProblem:
    def __init__(self, x_size: int, y_size: int, n: int, regions: list[Region] = None) -> None:
        self.x_size = x_size
        self.y_size = y_size
        self.n = n
        self.regions = []
        if regions is not None:
            self.regions = regions

    def get_random_point(self) -> Point:
        return Point(randrange(0, self.x_size), randrange(0, self.y_size))

    def generate_starting_region(self) -> None:
        """ Creates random points inside board and finds biggest convex polygon using Graham scan """
        point_list = list(set([self.get_random_point() for _ in range(self.n)]))

        # find most bottom-left point
        point_list.sort(key=lambda p: (p.y, p.x))
        p0 = point_list[0]

        # sort by polar angle
        point_list.sort(key=lambda p: p0.polar_angle_to_point(p))

        point_stack = []
        for point in point_list:
            while len(point_stack) > 1 and ccw(point_stack[-2], point_stack[-1], point) < 0:
                point_stack.pop()
            point_stack.append(point)

        self.regions.append(Region(point_stack))

    def divide_starting_region(self) -> None:
        """ divide big region into random regions """
        all_points = self.regions[0].points
        points_available = deepcopy(all_points)
        connections: list[list[int, int]] = []

        # add connections from starting region
        for i in range(len(all_points) - 1):
            connections.append([i, i+1])

        while len(points_available) > 0:
            p: Point = choice(points_available)

            if can_connect(p, all_points, connections):
                points_available.sort(key=lambda curr_p: p.distance_to_point(curr_p))

                for point in points_available:
                    if is_connection_legal(p, point, all_points, connections):
                        connections.append([all_points.index(p), all_points.index(point)])
                        break
            else:
                points_available.remove(p)

        self.regions = get_regions(all_points, connections)
