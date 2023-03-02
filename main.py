from pytube import YouTube
from pytube import Playlist

p = Playlist('https://www.youtube.com/watch?v=LKQc7deraKo&list=PLhlzPAwSE2kIExse-BctOdM2XnrJTGEo7')

for video in p.videos:
    video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
print('funciona')




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

