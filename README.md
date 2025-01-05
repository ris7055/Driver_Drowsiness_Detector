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
## Testing and Results in Real-World Scenario:
The tests were conducted in conditions with background effects and lighting

1. Different lighting conditions.
2. Drivers posture and position of drivers face.

```
Test case 1: Optimal Lighting effect
Detection: State_Awake
```

<img src="/outcomes/awake_state.png" alt="Awake_State.png" width="400" height="400">

```
Result:
The image showcases a real-time driver drowsiness detection system in action, identifying the driver's state as 'Awake' with a confidence score of 0.70. 
So,using the YOLOv5 model, the system accurately detects and tracks the driver’s face through a bounding box and evaluates key facial features such as eye openness and overall alertness. 
The detection is performed via a live video stream, processed in real time, and displayed on the interface.
```


```
Test case 2: Bright Lighting effect
Detection: State_Awake
```
<img src="/outcomes/yawn_state.png" alt="Yawn_State.png" width="400" height="400">


```
Result:
The image demonstrates the Driver Drowsiness Detection System identifying the driver's state as 'Yawn' with a confidence score of 0.73 using the YOLOv5 model.
The system accurately detects facial features and identifies signs of fatigue, such as yawning, by analyzing real-time video streams.
The bounding box highlights the driver's face, and the system classifies the state based on detected cues. 
```

```
Test case 3: Poor Lighting effect
Detection: State_drowsy
```
<img src="/outcomes/drowsy_state.png" alt="Yawn_State.png" width="400" height="400">


```
The image illustrates the Driver Drowsiness Detection System identifying the driver's state as 'Drowsy' with a confidence score of 0.86 using the YOLOv5 model even in poor light condition.
The system analyzes facial cues, such as closed eyes and head position, from a real-time video stream to determine signs of fatigue. A bounding box highlights the driver’s face, and the detected state is displayed with its confidence score. Additionally, the interface includes a counter (showing 15 drowsiness events) and a 'Reset Counter' button for recalibration. An alert icon is also visible, indicating an active warning mechanism in which if the confidence level is greater than 0.85 the voice alert will produce sound "Wake up! You're feeling drowsy" to create awareness for the driver.
```

## References:

IEEE standard Journal Paper,

[1] Y. R, V. Ritheesh, S. Reddy and R. G. Rajan, "Driver Drowsiness Detection and Alert System using YOLO," 2022 International Conference on Innovative Computing, <br>
Intelligent Communication and Smart Electrical Systems (ICSES), Chennai, India, 2022, pp. 1-6, [doi: 10.1109/ICSES55317.2022.9914261.](https://ieeexplore.ieee.org/document/9914261)

[2] B. Yazici, A. Özdemir and T. Ayhan, "System-on-Chip Based Driver Drowsiness Detection and Warning System," <br>
2022 Innovations in Intelligent Systems and Applications Conference (ASYU), Antalya, Turkey, 2022, pp. 1-5, [doi: 10.1109/ASYU56188.2022.9925481.](https://ieeexplore.ieee.org/document/9925481)

[3] Salah Eddine Bekhouche, Yassine Ruichek, Fadi Dornaika,
Driver drowsiness detection in video sequences using hybrid selection of deep features, Knowledge-Based Systems,ISSN 0950-7051, <br>
[https://doi.org/10.1016/j.knosys.2022.109436.](https://www.sciencedirect.com/science/article/abs/pii/S0950705122007225?via%3Dihub)
 
[4] S. Rathod, T. Mali, Y. Jogani, N. Faldu, V. Odedra and P. K. Barik, "RealD3: A Real-time Driver Drowsiness Detection Scheme Using Machine Learning," <br>
2023 IEEE Wireless Antenna and Microwave Symposium (WAMS), Ahmedabad, India, 2023, pp. 1-5, [doi: 10.1109/WAMS57261.2023.10242860.](https://ieeexplore.ieee.org/document/10242860)

[5] M. T. Soe, A. Zaw Min, H. T. Kyaw, M. Min Paing, S. M. Htet and B. Aye, "Abnormal Behavior Detection in Real-time for Advanced Driver Assistance System (ADAS) using YOLO," <br>
2022 IEEE Symposium on Industrial Electronics & Applications (ISIEA), Langkawi Island, Malaysia, 2022, pp. 1-6, [doi: 10.1109/ISIEA54517.2022.9873672.](https://ieeexplore.ieee.org/document/9873672)


That's all! Thank you!

## Author and contributed by:

MD Raffaul Islam <br>
Kuala Lumpur, Malaysia <br>
raffaul7055@gmail.com

Azizar Mohammad Sadmam Sobhan <br>
Kuala Lumpur, Malaysia <br>
sasadmamaziz@gmail.com 

Nicolas Perera Niru Roy <br>
Dhaka, Bangladesh <br>
nicolaspereraniruroy2001@gmail.com 

Keiko Prakoso <br>
Kuala Lumpur, Malaysia <br>
keikorafi@gmail.com 

Bimo Kuncoro Yakti Prasetijo <br>
Petaling Jaya, Malaysia <br>
bimokuncoroyaktiprasetijo@gmail.com 

Muhammad Raditya Nayatama <br>
Kuala Lumpur, Malaysia <br>
radityanayatama@gmail.com 




