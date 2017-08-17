import requests
import subprocess
import time
from instapush import Instapush, App
app = App(appid='5995ec43a4c48a06217b23c6', secret='9c3d758baf6cae6108515820a57ce837')

#subprocess.call("ngrok start -config=ngrok.yml main",shell=False)
print("wait...")
time.sleep(5)
print("ready")
lista =[]
commandstring = ""
r=requests.get('http://localhost:4040/api/tunnels')
data=r.json()
for i in range(2):	
	proto = data["tunnels"][i]["proto"]
	if proto == "https":
		public_url = str(data["tunnels"][i]["public_url"])

print public_url

lista.append("0x08") 	#0
lista.append("0x0008")	#1
lista.append("")		#2
lista.append("02")		#3
lista.append("01")		#4
lista.append("06")		#5
lista.append("03")		#6
lista.append("03")		#7
lista.append("aa")		#8
lista.append("fe")		#9
lista.append("")		#10
lista.append("16")		#11
lista.append("aa")		#12
lista.append("fe")		#13
lista.append("10")		#14
lista.append("00")		#15

def leadingZero(v):
	if len(v) == 2 :
		return v
	elif len(v) == 1:
		return "0"+v
	else:
		return "error"

url = public_url
if url.startswith("https://"):
	lista.append("03")
	public_url2 = url.lstrip("https://")

for char in public_url2:
	letter = hex(ord(char)).lstrip("0x")
	lista.append(letter);

lista[2] = leadingZero(hex(len(lista)-3).lstrip("0x"))
lista[10] = leadingZero(hex(len(lista)-11).lstrip("0x"))

if len(lista) == 0:
	commandstring = "error"
elif len(lista) <= 34:
	for i in range(len(lista), 34):
		lista.append("00")

	for i in range(len(lista)):
		commandstring = commandstring + str(lista[i]) + " "

command1 = "sudo hciconfig hci0 up"
command2 = "sudo hciconfig hci0 leadv 3"
command3 = "sudo hcitool -i hci0 cmd " + commandstring


print(command1)
print(command2)
print(command3)

app.notify(event_name='ProjectKunayWow', trackers={ 'url': public_url,'trama' : commandstring})

subprocess.call(command1,shell=True)
subprocess.call(command2,shell=True)
subprocess.call(command3,shell=True)