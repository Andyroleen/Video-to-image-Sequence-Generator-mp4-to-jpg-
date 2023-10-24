Video to Image Sequence Converter

Introduction:
The Video to Image Sequence Converter is a Python-based application that allows you to convert a video file into a sequence of images in PNG format. This tool is helpful if you want to extract individual frames from a video for various purposes, such as image processing, computer vision, or creating a video thumbnail.
to run the tool with python, open command prompt in same directory and run following command: 
python mp42jpg.py
This command will run graphical interface of tool.
if you want to package tool as an executable file run command prompt in same directory where 'mp42jpg.py' is located and run following command:
pip install pyinstaller
(If you have installed pyinstaller, skip this code and run following command only)
pyinstaller --onefile mp42jpg.py
This will package the tool as an executable file in "\Tool Directory\dist\mp42jpg.exe"
Features:
Easy-to-use graphical user interface (GUI).
Converts MP4 videos into a sequence of PNG images.
Displays real-time progress of the conversion.
Option to choose the input video and output directory.
Fast and efficient video frame extraction.

Supported Video Formats:
This tool primarily supports MP4 video files. You can use it to convert MP4 videos into a sequence of PNG images. If you have a different video format, consider converting it to MP4 before using this tool. There are various video conversion tools available that can help you convert videos to the MP4 format.

How to Use:
Select an MP4 Video:

Click the "Select MP4 Video" button or manually type the path to your MP4 video in the entry field. This video will be used as the source for frame extraction.
Choose an Output Directory:

Click the "Select Output Directory" button or enter the path of the directory where you want to save the extracted PNG images.
Start the Conversion:

Click the "Convert Video to Images" button to start the conversion process. The GUI will display the progress as the tool processes each frame of the video.
Conversion Progress:

As the frames are processed, the "Progress" label will display the percentage of completion. You can monitor the progress in real-time.
Completion Notification:

Once the conversion is complete, a notification window will appear, confirming that the video to image sequence conversion has finished successfully.
Find Your PNG Images:

The converted PNG images will be saved in the directory you specified. You can now access and use these images as needed.
Note:
The tool may work with other video formats if you first convert them to the MP4 format.
Ensure that you have Python installed on your system, as well as the required Python libraries (moviepy and Pillow).
