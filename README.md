# High Priority Register for Windows (HPRW)
Fast register process for high priority on windows, using contextual menu, very fast, right click and enjoy !!

What for is it?

Basictly add (pinned) to the REG in windows the process that you need set priority in High forever. Good for games and other task
![image](https://user-images.githubusercontent.com/14153649/203855395-a16e0703-eb23-42a2-b508-c6427244261e.png)

How do it?
In summary, generate a shortcut in your context menu, in the which you can simply do right click on the .exe and set in high process forever
![image](https://user-images.githubusercontent.com/14153649/203855792-c677c4e7-1d59-47c2-af86-2237b183b9df.png)

But really it generte and execeute the .reg file with the neccesary data to be registered in Windows.
Like this

```
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\Spider-Man.exe]

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\Spider-Man.exe\PerfOptions]
"CpuPriorityClass"=dword:00000003
```


Requeriments:
- Windows
- Python 3x

Steps:
1) Execute RegistrarMenuContextual.bat
2) Search a .exe, righ click and  click on Set_High_Priority
3) Enjoy
