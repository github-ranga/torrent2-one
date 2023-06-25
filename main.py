import os

os.system('curl -OJ "https://codeload.github.com/novnc/noVNC/zip/refs/tags/v1.4.0" > /dev/null')
os.system('unzip "./noVNC-1.4.0.zip" > /dev/null')
os.system('git clone https://github.com/novnc/websockify ./noVNC-1.4.0/utils/websockify')
os.chdir('/home/user/app')

os.system('echo $PATH')
os.system('echo $PWD')

#os.system('echo -e "123456" > vncpass')
#os.system('echo -e "#!/bin/sh\nxfce4-terminal" > xstartup')
os.system('chmod +x ./xstartup')



#os.system('echo "------noVNC------"')
#os.system('./noVNC-1.4.0/utils/novnc_proxy --vnc localhost:5901 --listen localhost:7860 &')

os.system('echo "------websockify------"')
#os.system('echo -e "8080:localhost:8080" > tok')
os.system('./noVNC-1.4.0/utils/websockify/run --token-plugin=TokenFile --token-source=./tok 0.0.0.0:7860 --web=./ -D')


os.system('echo "------vncserver------"')
os.system('vncserver -passwd ./vncpass -xstartup ./xstartup -depth 32 -geometry 1200x900 ')



#os.system('echo "------hppt.server------"')
#os.system("python -m http.server 7860")
