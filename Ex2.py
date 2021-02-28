# This program allows the user to approximate a solution to an initial value problem for a differential equation,
# and then works out the analytical solution using integration with an integrating factor.

# Importing matplot to be able to create graphs of solutions, and math for exponential.
import matplotlib.pyplot as plt
import math

# Here I declare arrays, firstly 'step_sizes' which contains the different step sizes, and then also arrayX and arrayY
# in order to store the resulting x and y values.
step_sizes = [1,0.2,0.05]
# Do you really need two types of arrays? Perhaps arrayX and arrayY could already be 2d?
arrayX = [[],[],[]]
arrayY = [[],[],[]]

# EULER'S METHOD: Here is where the program performs Euler's method. Firstly i use y(0) = -3, to store the initial x
# and y values. The relevant step size is then chosen.
for i in range(0,3):
    x = 0
    y = -3
    step_size = step_sizes[i]
    for i in range(0,int(5/step_size) + 1):
        # In this for loop, I append the x and y values to the array, and then I use a mathematical expression on line
        # 24 to apply Euler's method. The value x is then increased by the step size.
        arrayX[i].append(x)
        arrayY[i].append(y)
        y += step_size * (x + y/5)
        x += step_size

# The arrays are then segmented at the relevant points, and added to a larger array.
#cutoffsX = [arrayX[:6],arrayX[6:32],arrayX[32:]]
#cutoffsY = [arrayY[:6],arrayY[6:32],arrayY[32:]]

# ANALYTICAL METHOD: Here is where the program performs the analytical method. Working out for the mathematical
# expression on line 46 can be found in the 'Working.txt'.
# perhaps array above could be called EulerArray and this one AnalyticalArray?
realArrayX = []
realArrayY = []
for i in range(0,3):
    # Same declarations as in Euler's method.
    x = 0
    y = -3
    step_size = step_sizes[i]
    for i in range(0,int(5/step_size) + 1):
        # This is the main mathematical loop. The program plugs in the x value into the expression to get the accurate
        # answer for the value of y. The step size is then incremented.
        realArrayX.append(x)
        realArrayY.append(y)
        y = (-5 * x) - 25 + (22 * math.exp(x/5))
        x += step_size

# Arrays are segmented again.
realCutoffsX = [realArrayX[:6],realArrayX[6:32],realArrayX[32:]]
realCutoffsY = [realArrayY[:6],realArrayY[6:32],realArrayY[32:]]

# This final for loop is then used to create the graphs.
for i in range(0,3):
    # Using the matplotlib library, I first create the parameters for the graph with .plot (plots coordinates), .axis
    # (defines range of axis) and .label (labels the axis). The graphs are then displayed to the user.
    plt.plot(arrayX[i], arrayY[i], 'ro', label="numerical")
    plt.plot(realCutoffsX[i], realCutoffsY[i], '-', label="analytical")
    plt.axis([0,5,-4,10])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Numerical vs Analytical Method")
    plt.legend()
    plt.show()
