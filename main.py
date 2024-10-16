import os
import tkinter as tk
from tkinter import filedialog

def get_path():
    root = tk.Tk()
    root.withdraw() 
    return filedialog.askdirectory(title="Pick folder with images")

def get_pics(folder_path, extensions):
    return [
        f for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f)) and os.path.splitext(f.lower())[1] in extensions
    ]

def rename_pics(folder_path, images):
    for idx, image in enumerate(images, start=1):
        old_path = os.path.join(folder_path, image)
        new_name = f"{idx}_{image}"
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed'{image}' to '{new_name}'")

def rename_pic_date():
    folder_path = get_path()
    if not folder_path:
        print("No folder selected , end")
        return

    extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff']
    images = get_pics(folder_path, extensions)
    images.sort(key=lambda x: os.path.getctime(os.path.join(folder_path, x)))
    rename_pics(folder_path, images)
    print("Renaming done .")

if __name__ == "__main__":
    rename_pic_date()
