from tkinter import *

def get_data(event=NONE):
    print("string",strVar.get())
    print("number",intVar.get())
    print("double",dblVar.get())
    print("boolean",boolVar.get())

def bind_button(event=NONE):
    if boolVar.get():
        getDataButton.unbind("<Button-1>")
    else:
        getDataButton.bind("<Button-1>", get_data)

root = Tk()

strVar = StringVar()
intVar = IntVar()
dblVar = DoubleVar()
boolVar = BooleanVar()

strVar.set("Enter String")
intVar.set("enter number")
dblVar.set("enter double")
boolVar.set(True)

strEntry = Entry(root, textvariable=strVar)
strEntry.pack(side=LEFT)

intEntry = Entry(root, textvariable=intVar)
intEntry.pack(side=LEFT)

dblEntry = Entry(root, textvariable=dblVar)
dblEntry.pack(side=LEFT)

thecheckbutton = Checkbutton(root, text = "switch", variable=boolVar)
thecheckbutton.bind("<Button-1>", bind_button)
thecheckbutton.pack(side=LEFT)

getDataButton = Button(root, text="get data")
getDataButton.bind("<Button-1>", get_data)
getDataButton.pack(side= LEFT)

root.mainloop()