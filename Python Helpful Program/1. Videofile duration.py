from moviepy.editor import VideoFileClip

clip = VideoFileClip("video.mp4")
duration = clip.duration
print(f"Duration of the video: {duration} seconds")
