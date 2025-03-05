import subprocess
import tkinter as tk
from tkinter import filedialog, ttk
import threading

def download_video_yt_dlp(url, output_path, audio_only, resolution, progress_bar, progress_label, status_label):
    """Downloads a video or audio using yt-dlp, with progress."""
    try:
        command = ["yt-dlp", "-P", output_path]

        if audio_only:
            command.extend(["-x", "--audio-format", "mp3"])
        elif resolution and resolution != "highest" and resolution != "lowest":
            command.extend(["-f", f"best[height<={resolution}]"])
        elif resolution == "lowest":
            command.extend(["-f", "worst"])
        else: #highest
            command.extend(["-f", "best"])

        command.extend(["--progress-template", "%(progress.percentage)s"]) #Progress template
        command.append(url)

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                try:
                    percentage = float(output.strip())
                    progress_bar["value"] = percentage
                    progress_label.config(text=f"{percentage:.2f}%")
                except ValueError:
                    pass #Ignore non-percentage output

        if process.returncode == 0:
            status_label.config(text="Download complete.")
        else:
            status_label.config(text=f"Download failed (Code {process.returncode}).")

    except FileNotFoundError:
        status_label.config(text="Error: yt-dlp not found. Please install it.")
    except Exception as e:
        status_label.config(text=f"An error occurred: {e}")

def start_download():
    """Starts yt-dlp download in a separate thread."""
    url = url_entry.get()
    resolution = resolution_combobox.get()
    audio_only = audio_var.get()
    output_directory = filedialog.askdirectory()

    if output_directory:
        threading.Thread(target=download_video_yt_dlp, args=(url, output_directory, audio_only, resolution, progress_bar, progress_label, status_label)).start()
    else:
        status_label.config(text="Please select an output directory.")

# GUI setup
root = tk.Tk()
root.title("YouTube Downloader (yt-dlp)")

url_label = tk.Label(root, text="YouTube URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

resolution_label = tk.Label(root, text="Resolution:")
resolution_label.pack()
resolution_options = ["highest", "lowest", "1080p", "720p", "480p", "360p", "240p", "144p"]
resolution_combobox = ttk.Combobox(root, values=resolution_options, state="readonly")
resolution_combobox.current(0)
resolution_combobox.pack()

audio_var = tk.BooleanVar()
audio_checkbutton = tk.Checkbutton(root, text="Audio Only", variable=audio_var)
audio_checkbutton.pack()

download_button = tk.Button(root, text="Download", command=start_download)
download_button.pack()

progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack()

progress_label = tk.Label(root, text="0.00%")
progress_label.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()