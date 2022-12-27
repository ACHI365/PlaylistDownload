import yt_dlp
import os
import shutil
from pytube import Playlist
import tkinter as tk
from tkinter import filedialog


def youtube2mp3(video_url, outdir):
    video_info = yt_dlp.YoutubeDL().extract_info(url=video_url, download=False)
    filename = f"{video_info['title']}.mp3".replace("/", "").replace("\\", "").replace("|", "").replace("\"", "")

    new_path = outdir + f"\\{filename}"

    if os.path.exists(new_path):
        print(f"File with path: {new_path} already exists, thus skipping downloading")
        return

    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    shutil.move(filename, new_path)

    print("Download complete... {}".format(filename))


def getPlayListURLs(playlist, outdir):
    yt = Playlist(playlist)

    urls = []

    for url in yt:
        youtube2mp3(url, outdir)

    return urls


if __name__ == '__main__':
    print("Please insert the path where you want to save your data (C:\\Users\\Public\\Music is default)")
    root = tk.Tk()
    root.withdraw()

    directory = filedialog.askdirectory()

    if not os.path.isdir(directory):
        directory = "C:\\Users\\Public\\Music"
    getPlayListURLs(input("insert playList: "), directory)
