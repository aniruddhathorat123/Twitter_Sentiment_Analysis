from tkinter import *

def addition():
    n1 = num1.get()
    n2 = num2.get()
    n3 = int(n1) + int(n2)
    print(n3)
    res.insert(0,n3)

root = Tk()

root.title("Addition")
root.geometry("300x300")

lb1 = Label(root , text = "Number 1:")
lbl2 = Label(root, text = "Number 2:")
lbl3 = Label(root, text = "Result:")

bt1 = Button(root, text = "ADD", bg = "red", fg = "white", command = addition)

num1 = Entry(root)
num2 = Entry(root)
res = Entry(root)


lb1.grid(row = 0)
lbl2.grid(row = 1)
num1.grid(row = 0, column = 1)
num2.grid(row = 1, column = 1)
bt1.grid(row = 2, column = 1)
lbl3.grid(row = 4, column = 1)
res.grid(row = 4, column = 3)

root.mainloop()