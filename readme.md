# script Pytube en un contenedor
Para ello necesitaremos tener una carpeta llamda _envYoutube_ y otra llamada _app_ en la que guardaremos nuestros scripts

## _app_ 
tendremos dentro un script que se llamará _myscript.py_ y que contendrá la siguiente forma:
### _myscript.py_
~~~
from pytube import YouTube

#link = input("Enter the link: ")
yt = YouTube("https://www.youtube.com/watch?v=aFqTjk3kcEw&ab_channel=Garajedeideas")

#Title of video
print("Title: ",yt.title)
#Number of views of video
print("Number of views: ",yt.views)
#Length of the video
print("Length of video: ",yt.length,"seconds")
#Description of video
print("Description: ",yt.description)
#Rating
print("Ratings: ",yt.rating)


yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
~~~
## Ficheros
Tambien tendremos que crear el _docker-compose.yml_, _Dockerfile_ y _requirements.txt_

### _docker-compose.yml_
Es como debe crearse el contenedor.
~~~
version: '3.3'
services:
    python:
        container_name: pruebascript
        volumes:
           - ./app:/usr/src/app
        image: youtubeimagen:chromecast
        tty: true
        stdin_open: true
        working_dir: /usr/src/app
        command: ["python","myscript.py"]
~~~

### _Dockerfile_
es como queremos que funcione el contenedor.
~~~
FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /usr/src/app

CMD ["python","myscript.py"]
~~~

### _requirements.txt_
Son las librerias que necesitaremos.
~~~
pytube==12.1.2
PyChromecast
~~~
