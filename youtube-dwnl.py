from pytube import YouTube

#Url of the video to be downloaded

# url = "https://"
#lets get the URl from the user

url = input("Enter the Youtube Video Link: ").streams.get_highest_resolution().download

#create a YouTube object and set the video URL

video = YouTube(url)

#Get the Video with the highest resolution and bitrate

video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
    

# download the video with the path

#video_stream.download()