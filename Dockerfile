FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apt update
RUN apt install -y curl unzip xfce4-terminal tigervnc-standalone-server xfce4
RUN apt install -y dbus-x11 fish
RUN apt install -y stow
#RUN apt install docker docker-engine docker.io
RUN systemctl --user dbus

RUN useradd -m -u 1000 user
 
USER user

ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the current directory contents into the container at $HOME/app setting the owner to the user
COPY --chown=user . $HOME/app
RUN python -m http.server 7860
CMD [ "python" , "main.py" ]