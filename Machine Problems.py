import sys
from tkinter import *

def value1():
    q = float(num1.get())
    d=float (5/9 * (q-32)); #Celcius
    label1=Label(root,text = "The value entered is Celsius is: %.1f" %d). pack(side =BOTTOM)
    return
def value2():
    q = float(num1.get())
    d = int(q); #Fahrenheit
    f = int(d)* 9/5 =32);
    label1=Label(root,text = "The value entered is Celsius is: %.1f" %d). pack(side =BOTTOM)
    return
def value3():
    q = float(num1.get())
    d = int (q + 273); #Kelvin
    f = int(9.0/5.0);
    t = int(f * d)
    label1=Label(root,text = "The value entered is Celsius is: %.1f" %d). pack(side =BOTTOM)
    return

root = Tk()
root.title("Temperature Converter")
root.geometry('450x450+400+150')
frame = Frame(root)
frame.pack

num1=StringVar()
radbtn = StringVar
radbtn.set(None)

frame1 = Frame(root)
frame1.pack(side=TOP)

label2=Label(frame1,text= 'Enter Temperature for Conversion',fg='Black',relief =RAISED)
label2.pack(side=TOP)

label2=Label(frame1,text= '\n\n')
label2.pack(side=TOP)

txtDisplay=Entry(frame1,textvariable=num1, bd=30,insertwidth=1,font=12,justify='center')
txtDisplay.pack(side=TOP)
label2=Label(frame1, text = 'n\n\')
label2.pack(side=TOP)

radio1= Radiobutton(frame1, text="Celsius", variable=radbtn, value="Celsius", command=value1).pack(side=BOTTOM)
radio1= Radiobutton(frame1, text="Fahrenheit", variable=radbtn, value="Fahrenheit", command=value2).pack(side=BOTTOM)
radio1 = Radiobutton(frame1, text="Kelvin", variable=radbtn, value="Kelvin", command=value3).pack(side=BOTTOM)

button1 = Button(frame1,padx=16, pady=16, bd=8, text="Today's Temperature is", fg="black", font=48, command=value1)
button1.pack(side=BOTTOM)

root.mainloop()