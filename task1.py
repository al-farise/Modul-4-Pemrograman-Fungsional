# Curry function
def perkalian(a):
    def dengan(b):
        return a * b
    return dengan


# HoF
x = perkalian(20)
y = x(20)

print(y)

# Currying
print(perkalian(10)(29))
