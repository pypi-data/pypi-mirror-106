import subprocess
import logging
from os import path

def check_for_imagemagick():
    try:
        subprocess.run('convert', shell=True, check=True)
    except subprocess.CalledProcessError as err:
        logging.error(str(err))
        raise ValueError('ImageMagic:convert not found') from err

def convert_gif(gif_filename):
    filename, _ = path.splitext(gif_filename)
    try:
        subprocess.run(f"convert {filename}[0] {filename}.png", shell=True, check=True)
    except subprocess.CalledProcessError as err:
        logging.error(f"Error: convert {filename}[0] {filename}.png")
        logging.error(str(err))
        raise ValueError(f"Error during: convert {filename}[0] {filename}.png") from err
    return f"{filename}.png"
