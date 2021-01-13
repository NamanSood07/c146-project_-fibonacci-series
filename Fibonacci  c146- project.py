# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:10:53 2021

@author: HIMALINAMAN
"""
from tkinter import*
root=Tk()
root .title("Fibonacci")
root.geometry("300x300")


label_num=Label(root, text="Enter a number", )

num = Entry(root)
label_series =Label(root, text="Fibonacci Series :" )
result=Label(root)

def fibonacci():
    number=num.get()
    first_no=0
    second_no=1
    sum=0
  
    counter=1
    while(counter <= int(number)):
        label_series["text"]+= str(sum) +" "
        counter= counter+1
        first_no= second_no
        second_no=sum
        sum=first_no + second_no
       
        result["text"]=str(sum)
btn=Button(root, text="Show Fibonacci Series", command=fibonacci)

num.pack()
label_num.pack()

label_series.pack()

result.pack()
btn.pack()


root.mainloop()
