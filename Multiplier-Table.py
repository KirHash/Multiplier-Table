from tkinter import *
import tkinter.messagebox

root = Tk()

space = " "
root.title(80 * space + "Multiplication Table")
root.geometry("642x470+440+100") #670, 500

enterTable = StringVar()
#==================================Frame====================================================================
baseFrame = Frame(root, bd=14, bg="black", relief=RIDGE)
baseFrame.grid()

leftFrame = Frame(baseFrame, bd=7, width=350, height=540, relief=RIDGE)
leftFrame.grid(row=0, column=0)

rightFrame = Frame(baseFrame, bd=7, width=350, height=540, relief=RIDGE)
rightFrame.grid(row=0, column=1)
#=================================Function===================================================================
def MultTable():
    txtResult.delete(1.0,END)
    m = (enterTable .get())
    enterTable.set("")

    if (m.isdigit()):
        m = int(m)
        for x in range(1, 11):
            txtResult.insert(END, (x), '\t'," x ",'\t', (m) , '\t', " = ", '\t', (x*m))
            txtResult.insert(END, '\n\n')
        return True
    else:
        tkinter.messagebox.showwarning("Error", "Invalid data, Numbers only")
        enterTable.set("")
        return False
    
def iQuit():
    iQuit = tkinter.messagebox.askyesno("Multiplication Table", "Confirm if you want to exit")
    if iQuit > 0:
        root.destroy()
    else:
        txtResult.delete(1.0,END)
        enterTable.set("")

def iReset():
    iQuit = tkinter.messagebox.askyesno("Multiplication Table", "Confirm if you want to reset")
    if iQuit > 0:
        txtResult.delete(1.0,END)
        enterTable.set("")
#============================Entry and Function=================================================================
titleLabel = Label(rightFrame, text="Multiplication Table", font=("arial",20,"bold"))
titleLabel.grid(row=0, column=0)

txtResult = Text(rightFrame, font=("arial",10,"bold"), bd=10, width=30, height=23)
txtResult.grid(row=1, column=0)

title = Label(leftFrame, text="Enter a number", font=("arial",20,"bold"))
title.grid(row=0, column=0)

txtInput = Entry(leftFrame, textvariable=enterTable, bd=10, font=("arial",20,"bold"), justify="center")
txtInput.grid(row=1, column=0)
#===================================Button=======================================================================
btnMultiple = Button(leftFrame, text="Multiply", bd=10, font=("arial",20,"bold"), width=16, command=MultTable)
btnMultiple.grid(row=2, column=0, pady=20)

btnReset = Button(leftFrame, text="Reset", bd=10, font=("arial",20,"bold"), width=16, command=iReset)
btnReset.grid(row=3, column=0, pady=20)

btnQuit = Button(leftFrame, text="Quit", bd=10, font=("arial",20,"bold"), width=16, command=iQuit)
btnQuit.grid(row=4, column=0, pady=20)
#================================================================================================================
root.mainloop()
