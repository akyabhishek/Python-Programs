# importing the module
from pytube import YouTube

yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0').streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()