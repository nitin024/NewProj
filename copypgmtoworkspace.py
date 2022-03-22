import tkinter as tk
import os.path
import datetime
import shutil 
import errno 

window = tk.Tk()
window.title("Copy Program to Workspace")

frm_entry = tk.Frame(master=window)
ent_input = tk.Entry(master=frm_entry, width=20)
lbl_temp = tk.Label(master=frm_entry, text="Input Program Name")

ent_input.grid(row=0, column=1, sticky="w")
lbl_temp.grid(row=0, column=0, sticky="e")

dest = "U:\\IDz\\Projects\\Workspace\\Test\\Cobol\\"
srcfile = "X:\\Felix\\Test\\Cobol\\"


def my_main():
    """Accept program name and copy the program to Workspace and 
    put that file in lbl_result.
    """
    input_program_valid = False
    input_program = ent_input.get()
    print(f'\nInput Program Name: {input_program}\n')
    
    if input_program:
        input_program_valid = True
    else:
        lbl_result["text"] = "Error : Invalid Program Name. \nInput Again."
    program = str. rstrip(input_program)
    program = program.upper()
    if input_program_valid: 
        srcpgm = srcfile + program + '.CBL'
        shutil.copy2(srcpgm,dest)

        print(f"\n Program " + program + " Copied")
        lbl_result["text"] = "\n " + program + " Copied at --> U:\\IDz\\Projects\\Workspace\\Test\\Cobol\\ \n"
    
btn_start = tk.Button(
    master=window,
    text="CLICK TO COPY",
    command=my_main  # Executable para
)
lbl_result = tk.Label(master=window, text="Workspace Library -> U:\\IDz\\Projects\\Workspace\\Test\\Cobol \n")

frm_entry.grid(row=0, column=0, padx=10, pady=5)
btn_start.grid(row=0, column=1, padx=5, pady=10)
lbl_result.grid(row=1, column=0, padx=10, pady=5)


window.mainloop()
