from pytube import YouTube
from tkinter import *
from tkinter import filedialog, messagebox
import threading


def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        file_path = filedialog.askdirectory()
        if file_path:
            stream.download(output_path=file_path)
            messagebox.showinfo("Download complete", "Video downloaded successfully!")
        else:
            messagebox.showwarning("Download cancelled", "Please choose a folder to save the video.")
    except Exception as e:
        messagebox.showerror("Error", "Invalid link")

def download_audio(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        file_path = filedialog.askdirectory()
        if file_path:
            stream.download(output_path=file_path)
            messagebox.showinfo("Download complete", "Audio downloaded successfully!")
        else:
            messagebox.showwarning("Download cancelled", "Please choose a folder to save the audio.")
    except Exception as e:
        messagebox.showerror("Error", "Invalid link")

def clear():
    entry_url.delete(0, END)

def exit_app():
    root.destroy()

def start_video_download():
    url = entry_url.get().strip()
    if not url:
        messagebox.showwarning("Empty field", "Please enter a valid YouTube video URL.")
        return
    threading.Thread(target=download_video, args=(url,)).start()

def start_audio_download():
    url = entry_url.get().strip()
    if not url:
        messagebox.showwarning("Empty field", "Please enter a valid YouTube video URL.")
        return
    threading.Thread(target=download_audio, args=(url,)).start()

root = Tk()
root.title("YouTube Video Downloader")
root.geometry("700x550")
root.iconphoto(True, PhotoImage(file="images/downloading.png"))

header = Label(root, text="YouTube Video Downloader", font='Ariel')
header.pack()

label_url = Label(root, text="Enter the YouTube Video URL")
label_url.pack()

entry_url = Entry(root, width=50)
entry_url.pack()

frame_buttons = Frame(root)
frame_buttons.pack()

button_download = Button(frame_buttons, text="Download Video", command=start_video_download)
button_download.pack(side=LEFT, padx=5)

button_audio = Button(frame_buttons, text="Download Audio", command=start_audio_download)
button_audio.pack(side=LEFT, padx=5)

button_clear = Button(frame_buttons, text="Clear", command=clear)
button_clear.pack(side=LEFT, padx=5)

button_exit = Button(root, text="Exit", command=exit_app)
button_exit.pack(pady=10)

root.mainloop()
