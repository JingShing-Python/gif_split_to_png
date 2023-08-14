from PIL import Image, ImageSequence
import os

def split_gif_to_frames(input_gif, output_folder):
    try:
        gif = Image.open(input_gif)

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        frames = [frame.copy() for frame in ImageSequence.Iterator(gif)]
        for idx, frame in enumerate(frames):
            output_filename = f"{output_folder}/frame_{idx:03d}.png"
            frame.save(output_filename)

        print("Successfully split and saved each frame as individual PNG files.")
    except Exception as e:
        print("An error occurred:", str(e))

input_gif = 'input.gif'
output_folder = 'output'
split_gif_to_frames(input_gif, output_folder)
