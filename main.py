from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('PythonGuides')
window.minsize(width=400,height=300)
window.config(bg='Light blue')

def calculate_bmi():
    kg = int(weight_e.get())
    m = int(height_e.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    bmi_index(bmi)

def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Obesity')
    else:
        messagebox.showerror('bmi-pythonguides', 'something went wrong!')
def rest_button():
    weight_e.delete(0,'end')
    height_e.delete(0,'end')
var=IntVar()

label1 = Label(window,text="Choose Gander",)
label1.config(bg="grey")
label1.grid(row=1,column=1)

frame = Frame(window)
frame.grid(row=1,column=2,padx=70)
maler = Radiobutton(frame,text="MALE",variable=var,value=1)
maler.pack(side=LEFT)
maler.config(bg="grey")
fermaler = Radiobutton(frame,text="FERMALE",variable=var,value=2)
fermaler.pack(side=RIGHT)
fermaler.config(bg="grey")

weight_l = Label(window,text="Your Weight")
weight_l.config(bg="grey")
weight_l.grid(row=2,column=1)

weight_e = Entry(window,bg="white",fg="black")
weight_e.grid(row=2,column=2,pady=10)

height_l = Label(window,text="Your Height")
height_l.config(bg="grey")
height_l.grid(row=3,column=1)

height_e = Entry(window,bg="white",fg="black")
height_e.grid(row=3,column=2,pady=10)

frame2 = Frame(window)
frame2.grid(row=5,columnspan=3,pady=50)

cal_bt = Button(frame2,text="CALCULATE",command=calculate_bmi)
cal_bt.pack(side=LEFT)

res_bt = Button(frame2,text="DELETE",command=rest_button)
res_bt.pack(side=RIGHT)

exit_bt = Button(frame2,text="EXİT",command=lambda:window.destroy())
exit_bt.pack(side=RIGHT)

window.mainloop()