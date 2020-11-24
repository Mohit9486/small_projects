import pytube

url = input("paste link here: ")

youtube = pytube.YouTube(url)

title =  youtube.title
print(title)


print("downloading started")
youtube.streams.get_highest_resolution().download()
print("download copleted")