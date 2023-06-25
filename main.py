import os

os.system('curl -OJ "https://codeload.github.com/novnc/noVNC/zip/refs/tags/v1.4.0"')
os.system('unzip "./noVNC-1.4.0.zip"')


os.system("python -m http.server 7860")


#from fastapi import FastAPI

#app = FastAPI()


#@app.get("/")
#def read_root():
#    return {"Hello": "World!"}