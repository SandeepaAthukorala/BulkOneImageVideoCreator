import os
from moviepy.editor import ImageClip, AudioFileClip

def create_video(image_path, audio_path, output_path):
    # Load the image
    image_clip = ImageClip(image_path)

    # Set the fps for the image clip
    fps = 60
    image_clip = image_clip.set_fps(fps)

    # Load the audio
    audio_clip = AudioFileClip(audio_path)

    # Set the duration of the video: audio duration
    video_duration = audio_clip.duration
    image_clip = image_clip.set_duration(video_duration)

    # Start the audio 0.5 seconds into the video
    # audio_clip = audio_clip.set_start(0.5)

    # Set the audio to the image clip with delay
    video_clip = image_clip.set_audio(audio_clip)

    # Write the result to a file
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', fps=fps)

def process_folder(folder_path):
    # Lists to store jpeg and mp3 files
    jpeg_files = []
    mp3_files = []

    # Scan the folder for jpeg and mp3 files
    for file_name in os.listdir(folder_path):
        ext = os.path.splitext(file_name)[1].lower()
        if ext == '.jpeg' or ext == '.jpg':
            jpeg_files.append(os.path.join(folder_path, file_name))
        elif ext == '.mp3':
            mp3_files.append(os.path.join(folder_path, file_name))

    # Process each pair based on their order in the list
    for i in range(min(len(jpeg_files), len(mp3_files))):
        image_path = jpeg_files[i]
        audio_path = mp3_files[i]
        output_name = os.path.splitext(os.path.basename(audio_path))[0] + '.mp4'
        output_path = os.path.join(folder_path, output_name)

        # Create the video file
        create_video(image_path, audio_path, output_path)
        print(f"Created video: {output_path}")

def process_main_folder(main_folder_path):
    # Walk through the main folder and all its subfolders
    for root, dirs, files in os.walk(main_folder_path):
        # Check if there are any mp3 files in the current folder
        if any(file.lower().endswith('.mp3') for file in files):
            print(f"Processing folder: {root}")
            process_folder(root)

# Specify the main folder containing the subfolders
main_folder_path = 'D:\\AI Songs Out\\New Music\\Short'
process_main_folder(main_folder_path)
