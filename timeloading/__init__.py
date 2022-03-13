#!/usr/bin/env python
# coding:utf-8
#code by:YasserBDJ96
#email:yasser.bdj96@gmail.com

#START{
from multiprocessing import Process
import time

#start timeloading class:
class timeloading:
    #__init__
    def __init__(self,animation="⢿⣻⣽⣾⣷⣯⣟⡿",time_w=0.1):
        self.animation=animation
        self.time_w=time_w

    def loading_bar(animation,exit_flag,msg,time_w):
        i=0
        while not exit_flag:
            print("\r"+animation[i%len(animation)]+" "+msg,end="")
            time.sleep(time_w)
            i+=1
        
    def loading(self,function,args="",msg="Working on tasks...",done="Done!"):
        if type(self.animation)==str:
            x="'"
        else:
            x=""
        if args!="":
            args=f",args={args}"
        x=f"""
exit_flag=False
x1=Process(target=timeloading.loading_bar,args=({x}{self.animation}{x},exit_flag,"{msg}",{self.time_w}))
x1.start()
x2=Process(target={function}{args})
x2.start()
x2.join()
x1.terminate()
#x2.terminate()
print("{done}")
exit_flag=True"""
        return x
#}END.