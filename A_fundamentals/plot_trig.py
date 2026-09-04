# NB: Students *NOT* expected to do it like this
#  - But doing it like this allows easy repetition
#  - See "fundamentals_8.ipynb"
#
# This module plots user-specified trig functions

# Import all the definitions from the numpy and plotting libraries
import numpy as np
import matplotlib.pyplot as plt

# Define the plotting function
def makeplot(funcname):

    # Define the x array
    x=np.arange(0, 2*np.pi, 0.01)

    # Check if the user entered the sin, cos, or tan function
    if funcname=='sin':
        plt.plot(x, np.sin(x))
    elif funcname=='cos':
        plt.plot(x, np.cos(x))
    elif funcname=='tan':
        plt.plot(x, np.tan(x))
    else:
        print("Unrecognized function: "+str(funcname))

