from pytube import YouTube

url = input("Enter url: ") 

youtube_video = YouTube(url)
print("TITRE: ", youtube_video.title)
print("NB VUES: ", youtube_video.views)

stream = youtube_video.streams.get_by_itag(251)
#stream = youtube_video.streams.get_highest_resolution()
print("Téléchargement...")
stream.download()
print("OK")
#for video in youtube_video.streams:
 #   print(video)
