from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Fever Report")
root.geometry("600x600")
Label_question1=Label(root,text="Do you have any Headaches or Sore Throats?")
Label_question1.pack()

question1_radiobtn1=StringVar(value="0")
question1_r1=Radiobutton(root,text="Yes",variable=question1_radiobtn1,value="Yes")
question1_r1.pack()

question1_r2=Radiobutton(root,text="No",variable=question1_radiobtn1,value="No")
question1_r2.pack()

Label_question2=Label(root,text="Do you have high body temperature?")
Label_question2.pack()

question2_radiobtn1=StringVar(value="0")
question2_r1=Radiobutton(root,text="Yes",variable=question2_radiobtn1,value="Yes")
question2_r1.pack()

question2_r2=Radiobutton(root,text="No",variable=question2_radiobtn1,value="No")
question2_r2.pack()

Label_question3=Label(root,text="Do you have eye redness?")
Label_question3.pack()

question3_radiobtn1=StringVar(value="0")
question3_r1=Radiobutton(root,text="Yes",variable=question3_radiobtn1,value="Yes")
question3_r1.pack()

question3_r2=Radiobutton(root,text="No",variable=question3_radiobtn1,value="No")
question3_r2.pack()

def GenerateFeverReport():
    score=0
    if question1_radiobtn1.get()=="Yes":
        score=score+20
        print(score)
    if question2_radiobtn1.get()=="Yes":
        score=score+20
        print(score)
    if question3_radiobtn1.get()=="Yes":
        score=score+20
        print(score)
    
    if score<=20:
        messagebox.showinfo("Report!","You don't need to visit a doctor")
    elif score>20 and score<=40:
        messagebox.showinfo("Report!","You might perhaps need to visit the doctor")
    else:
        messagebox.showinfo("Report!","You are strongly advised to visit the doctor")







btn1=Button(root,text="Click Me to Generate Report",bg="black",fg="white",command=GenerateFeverReport)
btn1.pack()
root.mainloop()