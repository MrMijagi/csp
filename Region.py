from __future__ import annotations
from Point import Point


class Region:
    def __init__(self, points: list[Point] = None, neighbors: list[Region] = None):
        self.points = []
        if points is not None:
            self.points = points

        self.neighbors = []
        if neighbors is None:
            self.neighbors = neighbors
