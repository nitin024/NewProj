from tkinter import *

# from PIL import ImageTk,Image
root = Tk()
root.title("Learn new stuff")
#root.iconbitmap("C:\\IMEX255\\nk.ico")
root.iconbitmap('C:\\IMEX255\\pythonicon.ico')


def bind():
    region_input = clicked.get()
    input_program = inputprogram.get()
    program = str. rstrip(input_program)
    label_result["text"] = "Finally : " + region_input + program

region = ["SIT", "UAT"]

clicked = StringVar()
clicked.set("SIT")

drop = OptionMenu(root, clicked, *region)
drop.pack()

input_label = Label(root, text="Input Prog name: ")
input_label.pack(anchor=W)
inputprogram = Entry(root, width=20)
inputprogram.pack()



MyButton = Button(root, text="click Me", command=lambda: bind())
MyButton.pack()

label_result = Label(root, text=" Yo Yo")
label_result.pack()

root.mainloop()
