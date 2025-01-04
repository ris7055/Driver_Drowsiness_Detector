import tkinter as tk
import customtkinter as ctk

import torch
import numpy as np
import random
import cv2
from PIL import Image, ImageTk
import vlc

# Initialize GUI
app = tk.Tk()
app.geometry("600x600")
app.title("Driver Drowsiness Detector")
ctk.set_appearance_mode("dark")

#initial height=400, width=600
vidFrame = tk.Frame(height=400, width=600)
vidFrame.pack()
blank_image = ImageTk.PhotoImage(Image.new('RGB', (600, 400), (0, 0, 0)))
vid = ctk.CTkLabel(master=vidFrame, image=blank_image, text="")
vid.pack()

# Initialize webcams():
#vid = ctk.CTkLabel(master=vidFrame)
#blank_image = ImageTk.PhotoImage(Image.new('RGB', (600, 400), (0, 0, 0)))
#vid = ctk.CTkLabel(master=vidFrame, image=blank_image, text="")


# Counter and Reset Button
counter = 0
counterLabel = ctk.CTkLabel(
    master=app,
    text=counter,
    height=40,
    width=120,
    font=("Arial", 20),
    text_color="white",
    fg_color="teal"
)
counterLabel.pack(pady=10)

def reset_counter():
    global counter
    counter = 0
    counterLabel.configure(text=counter)

resetButton = ctk.CTkButton(
    master=app,
    text="Reset Counter",
    command=reset_counter,
    height=40,
    width=120,
    font=("Arial", 20),
    text_color="white",
    fg_color="teal"
)
resetButton.pack(pady=10)

model = torch.hub.load('../yolov5', 'custom', path='../yolov5/runs/train/exp16/weights/last.pt', source='local', force_reload=True)
cap = cv2.VideoCapture(1)
def detect():
    global counter
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(frame)
    img = np.squeeze(results.render())

    print(results.xywh[0])
    if len(results.xywh[0]) > 0:
        dconf = results.xywh[0][0][4]
        dclass = results.xywh[0][0][5]

        if dconf.item() > 0.85 and dclass.item() == 16.0:
            filechoice = random.choice([1,2,3])
            p = vlc.MediaPlayer(f"file:///{filechoice}.wav")
            p.play()
            counter += 1

    imgarr = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(imgarr)
    vid.imgtk = imgtk
    vid.configure(image=imgtk)
    vid.after(10, detect)
    counterLabel.configure(text=counter)

detect()
app.mainloop()