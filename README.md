## Driver Drowsiness Detection
Driver drowsiness detection is a crucial safety technology designed to reduce accidents caused by drivers falling asleep at the wheel. 
This project aims to develop a real-time drowsiness detection system using YOLOv5, a state-of-the-art computer vision model. 
The system will analyze live video streams to identify signs of drowsiness and create awareness for driver through an voice alert system, ensuring enhanced road safety

### Motivation

Driver drowsiness is a major cause of road accidents, leading to injuries, fatalities, and economic losses. Traditional safety measures focus on reducing accident impact rather than preventing them. 
With advancements in computer vision and deep learning, YOLOv5 offers an efficient solution for real-time drowsiness detection due to its accuracy and speed. 
This project aims to leverage YOLOv5 to build a real-time monitoring system that detects drowsiness from live video streams and issues timely alerts, enhancing road safety and reducing accident risks.


### Built with:

[torch](https://pytorch.org/) & [torchvision](https://pypi.org/project/torchvision/) : These libraries are essential for training and running the YOLOv5 model. PyTorch provides the deep learning framework for model training, while Torchvision supports image transformations and model-related utilities.

[opencv-python](https://opencv.org/) : OpenCV is critical for processing and analyzing video feeds in real-time. It enables image pre-processing, camera integration, and frame-by-frame analysis for detecting drowsiness.

[customtkinter](https://github.com/TomSchimansky/CustomTkinter) :  This library allowed the creation of a user-friendly graphical user interface (GUI) for the desktop application. It provided enhanced widget customization, improving the usability and aesthetics of the app.

[python-vlc](https://pypi.org/project/python-vlc/) : VLC integration enabled to capture video frame and the system to play voice sounds to notify when drowsiness was detected. It ensured timely alerts for the driver.

[numpy](https://numpy.org/) : Numpy was fundamental for numerical computations, including matrix operations and image data processing. It acted as the backbone for handling image arrays efficiently.

[matplotlib ](https://matplotlib.org/): Matplotlib was utilized for data visualization during the model training phase. It helped in analyzing metrics like loss curves and detection accuracy.

[labelImg](https://github.com/HumanSignal/labelImg.git) : LabelImg played a vital role in annotating the dataset. Proper image labeling is crucial for accurate training of the YOLOv5 model.

[yolov5/ultralytics](https://github.com/ultralytics/yolov5) : Ultralytics provided tools and scripts specifically optimized for YOLOv5 model training, evaluation, and fine-tuning, simplifying the overall workflow. 


## Getting Started:
These instructions will help to set up the project and run on local machine for further development and testing purposes.

1. Install and set up Python 3.
2. Create virtual environment in desired directory
3. Install the requirements.txt

## Running the program:
First create a new directory and clone the repo:
```
https://github.com/ris7055/Driver_Drowsiness_Detector.git
```

Then setup virtual env and activate from terminal/cmd in the same directory:
```
pip install virtualenv #if virtual environment dependency was not installed in pip packages
python -m virtualenv Driver_Drowsiness_Detector/venv
cd Driver_Drowsiness_Detector/
venv\Scripts\activate
```
Now Install the requirements.txt;
```
pip install -r requirements.txt
```
After this, access the application folder and run the app:
```
cd application
python drowsy_app.py
```
That's all! Thank you!

## Author

MD Raffaul Islam
Kuala Lumpur, Malaysia
raffaul7055@gmail.com

Azizar Mohammad Sadmam Sobhan
Kuala Lumpur, Malaysia
sasadmamaziz@gmail.com 

Nicolas Perera Niru Roy 
Dhaka, Bangladesh 
nicolaspereraniruroy2001@gmail.com 

Azizar Mohammad Sadmam Sobhan
Kuala Lumpur, Malaysia
sasadmamaziz@gmail.com 

Keiko Prakoso
Kuala Lumpur, Malaysia
keikorafi@gmail.com 

Bimo Kuncoro Yakti Prasetijo
Petaling Jaya, Malaysia
bimokuncoroyaktiprasetijo@gmail.com 

Muhammad Raditya Nayatama
Kuala Lumpur, Malaysia
radityanayatama@gmail.com 




