

def f(x):
    return x * x

def derivative(x):
    return 2 * x

x = 10
lr = 0.1
iterations = 100

for i in range(iterations):
    x = x - lr * derivative(x)

print("Minimum x:", x)
print("Minimum value:", f(x))
