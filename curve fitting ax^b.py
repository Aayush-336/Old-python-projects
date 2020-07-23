import math
import two_var_eqs_solver

# def eqs(a1, b1, c1, a2, b2, c2):
#     sol_a = round(((c1 * b2) - (c2 * b1)) / ((a1 * b2) - (a2 * b1)), 4)
#     sol_b = round((c1 - a1 * sol_a) / b1, 4)
#     return sol_a, sol_b


x = list(map(float, input("Enter values of X:").split(' ')))
y = list(map(float, input("Enter values of Y:").split(' ')))
sumofx, sumofx2, sumofy, sumofxy = 0, 0, 0, 0
for i in range(len(x)):
    logx = math.log(x[i])
    logy = math.log(y[i])
    sumofx += logx
    sumofx2 += logx ** 2
    sumofy += logy
    sumofxy += logx * logy
    print(f"{i + 1}:  {round(logx, 4)}\t{round(logy, 4)}\t{round(logx * logy, 4)}\t{round(logx ** 2, 4)}")
sumofx = round(sumofx, 4)
sumofx2 = round(sumofx2, 4)
# print(sumofxy)
sumofxy = round(sumofxy, 4)
sumofy = round(sumofy, 3)
print("Sum of X: ", sumofx)
print("Sum of X^2: ", sumofx2)
print("Sum of Y: ", sumofy)
print("Sum of XY: ", sumofxy)
print(f"Equation : \n {sumofy} = {len(x)}A + {sumofx}B \n {sumofxy}={sumofx}A + {sumofx2}B\n")
A, B = two_var_eqs_solver.eqs(len(x), sumofx, sumofy, sumofx, sumofx2, sumofxy)
a=math.exp(A)
b=B
print("a=", a, "b=", b)
print(f"curve: y={a}*x^{b}")

