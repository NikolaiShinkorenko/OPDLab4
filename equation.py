import math

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def equation(a_coef, b_coef, c_coef):
    if a_coef == "" or is_number(a_coef) is False or float(a_coef) == 0:
        raise TypeError
    else:
        a = float(a_coef)

    if b_coef == "" or b_coef is None:
        b = 0
    elif is_number(b_coef):
        b = float(b_coef)
    else:
        raise TypeError

    if c_coef == "" or c_coef is None:
        c = 0
    elif is_number(c_coef):
        c = float(c_coef)
    else:
        raise TypeError

    discriminant = (b * b) - (4 * a * c)
    if discriminant < 0:
        return "Действительных корней нет"
    else:
        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        else:
            x1 = x2 = -b / (2 * a)
        return [round(x1, 2), round(x2, 2)]