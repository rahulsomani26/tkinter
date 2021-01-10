import tkinter as tk
from database import PhoneBook
# from PIL import Image, ImageTk

p = PhoneBook()


def addData():
    # print(type(nameValue.get()))
    p.addData(nameValue.get(), addressValue.get(), mobileValue.get())


def viewData():
    p.getRecord()


root = tk.Tk()
root.geometry('1000x1000')
root.configure(bg="#833737")
root.title("Telephone Diary")
try:
    root.iconbitmap("myicon.ico")
except Exception as e:
    print(e)
# root['bg'] = 'red'
nameValue = tk.StringVar()
addressValue = tk.StringVar()
mobileValue = tk.StringVar()


labelName = tk.Label(root, text="Enter Name", width=20)
labelName.grid(column=0, row=0)
labelAddress = tk.Label(root, text="Address", width=20, background="#833737")
labelAddress.grid(column=0, row=1)
labelMobile = tk.Label(root, text="Mobile", width=20, background="#833737")
labelMobile.grid(column=0, row=2)


entryName = tk.Entry(root, textvariable=nameValue)
entryAddress = tk.Entry(root, textvariable=addressValue)
entryMobile = tk.Entry(root, textvariable=mobileValue)


entryName.grid(column=1, row=0)
entryAddress.grid(column=1, row=1)
entryMobile.grid(column=1, row=2)


# cta buttons

addButton = tk.Button(text="Add", command=addData)
viewButton = tk.Button(text="view", command=viewData)
addButton.grid(column=0, row=4)
viewButton.grid(column=1, row=4)


root.mainloop()
