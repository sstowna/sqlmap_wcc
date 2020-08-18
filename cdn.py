# cdn.py Source Code
# Written by Jhin Scripter

import itertools, threading, time, sys, os, winreg

pappdatap = os.getenv("APPDATA")

if os.path.isdir(r"{}\sqlmap_wcc".format(pappdatap)):
	print("You aleadry have sqlmap_wcc installed, open 'remove.bat' to remove it.")
	exit()

fp = input("Ex: D:\\MyFiles\\slmap-v8-smd-0x9-b1 \nSqlmap path: ")
os.system("cls")
pp = input("(py, python, python3, python2)\nPython prefix: ")
os.system("cls")

finished = False

def loadinganimation():
	for c in itertools.cycle(['|', '/', '-', '\\']):
		if finished:
			break
		sys.stdout.write("\rWorking on " + c)
		sys.stdout.flush()
		time.sleep(0.3)
	print("Path > {}\nPython Prefix: {}".format(fp, pp))

threading.Thread(target=loadinganimation).start()

os.mkdir(r"{}\sqlmap_wcc".format(pappdatap))

time.sleep(0.5) # To prevent errors

prompt_cnfg_file = open(r"{}\sqlmap_wcc\sqlmap_cnfg.cmd".format(pappdatap), "w")
prompt_cnfg_file.write(f"doskey sqlmap={pp} {fp}\\sqlmap.py $*\ncls")
prompt_cnfg_file.close()

time.sleep(1.5) # To prevent errors

os.system("cls")

try:
	winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Command Processor")
	regkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Command Processor", 0, winreg.KEY_WRITE)
	winreg.SetValueEx(regkey, "Autorun", 0, winreg.REG_EXPAND_SZ, r"{}\sqlmap_wcc\sqlmap_cnfg.cmd".format(pappdatap))
except:
	print("Erro no registro!")

finished = True
time.sleep(1)
input("Finished!\n\n>")