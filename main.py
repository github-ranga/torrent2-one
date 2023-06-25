import os

os.system('curl -OJ "https://codeload.github.com/novnc/noVNC/zip/refs/tags/v1.4.0"')
os.system('unzip "./noVNC-1.4.0.zip"')

os.system('echo $PATH')
os.system('echo $PWD')

os.system('echo -e "\n123456\n123456\nn\n" | vncpasswd')
os.system('echo -e "#!/bin/sh\nxfce4-terminal" > ~/.vnc/xstartup')

os.system('vncserver -depth 32 -geometry 1200x900 &')
os.system('./noVNC-1.4.0/utils/novnc_proxy --vnc localhost:5901 --listen localhost:7860 &>/dev/null &')

#os.system("python -m http.server 7860")
