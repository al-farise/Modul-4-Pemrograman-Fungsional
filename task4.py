import math

def translation(tx, ty):
    return lambda x, y: (x + tx, y + ty)

def dilatation(sx, sy):
    def transform(x, y):
        x = (x * sx) + (y * 0)
        y = (x * 0) + (y * sy)
        return x, y
    return transform

def rotation(degree):
    def transform(x, y):
        x = x * math.cos(math.radians(degree)) - y * math.sin(math.radians(degree))
        y = x * math.sin(math.radians(degree)) + y * math.cos(math.radians(degree))
        return x, y
    return transform

# Translasi
translation_point = translation(2, -1)
translation_result = translation_point(3, 5)
print(f"Koordinat setelah translasi: " + str(translation_result))

# Dilatasi
dilatation_point = dilatation(2, -1)
dilatation_result = dilatation_point(3, 5)
print(f"Koordinat setelah dilatasi: " + str(dilatation_result))

# Rotasi
rotation_point = rotation(30)
rotation_result = rotation_point(3, 5)
print(f"Koordinat setelah rotasi: " + str(rotation_result))