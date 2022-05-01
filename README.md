<h1>timeloading</h1>

<p>Animated loading bar. This package is a loading bar that appears when a specific function is run an animation and text. This bar is stoped to run after the function has finished working. You can control the shape and the waiting message, even the animation and its colors.</p>

[![Python package](https://github.com/yasserbdj96/timeloading/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/yasserbdj96/timeloading/actions/workflows/python-app.yml) [![Docker image](https://github.com/yasserbdj96/timeloading/actions/workflows/docker-image.yml/badge.svg)](https://github.com/yasserbdj96/timeloading/actions/workflows/docker-image.yml) [![CodeFactor](https://www.codefactor.io/repository/github/yasserbdj96/timeloading/badge)](https://www.codefactor.io/repository/github/yasserbdj96/timeloading)

<h2>Languages:</h2>
* python3

<h2>Supported Distributions:</h2>

| Distribution | Version Check     | Python Test Version | Supported | Status  | Everything works |
| :----------: | :---------------: | :-----------------: | :-------: | :----:  | :--------------: |
| Ubuntu       | 20.04.3           | 3.6, 3.7, 3.8, 3.9  | Yes       | Working | Yes              |
| Windwos      | 11.6.4            | 3.6, 3.7, 3.8, 3.9  | Yes       | Working | Yes              |
| MacOS        | 10.0.20348        | 3.6, 3.7, 3.8, 3.9  | Yes       | Working | Yes              |

<h2>Installation:</h2>

```
pip install timeloading
```

<h2>Usage:</h2>

```python
from timeloading import *

# Default usage:
exec(timeloading().loading(function))

# In-depth use:
exec(timeloading(animation,time_w).loading(function,args,msg,done))

"""
Help:
# animation : ascii animation text list. ex: ["⢿","⣻","⣽","⣾","⣷","⣯","⣟","⡿"] OR "⢿⣻⣽⣾⣷⣯⣟⡿"
# time_w : Transition time between animations.
# function : The function name must be a string.
# args : Function variables. ex: (var_name,) OR [var_name]
# msg : Waiting message text.
# done : Message after completion.
"""
```

<h2>Examples:</h2>

```python
from timeloading import *

# func1:
def func1():
    time.sleep(3)

# func2:
def func2(x):
    time.sleep(x)

# example-1:
# Run the wait function "func1" for 3 seconds with default settings.
exec(timeloading().loading(function="func1")) # You can run the code directly without using exec() and write the code that returns directly from the function.

# example-2:
# Run the wait function "func2" for 5 seconds and change the message settings.
exec(timeloading().loading(function="func2",args=[5],msg="Loading....",done="ok"))

# example-3:
# The same as the previous example, but with a change in the speed and shape of the animation.
exec(timeloading(animation=["[*  ]","[ * ]","[  *]","[ * ]",],time_w=0.1).loading(function="func2",args=[5],msg="Loading....",done="ok"))

# example-4:
# Example with color
from hexor import * # pip install hexor

p1=hexor(True,"hex")
s0=p1.c("*","#ff0000")
s1=p1.c("*","#760e0e")
s2=p1.c("*","#ff7272")

l=[f"[{s0}{s1}{s2}]",f"[{s1}{s2}{s0}]",f"[{s2}{s0}{s1}]"]
exec(timeloading(animation=l,time_w=0.1).loading(function="func2",args=[5],msg="Loading....",done="ok"))
```

<h2>Screenshot:</h2>

<div align="center">
    <a href="https://raw.githubusercontent.com/yasserbdj96/timeloading/main/screenshot/screenshot_1.png">
        <img alt="yasserbdj96" height="100" src="https://raw.githubusercontent.com/yasserbdj96/timeloading/main/screenshot/screenshot_1.png">
    </a>
</div>

<h2>Changelog History:</h2>

```
## 0.0.1 [13-03-2022]
- First public release.
```

<h1></h1> 

<div align="center">
    <a href="http://yasserbdj96.github.io/">Go to this link to get more information</a>
    <br>
    <a href="https://github.com/yasserbdj96/imbot" align="center">
        <img align="center"  alt="" src="https://visitor-badge.laobi.icu/badge?page_id=yasserbdj96.timeloading">
    </a>
</div>
