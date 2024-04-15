from tkinter import *
def bmi():
    h=height.get()
    w=weight.get()
    bmi= w/h**2

    label2.config(text=bmi)

    if bmi>0:
        if (bmi<18.5):
            label3.config(text="You are underweight.")
        elif (bmi<=24.9):
            label3.config(text="You are normal.")
        elif (bmi<=29.9):
            label3.config(text="You are overweight.")
        elif (bmi<=34.9):
            label3.config(text="You are obese.")
        elif (bmi<=39.9):
            label3.config(text="You are severely obese.")
        else:
            label3.config(text="You are morbidly obese.")
    else:
        label3.config(text="Enter valid data.")
root=Tk()
root.title("BMI Calculator")
root.geometry("500x400")
frame1= Frame(root,bg="#E0BD67",border=1)
frame1.place(x=0,y=0,height=50,width=500)
heading= Label(frame1,text="BMI Calculator" , font="Courier 20 bold",pady=10,bg="#E0BD67")
heading.pack()

lf1= LabelFrame(root,text="Height(m)",font="Helvetica" )
lf1.place(x=10,y=60)
height=DoubleVar()
h_entry=Entry(lf1,textvariable=height).pack(padx=20,pady=5)

lf2= LabelFrame(root,text="Weight(kg)",font="Helvetica" )
lf2.place(x=250,y=60)
weight=DoubleVar()
w_entry=Entry(lf2,textvariable=weight).pack(padx=20,pady=5)

button1=Button(root,text="Get Your BMI",command=bmi)
button1.place(x=175,y=150)

label1= Label(root,text="BMI : ",font="Helvetica 14" )
label1.place(x=30,y=200)
label2= Label(root,text=" ",font="Helvetica 14" )
label2.place(x=90,y=200)
label3= Label(root,text=" ",font="Helvetica 14" )
label3.place(x=30,y=240)


root.mainloop()