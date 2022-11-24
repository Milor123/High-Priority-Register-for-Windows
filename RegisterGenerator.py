# Author: Mateo Bohorquez
# Description: Fast register process of games or .exe files in REG and force to keep it in high priority on CPU
# Requeriments: Windows. (Tested in windows 10)
# How works? With the .bat files, you will create a register .reg file, the which in firts place, create a new object
# over you contextual menu, and allow to you, do right click on .exe file, then set it as high priority, creating it a new
# reg file with the data for keep it registered as high priority process.

import os
import sys
import pathlib

class RegIster:
    hook_cmd = str
    process_name_exe = str
    reg_text = str
    proceess_priority = 3 #(See windows documentation, 3 = High)
    reg_contexualmenu_text = str
    current_path = str(pathlib.Path(__file__).parent.resolve())+ "\\"


    def __init__(self):

        
        self.reg_text = """\
Windows Registry Editor Version 5.00\n
[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\{}]\n
[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\{}\PerfOptions]
"CpuPriorityClass"=dword:0000000{}\
"""
        # Only if have args pass through contextual menu (Windows)
        try:

            if str(sys.argv[1]) == "--registerMenu":
                self.make_reg_contextual_menu()
            else:
                self.process_name_exe = str(sys.argv[1].split("\\")[-1])
                self.push_reg_data(self.process_name_exe, self.proceess_priority)
                self.make_reg("PatchProcess.reg", self.reg_text)
                self.register_reg("PatchProcess.reg")
        except:
            pass

        
    
    # Save the reg data according to name process and priority int 0-3
    def push_reg_data(self, process_name, process_priority=3):
        self.reg_text = self.reg_text.format(process_name, process_name, process_priority)
    
    # reg_name expect str name.extension = name.reg and reg_text for the .reg
    def make_reg(self, reg_name, reg_text):
        with open (self.current_path + reg_name, "w") as reg_creator:
            reg_creator.write(reg_text)

    # reg_name expect str name.extension = name.reg
    def register_reg (self, reg_name):
        # Add reg file name as text command to be executed
        command_text = ('cmd /c "{}"').format(self.current_path + reg_name)
        os.system(command_text)

    def make_reg_contextual_menu(self):

        # Get the current folder path
        # It must be \file.bat using the "\"
        bat_file_to_register = "\Start_HighPriorityScript.bat"
        # Append the current folder path with the name .bat file
        file_path = "{}{}".format(self.current_path, bat_file_to_register)
        # convert the path in doble backslash, for example C:\\example\\script.py, its neccesary for add the register file on windows
        file_path_for_register = file_path.replace("\\","\\\\")
        self.reg_contexualmenu_text = """\
Windows Registry Editor Version 5.00
[HKEY_CLASSES_ROOT\*\shell\Set_High_Priority\command]
@="\\"{}\\" \\"%1\\""
""".format(file_path_for_register)

        self.make_reg("ConfigurarMenuContextual.reg", self.reg_contexualmenu_text)
        self.register_reg("ConfigurarMenuContextual.reg")


    
init = RegIster()
#init.register_reg()
#init.make_reg_contextual_menu()