from src.basic import Simple


x = Simple(10)
x_squared = x.squared()
print(x_squared)


print(Simple(20).squared())
for _ in range(10):
    print("The weather is good")

print(Simple("a").squared())

try:
    print("The weather today" ** 2)
except:
    raise TypeError("Type error")


print("Exited with status 1")
