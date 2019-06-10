from math import sqrt


class Operation:
    # joint variability of two variables operations.
    def __init__(self, dinogroup: list, x: str, y: str):
        self.dinogroup = dinogroup
        self.x = x
        self.y = y

        self.mean_x, self.mean_y = self.mean()
        self.var_x, self.var_y = self.variance()
        self.standard_deviation_x = sqrt(self.var_x)
        self.standard_deviation_y = sqrt(self.var_y)

        self.covariance = self._covariance()

    def mean(self):  # weighted arithmetic mean
        x = 0
        y = 0

        for dino in self.dinogroup:
            x += dino.__getattribute__(self.x)
            y += dino.__getattribute__(self.y)
        return x / len(self.dinogroup), y / len(self.dinogroup)

    def variance(self):  # https://en.wikipedia.org/wiki/Variance
        x = 0
        y = 0
        for dino in self.dinogroup:
            x += dino.__getattribute__(self.x) ^ 2
            y += dino.__getattribute__(self.y) ^ 2
        return (x / len(self.dinogroup)) - self.mean_x, (y / len(self.dinogroup)) - self.mean_y

    def _covariance(self):  # https://en.wikipedia.org/wiki/Covariance
        c = 0
        for dino in self.dinogroup:
            c += dino.__getattribute__(self.x) * dino.__getattribute__(self.y)

        return (c / len(self.dinogroup)) - (self.mean_x * self.mean_y)

    def correlation_coefficient(self):  # https://en.wikipedia.org/wiki/Correlation_coefficient
        return self.covariance / (self.standard_deviation_x * self.standard_deviation_y)
