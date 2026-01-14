import tkinter as tk
from tkinter import messagebox, filedialog
from pytubefix import YouTube
import os

def download_video():
    # 1. Get URL from the input box
    video_url = url_entry.get()
    
    if not video_url:
        messagebox.showerror("Error", "Please paste a YouTube link first!")
        return

    try:
        # 2. Update status label
        status_label.config(text="Connecting to YouTube...", fg="blue")
        root.update()

        # 3. Create YouTube Object
        yt = YouTube(video_url)
        
        # 4. Get the highest resolution stream (usually 720p/1080p)
        stream = yt.streams.get_highest_resolution()
        
        # 5. Ask user where to save
        save_folder = filedialog.askdirectory()
        if not save_folder:
            status_label.config(text="Download Cancelled", fg="red")
            return

        status_label.config(text=f"Downloading: {yt.title}...", fg="orange")
        root.update()

        # 6. Download the video
        stream.download(output_path=save_folder)

        # 7. Success Message
        status_label.config(text="Download Complete! ✅", fg="green")
        messagebox.showinfo("Success", f"Video saved in:\n{save_folder}")
        
        # Clear the input
        url_entry.delete(0, tk.END)

    except Exception as e:
        status_label.config(text="Error Occurred", fg="red")
        messagebox.showerror("Download Error", f"Something went wrong:\n{str(e)}")

# --- GUI SETUP ---

# 1. Create the Window
root = tk.Tk()
root.title("Kanpur YouTube Downloader")
root.geometry("500x250")
root.resizable(False, False)

# 2. Header
header = tk.Label(root, text="YouTube Video Downloader", font=("Arial", 16, "bold"), fg="#ff0000")
header.pack(pady=10)

# 3. Input Field
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

lbl = tk.Label(input_frame, text="Paste Link:", font=("Arial", 12))
lbl.pack(side=tk.LEFT, padx=5)

url_entry = tk.Entry(input_frame, width=40, font=("Arial", 10))
url_entry.pack(side=tk.LEFT, padx=5)

# 4. Download Button
btn = tk.Button(root, text="Download Video", bg="red", fg="white", font=("Arial", 12, "bold"), command=download_video)
btn.pack(pady=15)

# 5. Status Label
status_label = tk.Label(root, text="Ready", font=("Arial", 10), fg="grey")
status_label.pack(pady=5)

# 6. Footer
footer = tk.Label(root, text="BCA Mini Project", font=("Arial", 8), fg="#ccc")
footer.pack(side=tk.BOTTOM, pady=5)

# Run the App
root.mainloop()