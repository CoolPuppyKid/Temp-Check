import os
from tkinter import *
from tkinter import ttk

def Get_User():
    return os.getlogin()   

def Get_Local_Temp():
    local_temp_path = os.getenv("TEMP")
    return local_temp_path

def Check_Extensions_Formatted(directory, file_extension):
    matching_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(file_extension):
                matching_files.append(os.path.join(root, file))

    if len(matching_files) == 0:
        formatted = "No Results But Just Because There Are No Files In Temp That Are EXE`s\n That Does Not Mean Your Safe I Recommend Using A\n Antivirus This Tool Is Just A Second Opinion"
    else:
        formatted = "Results: \n" + "\n".join(matching_files)
    
    return formatted


def Check_Extensions(directory, file_extension):
    matching_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(file_extension):
                matching_files.append(os.path.join(root, file))

    return matching_files

def clear_exes() -> None:
    exe_files = Check_Extensions(Get_Local_Temp(), ".exe")
    for path in exe_files:
        os.remove(path)
    Check_Extensions_Formatted()
    cleanDirButton.pack_forget(Get_Local_Temp(), ".exe")

root = Tk()
root.geometry("800x600")
root.title("Temp Check")

cleanDirButton = Button(root, text="Clear Temp EXEs (Not Recommended)", command=clear_exes)

cleanDirButton.pack_forget()

resultstr = StringVar()
resultstr.set("No Results Yet Press Check Temp")

def checkTemp():
    resultstr.set(Check_Extensions_Formatted(Get_Local_Temp(), ".exe"))
    exe_files = Check_Extensions(Get_Local_Temp(), ".exe")
    
    if len(exe_files) != 0:
        cleanDirButton.pack(padx=1, pady=1)

label = Label(root, text="Welcome To Temp Cleaner This Program\n Checks The Temp Folder For .EXE Files, Those Files In The Temp Folder May Be A Sign Of Malware\n And This Program Will Serve As An Early Warning")

label.pack(padx=20, pady=20)

CheckBtn = Button(root, text="Check Temp", command=checkTemp)
CheckBtn.pack(padx=20, pady=15)

results = Label(root, textvariable=resultstr)
results.pack(padx=1, pady=1)

root.mainloop()