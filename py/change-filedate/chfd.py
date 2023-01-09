import filedate
from pathlib import Path
import os
from glob import glob
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

top = Tk()

def change_file_date(folder,patternty):
    files = []
    start_dir = folder
    pattern = "*" + patternty
    print(start_dir)
    print(pattern)

    # Durchlaufe den Ordner und alle Unterordner
    for dir,_,_ in os.walk(start_dir):
        files.extend(glob(os.path.join(dir,pattern)))

    # Lese alle Datumseinträge
    dates = []
    with open('dates.txt') as date_file:
        for line in date_file:
            dates.append(line)

    # Änderungsdatum aller gesammelten Dateien ändern
    for file in files:
        didx = random.randint(0, 24) # Wähle ein zufälliges Datum
        a = file
        a_file = filedate.File(a)
        a_file.set(
            created = dates[didx],
            modified = dates[didx]
        )
        after = filedate.File(a)
        print(after.get())
    messagebox.showinfo("Msg", "finished!")

FLbl = Label(top, text="Folder")
FLbl.pack(side = LEFT)
FEntry = Entry(top, bd = 5)
FEntry.pack(side = LEFT)
PLbl = Label(top, text="Pattern")
PLbl.pack(side = RIGHT)
PEntry = Entry(top, bd = 5)
PEntry.pack(side = RIGHT)
BRun = Button(top, text="Run", command=lambda: change_file_date(FEntry.get(),PEntry.get()))
BRun.pack(side = RIGHT)
top.mainloop()