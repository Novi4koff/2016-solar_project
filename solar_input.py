# coding: utf-8
# license: GPLv3

from solar_objects import CelestialBody


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type in ["star", "planet"]:  
                object_parameters = parse_parameters(line)
                body = CelestialBody(*object_parameters)
                objects.append(body)
            else:
                print("Unknown space object")

    return objects


def parse_parameters(line):
    """Считывает данные о звезде/планете из строки.
    Входная строка должна иметь слеюущий формат:
    Star/Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты тела, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описанием тела.
    """
    obj_params = []
    for data in line.strip().split():
        try:
            obj_params.append(float(data))
        except:
            obj_params.append(data)
    return obj_params

def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            params = [obj.type.title(), obj.R, obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy]
            string = ' '.join(map(str, params)) + '\n'
            out_file.write(string)
# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...

if __name__ == "__main__":
    print("This module is not for direct call!")
