from numpy import arange

def polynomial(x):
    return x*x*x + 3*x*x - 5*x + 7


with open("polynomial.csv","w") as file:
    file.write("x,y\n")
    for i in range(2000):
        x = 0.001*i - 1
        file.write(f"{x},{polynomial(x)}\n")