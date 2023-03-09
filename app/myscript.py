from pytube import YouTube

#link = input("Enter the link: ")
yt = YouTube("https://www.youtube.com/watch?v=12K6qvc-x4c")

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