import os
import ast
myfile = open("logs.txt","w+")

emp_name=["mohit","rohit","hohit","kohit"]
emp_id=[1,2,3,4]
emp_age=[1,2,3,4]

#myfile.write()
dic1={"emp_name":emp_name,"emp_id":emp_id,"emp_age":emp_age}

print(dic1)

#list1=["emp_name","emp_id","emp_age"]
#list2=[emp_name,emp_id,emp_age]

#dic=zip(list1,list2)
#print(dic)
#dic=dict(dic)

#print(dic)
#print(list[0])


myfile.write(str(dic1))

print(dic1.get("emp_name",0)[0])

myfile.close()
myfile = open("logs.txt","r")


dic=myfile.read()
dic_convert=ast.literal_eval(dic)
print(dic_convert)
print(dic_convert.get("emp_name",0)[0])


'''
filter_none
brightness_5
dictionary = {'geek': 1, 'supergeek': True, 4: 'geeky'} 
  
try: 
    geeky_file = open('geekyfile.txt', 'wt') 
    geeky_file.write(str(dictionary)) 
    geeky_file.close() 
  
except: 
    print("Unable to write to file")
'''
'''
def fun():
if(var1.get()==1):
print('Doing Diploma')
if(var2.get()==1):
print('Doing B.Tech')
if(var3.get()==1):
print('Studying M.Tech')
if(var4.get()==1):
print('Earning Ph.D')

from tkinter import *
win = Tk( className="CheckBox Demo")
win.geometry("350x200")
var1 = IntVar()
Checkbutton(win, text='Diploma', variable=var1,activebackground="red",command=fun).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(win, text='B.TECH', variable=var2,command=fun).grid(row=1, sticky=W)
var3 = IntVar()
#var3.set(True)
Checkbutton(win, text='M.TECH', variable=var3,command=fun).grid(row=2, sticky=W)
var4 = IntVar()
Checkbutton(win, text='Ph.D', variable=var4,bg="yellow",command=fun).grid(row=3, column=3,sticky=W)
mainloop()
'''
