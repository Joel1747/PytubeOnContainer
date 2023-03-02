from pytube import YouTube
from pytube import Playlist

p = Playlist('')

for video in p.videos:
    video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
print('funciona')

#en caso de querer descargar un video solo,comentar lo de la playlist y descomentar lo de a continuación

#link = input("Enter the link: ")
#yt = YouTube("https://www.youtube.com/watch?v=aFqTjk3kcEw&ab_channel=Garajedeideas")


#Title of video
#print("Title: ",yt.title)
#Number of views of video
#print("Number of views: ",yt.views)
#Length of the video
#print("Length of video: ",yt.length,"seconds")
#Description of video
#print("Description: ",yt.description)
#Rating
#print("Ratings: ",yt.rating)


#yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

