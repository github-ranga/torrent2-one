import os

os.system('curl -OJ "https://codeload.github.com/novnc/noVNC/zip/refs/tags/v1.4.0" > /dev/null')
os.system('unzip "./noVNC-1.4.0.zip" > /dev/null')
os.system('git clone https://github.com/novnc/websockify ./noVNC-1.4.0/utils/websockify')

os.system('chmod +x /home/user/app/xstartup')



#os.system('echo "------noVNC------"')
#os.system('./noVNC-1.4.0/utils/novnc_proxy --vnc localhost:5901 --listen localhost:7860 &')

os.system('echo "------websockify------"')
os.system('./noVNC-1.4.0/utils/websockify/run --token-plugin=TokenFile --token-source=/home/user/app/tok 0.0.0.0:7860 --web=/home/user/app ')


#os.system('echo "------vncserver------"')
#os.system('vncserver -passwd /home/user/app/vncpass -xstartup /home/user/app/xstartup -depth 32 -geometry 1200x900 ')



#os.system('echo "------hppt.server------"')
#os.system("python -m http.server 7860")
