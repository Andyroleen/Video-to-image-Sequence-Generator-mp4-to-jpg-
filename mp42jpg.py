import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from moviepy.editor import VideoFileClip
from PIL import Image
import threading

def browse_video():
    file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    video_path_entry.delete(0, tk.END)
    video_path_entry.insert(0, file_path)

def browse_directory():
    directory = filedialog.askdirectory()
    output_path_entry.delete(0, tk.END)
    output_path_entry.insert(0, directory)

def convert_video_to_images():
    video_path = video_path_entry.get()
    output_path = output_path_entry.get()

    try:
        video = VideoFileClip(video_path)
        total_frames = int(video.fps * video.duration)
        video.close()

        def update_progress(frame_number):
            progress = int((frame_number / total_frames) * 100)
            progress_label.config(text=f"Progress: {progress}%")
            app.update_idletasks()

        video = VideoFileClip(video_path)
        for i, frame in enumerate(video.iter_frames(fps=int(video.fps), dtype="uint8")):
            image = Image.fromarray(frame)
            image.save(f"{output_path}/frame_{i:04d}.png")
            update_progress(i)

        video.close()
        progress_label.config(text="Progress: 100%")
        messagebox.showinfo("Conversion Complete", "Video to image sequence conversion is complete.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

app = tk.Tk()
app.title("Video to Image Sequence Converter")

frame = ttk.Frame(app)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)

video_label = ttk.Label(frame, text="Select MP4 Video:")
video_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

video_path_entry = ttk.Entry(frame)
video_path_entry.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

video_browse_button = ttk.Button(frame, text="Browse", command=browse_video)
video_browse_button.grid(row=0, column=2, padx=5, pady=5, sticky=tk.E)

output_label = ttk.Label(frame, text="Select Output Directory:")
output_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

output_path_entry = ttk.Entry(frame)
output_path_entry.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

output_browse_button = ttk.Button(frame, text="Browse", command=browse_directory)
output_browse_button.grid(row=1, column=2, padx=5, pady=5, sticky=tk.E)

convert_button = ttk.Button(frame, text="Convert Video to Images", command=lambda: threading.Thread(target=convert_video_to_images).start())
convert_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky=(tk.W, tk.E))

# Create a progress label to display the percentage
progress_label = ttk.Label(frame, text="Progress: 0%")
progress_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5, sticky=(tk.W, tk.E))

if __name__ == "__main__":
    app.mainloop()
