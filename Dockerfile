FROM python:3.9
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt




RUN apt update
RUN apt install -y curl unzip xfce4-terminal tigervnc-standalone-server xfce4
RUN apt install -y dbus-x11 fish
RUN apt install -y stow
RUN apt install -y dbus-user-session
RUN apt install -y uidmap iptables
RUN apt install -y kmod

RUN curl -o install.sh -fsSL https://get.docker.com
RUN sh install.sh
RUN apt install -y docker-ce-rootless-extras

RUN apt install -y apt-utils firefox-esr


#RUN echo 'kernel.unprivileged_userns_clone=1' >> /etc/sysctl.conf
#RUN echo 'net.ipv4.ping_group_range = 0 2147483647' >> /etc/sysctl.d/99-rootless.conf
#RUN echo 'net.ipv4.ip_unprivileged_port_start=0' >> /etc/sysctl.d/99-rootless.conf

#RUN sysctl --system

#RUN curl -OJ https://storage.googleapis.com/sysbox-releases/v0.6.2/sysbox-ce/sysbox-ce_0.6.2-0.linux_amd64.deb
#RUN apt install -y jq
#RUN apt install -y ./sysbox-ce_0.6.2-0.linux_amd64.deb


RUN useradd -m -u 1000 user
 
USER user

ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the current directory contents into the container at $HOME/app setting the owner to the user
COPY --chown=user . $HOME/app
RUN curl -OJ "https://codeload.github.com/novnc/noVNC/zip/refs/tags/v1.4.0" > /dev/null
RUN unzip "./noVNC-1.4.0.zip" > /dev/null
RUN git clone https://github.com/novnc/websockify ./noVNC-1.4.0/utils/websockify
RUN chmod +x /home/user/app/xstartup

#RUN python -m http.server 7860
CMD [ "python" , "main.py" ]