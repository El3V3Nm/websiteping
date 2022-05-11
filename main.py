import subprocess
import pyfiglet
text = pyfiglet.figlet_format("King") #ye agar coller full ho sakta hai to wo kr dena is text ko
print(text)
print("Enter An Ip or website name")
i = input()
subprocess.call("ping "+ i ,shell=True)
