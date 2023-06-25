import os

#os.system('curl -OJ "https://codeload.github.com/novnc/noVNC/zip/refs/tags/v1.4.0"')
#os.system('unzip "./noVNC-1.4.0.zip" &> /dev/null')

os.system('echo $PATH')
os.system('echo $PWD')
os.system('sudo apt install -y curl')
import os
import platform

os.system('echo -e "123456\n123456\nn\n" | vncpasswd')
os.system('echo -e "#!/bin/sh\nxfce4-terminal" > ~/.vnc/xstartup')

os.system('vncserver -depth 32 -geometry 1200x900 &')
os.system('noVNC-1.4.0/utils/novnc_proxy --vnc localhost:5901 --listen localhost:7860 &>/dev/null &')

#os.system("python -m http.server 7860")


#from fastapi import FastAPI

#app = FastAPI()


#@app.get("/")
#def read_root():
#    return {"Hello": "World!"}