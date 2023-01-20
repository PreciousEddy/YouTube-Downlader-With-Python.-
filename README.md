  ![Youtube](https://github.com/PreciousEddy/YouTube-Downlader-With-Python.-/blob/main/Images/youtube-downloader-with-text.svg)

# YouTube Video Downloader in Python -- Using  Pytube()

## What is Youtube?
  *A YouTube video is a digital video that is uploaded to the video-sharing platform YouTube. These videos can be created by individuals or organizations and can be watched by anyone with an internet connection. They can include a wide variety of content such as music videos, movie trailers, vlogs, educational videos, and more. Users can also comment on, like, and share videos on YouTube.*

## What is downloader?
  *A downloader is a software program or online service that allows users to download files from the internet to their local computer or device. This can include downloading software, music, videos, images, and other types of files. Some downloaders are specifically designed for certain types of files, such as video downloaders for downloading videos from video sharing sites like YouTube, while others are more general-purpose and can be used to download files from a variety of sources. Some downloaders also include features such as the ability to pause, resume, and schedule downloads.*

  ## Steps for making YouTube Video Downloader in Python-using Pytube()

  ### Here are the steps for creating a Youtube video downloader using python. 

  - Install the `pytube` library:
      > pip install pytube
  - Import the library in your Python script:  ` from pytube import youtube`
  - Use the YouTube class to initialize a YouTube object with the URL of the video you want to download:  `yt = YouTube(video_url)`
  - Use the 'streams' property to get a list of all the available streams for the video: `streams = yt.stream` in other words, you can get the highest quality of the video `video_stream = video.streams.get_highest_resolution()`
  - Download the video `V
