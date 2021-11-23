# coding: utf-8
# license: GPLv3


class CelestialBody:
    """
    Kласс, описывающий любое космическое тело.
    Содержит массу, координаты, скорость объекта,
    а также визуальный радиус в пикселах и его цвет.
    """

    def __init__(self, type, R, color, m, x, y, Vx, Vy):
        self.type = type.lower()
        self.R = R
        self.color = color
        self.m = m
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.Fx = None
        self.Fy = None
        self.image = None

    def move(self, dt):
        """
        Изменяет координаты и скорости тело за малое время dt.

        Параметры:
        dt - шаг по времени.
        """
        dt *= 3600
        self.x += self.Vx * dt
        self.y += self.Vy * dt
        self.Vx += self.Fx / self.m * dt
        self.Vy += self.Fy / self.m * dt
