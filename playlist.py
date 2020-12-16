import pytube

video_list = []

print("Enter the playlist's URL")
url = input("")

playlist = pytube.Playlist(url)

for url in playlist:
    v = pytube.YouTube(url)
    stream = v.streams.get_by_itag(22)
    print(f"Downloading video...")
    stream.download()
    print("Done")
