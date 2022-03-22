from tkinter import *
from tkinter import messagebox
import os.path
import datetime


# This Version accepts multiple programs as Input and shows help or info tag
# And writes the logs

root = Tk()
root.title("IMEX Mainframe Deploy Tool")

root.geometry('600x400')
#"root.configure(bg='white')

root.iconbitmap('C:\\IMEX255\\deploy3.ico')

envLst = ["DEV", "SIT", "UAT"]
BackupLst = ["YES", "NO", "BACKUP ONLY"]
t2d_Lst = ["YES", "NO"]
compile_Lst = ["YES", "NO"]
#comp_type_Lst = ["ONLINE", "BATCH"]


def Submit_verify():
    """Accept Input details and verify them and in case of error show on screen.
    """
    all_okay_flag = True
    # envionment = env_click.get()
    print("Inside Verify")
    
    
def reset_all():
    """Accept Input details and verify them and in case of error show on screen.
    """
    print("Inside Reset")
    

def env_selected(event):
    """Accept Input details and verify them and in case of error show on screen.
    """
    envionment = env_click.get()
    print(envionment)

    label_env["text"] =""
    
    #comp_type = comp_type_var.get()
    backup = backup_click.get()
    
    # if comp_type == 'NA':
    #     comp_type_var.set("Choose")
    #     drop_type["state"] = "active"
    
    if envionment == 'DEV':
        backup_click.set("NA")
        drop_backup["state"] = "disabled"
        
        t2d_var.set("Choose")
        drop_t2d["state"] = "active"

        compile_var.set("Choose")
        drop_compile["state"] = "active"
        
    if envionment == 'SIT' or envionment == 'UAT':
        if backup == 'NA':
            backup_click.set("Choose")
            drop_backup["state"] = "active"
    
        t2d_var.set("NA")
        drop_t2d["state"] = "disabled"

        compile_var.set("NA")
        drop_compile["state"] = "disabled"



env_click = StringVar()
env_click.set("Choose")
sel_env_label = Label(root, text="\nEnvionment: \n")
sel_env_label.place(x=5, y=0)
drop_env = OptionMenu(root, env_click, *envLst, command=env_selected)
drop_env.configure(font=('Futura',11,'bold'),fg='green')
drop_env.grid(column=1, row=0, sticky="w")

blank3_label = Label(root, text="------------------- ")
blank3_label.grid(column=0, row=1, sticky="e")

Query_input_label = Label(root, text="Program Name : ")
Query_input_label.grid(column=0, row=2, sticky="e")
InputProgramName = Entry(root, width=20)
InputProgramName.focus()
InputProgramName.grid(column=1, row=2, sticky="w")

# comp_type_input_label = Label(root, text="Component Type : ")
# comp_type_input_label.grid(column=0, row=3, sticky="e")
# comp_type_var = StringVar()
# comp_type_var.set("NA")
# drop_type = OptionMenu(root, comp_type_var, *comp_type_Lst)
# drop_type["state"] = "disabled"
# drop_type.grid(column=1, row=3, sticky="w")

sel_backup_label = Label(root, text="Back Up : ")
sel_backup_label.grid(column=0, row=4, sticky="e")
backup_click = StringVar()
backup_click.set("NA")
drop_backup = OptionMenu(root, backup_click, *BackupLst)
drop_backup["state"] = "disabled"
drop_backup.grid(column=1, row=4, sticky="w")

blank1_label = Label(root, text="------------------- ")
blank1_label.grid(column=0, row=5, sticky="e")

t2d_input_label = Label(root, text="Copy Prog Temp to Dev : ")
t2d_input_label.grid(column=0, row=6, sticky="e")
t2d_var = StringVar()
t2d_var.set("NA")
drop_t2d = OptionMenu(root, t2d_var, *t2d_Lst)
drop_t2d["state"] = "disabled"
drop_t2d.grid(column=1, row=6, sticky="w")

compile_input_label = Label(root, text="Compile in Dev : ")
compile_input_label.grid(column=0, row=7, sticky="e")
compile_var = StringVar()
compile_var.set("NA")
drop_compile = OptionMenu(root, compile_var, *compile_Lst)
drop_compile["state"] = "disabled"
drop_compile.grid(column=1, row=7, sticky="w")

blank2_label = Label(root, text="\n-------------------\n ")
blank2_label.grid(column=0, row=8, sticky="e")


reset_Button = Button(root, text="RESET", command=lambda: reset_all())
reset_Button.grid(column=0, row=9)


Verify_Button = Button(root, text="VERIFY", command=lambda: Submit_verify(),bg="white", fg="blue",font = ('Sans','10','bold'))
Verify_Button.grid(column=1, row=9)


#label_result0 = Label(root, text=" >> Ready to Deploy  ",relief=RAISED)
label_result0 = Label(root, text="",fg="Blue")
label_result0.grid(column=2, row=8, sticky="w")

label_env = Label(root, text="",fg="Red")
label_env.grid(column=2, row=0, sticky="w")
label_prog_in = Label(root, text="")
label_prog_in.grid(column=2, row=2, sticky="w")
# label_comp_type = Label(root, text="")
# label_comp_type.grid(column=2, row=3, sticky="w")
label_backup = Label(root, text="")
label_backup.grid(column=2, row=4, sticky="w")
label_t2d = Label(root, text="")
label_t2d.grid(column=2, row=6, sticky="w")
label_compile = Label(root, text="")
label_compile.grid(column=2, row=7, sticky="w")

root.mainloop()