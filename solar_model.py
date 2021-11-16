# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    G = gravitational_constant
    for obj in space_objects:
        if body.x == obj.x and body.y == obj.y:
            continue  # тело не действует гравитационной силой на само себя!
        else:
            r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
            F = (G * body.m * obj.m) / r**2
            tg_angle = (body.y - obj.y) / (body.x - obj.x)
            Fx = F / (1 + (tg_angle)**2)**0.5
            Fy = (F**2 - Fx**2)**0.5
            body.Fx += Fx
            body.Fy += Fy


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """
    
    body.ax = body.Fx/body.m
    body.x += body.Vx + (((body.ax) * dt**2) / 2)  # FIXME: не понимаю как менять...
    body.Vx += body.ax*dt
    body.ay = body.Fy/body.m
    body.y += body.Vy + (((body.ay) * dt**2) / 2)  # FIXME: не понимаю как менять...
    body.Vy += body.ay*dt


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
