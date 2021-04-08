from random import choice


class RegionsDomain:
    colors = [
        "red",
        "blue",
        "green",
        "yellow",
        "purple",
        "cyan"
    ]

    def __init__(self, values: list[str], k: int) -> None:
        self.values = values
        self.k = k

    def random_value(self) -> str:
        return choice(RegionsDomain.colors[:self.k])

    def get_domain_values(self) -> list[str]:
        return RegionsDomain.colors[:self.k]
