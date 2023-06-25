FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt




RUN useradd -m -u 1000 user

USER user

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH


WORKDIR $HOME/app

# Copy the current directory contents into the container at $HOME/app setting the owner to the user
COPY --chown=user . $HOME/app

CMD [ "python" , "main.py" ]