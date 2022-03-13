from timeloading import *

# func1:
def func1():
    time.sleep(3)

# func2:
def func2(x):
    time.sleep(x)

# example-1:
# Run the wait function "func1" for 3 seconds with default settings.
exec(timeloading().loading(function="func1"))

# example-2:
# Run the wait function "func2" for 5 seconds and change the message settings.
exec(timeloading().loading(function="func2",args=[5],msg="Loading....",done="ok"))

# example-3:
# The same as the previous example, but with a change in the speed and shape of the animation.
exec(timeloading(animation=["[*  ]","[ * ]","[  *]","[ * ]",],time_w=0.1).loading(function="func2",args=[5],msg="Loading....",done="ok"))

# example-4:
# Example with color
from hexor import * # pip install hexor

p2=hexor(True,"hex")
s0=p2.c("*","#ff0000")
s1=p2.c("*","#760e0e")
s2=p2.c("*","#ff7272")

l=[f"[{s0}{s1}{s2}]",f"[{s1}{s2}{s0}]",f"[{s2}{s0}{s1}]"]
exec(timeloading(animation=l,time_w=0.1).loading(function="func2",args=[5],msg="Loading....",done="ok"))