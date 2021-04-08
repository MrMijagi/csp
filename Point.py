from __future__ import annotations
from math import hypot, atan2


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Point) -> Point:
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other: Point) -> Point:
        if isinstance(other, Point):
            self.x += other.x
            self.y += other.y
            return self

    def distance_to_point(self, other: Point) -> float:
        return hypot(self.x - other.x, self.y - other.y)

    def polar_angle_to_point(self, other: Point) -> float:
        return atan2(other.y - self.y, other.x - self.x)

    def __repr__(self) -> str:
        return f'{self.x};{self.y}'

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'
