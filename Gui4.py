import tkinter as tk
import time
 
class BackGroundFrame(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
 
        self.frames = {}
        for klass in [StartPage, ManualPage]:
            self.frames[klass.__name__] = klass(container, self)
            self.frames[klass.__name__].grid(row = 0, column=0,sticky="nsew")
        self.frames["StartPage"].tkraise()
 
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        instruction = tk.Label(self,text="Welcome to Dispensing GUI")
        instruction.grid(row=0 , column =0,columnspan=3, sticky = "W")
 
        self.action1 = tk.Button(self, text="Retrieve Solution Name",command=lambda:self.push_retrieve_solutions())
        self.action1.grid(row = 0, column = 4,columnspan = 2,sticky= "W")
 
        tk.Label(self,text = "        ").grid(row =1, column = 0,sticky = "W")
        tk.Label(self,text = "Solutions to Pumps Allocations").grid(row =2, column = 0,columnspan=10,sticky = "W")
 
        self.typeofsolution = []
        for i in [0, 2, 4, 6]:
            self.create_typeofsolution({"width":12}, {"row":3, "column":i, "sticky":"W"})
 
        self.submitManual = tk.Button(self,text="Manual",command=lambda:controller.frames["ManualPage"].tkraise())
        self.submitManual.grid(row =8,rowspan=5, column = 0, columnspan = 4,sticky = "W")
 
        self.submitAutomatic = tk.Button(self,text="Automatic")
        self.submitAutomatic.grid(row =8,rowspan=5, column = 1, columnspan = 2,sticky = "W")
 
    def create_typeofsolution(self, entry_keys, grid_keys):
        typeofsolution = tk.Entry(self, **entry_keys)
        typeofsolution.grid(**grid_keys)
        self.typeofsolution.append(typeofsolution)
 
        i = len(self.typeofsolution)
        j = (i - 1) * 2
        tk.Label(self,text = "Pump {0}".format(i)).grid(row =4, column = j,columnspan=2,sticky = "W")
        tk.Label(self,text = "    ").grid(row =3, column = j + 1,sticky = "W")
 
    def retrieve_solutions(self):
        names = []
        for i in range(3):
            names.append(self.typeofsolution[i].get())
 
        return names
 
    def push_retrieve_solutions(self):
        print(self.retrieve_solutions())
 
class ManualPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
 
        self.manualtitle = tk.Label(self, text="Welcome to Manual Dispensing")
        self.manualtitle.grid(row=0 , column =0, columnspan=6, sticky="W")
 
        tk.Label(self,text = "Solution Name    ").grid(row =1, column = 0,sticky="W")
        tk.Label(self,text = "Time Input(s)     ").grid(row =1, column = 2,sticky="w")
        tk.Label(self,text = "Dispense").grid(row =1, column = 5,sticky="W")
 
        self.text = []
        for i in range(4):
            irow = (i + 1) * 2
            self.text.append(tk.Text(self, width =10, height = 1))
            self.text[-1].grid(row = irow, column = 0,columnspan= 10,sticky= "W")
            tk.Label(self,text = "        ").grid(row = irow + 1, column = 0,sticky="W")
 
        self.submitlol = tk.Button(self,text="Back to Main Menu",command=lambda:controller.frames["StartPage"].tkraise())
        self.submitlol.grid(row =10,rowspan=5, column = 0, columnspan = 4,sticky = "W")
 
        self.timepump = []
        for i in range(4):
            irow = (i + 1) * 2
            self.timepump.append(tk.Entry(self,width = 10))
            self.timepump[-1].grid(row = irow, column = 1, columnspan=10, sticky="w")
 
        self.submit = []
        for i in range(4):
            irow = (i + 1) * 2
            self.submit.append(tk.Button(self, text="Dispense {0}".format(i)))
            self.submit[-1].grid(row = irow, column = 3, columnspan = 10, sticky="w")
 
        names = controller.frames["StartPage"].retrieve_solutions()
        for i in range(3):
            self.text[i].delete(0.0)
            self.text[i].insert(0.0, names[i])
 
app = BackGroundFrame()
app.mainloop()