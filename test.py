import os
from tkinter import *
root=Tk()
root.geometry("600x500")
var=StringVar()
var_entry=Entry(root,textvariable=var)
var_entry.grid(row=0,column=0)
def solve():
    filename=var.get()+".csv"
    file=open(filename,"w+")
    file.writelines("hh,jj,jj,jj\n")
    file.close()
    file=open(filename,'r+')
    f
    print(type(file.readlines()[0]))


b=Button(text="submit",command=solve)
b.grid(row=0,column=0)

root.mainloop()
