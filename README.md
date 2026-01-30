# Auto-Framing: Face-Tracking Digital Zoom

> **Turn your standard webcam into an AI-powered smart camera.**

Auto-Framing uses computer vision to digitally replicate the "follow-me" feature found in high-end conference cameras. By leveraging the lightweight **YuNet** deep learning model, it detects your face in real-time and dynamically pans and zooms to keep you in the spotlight—no expensive hardware required.

##  Key Features

* **Intelligent Tracking:** The camera "knows" where you are. If you lean back or move around, the frame follows you automatically.
* **Dual-Stage Digital Zoom:** Seamlessly toggle between **1.5x** (Presenter Mode) and **2x** (Close-up Mode).
* **Smooth-Motion Logic:** Built-in tolerance zones prevent the "jittery cameraman" effect, ensuring the view only moves when *you* do.

---

## Prerequisites

* **Python 3.7+**
* A standard webcam

##  Installation & Setup

### 1. Clone the Repository
Get the code on your local machine:
```bash
git clone [https://github.com/NitinYadav354/Auto-Framing](https://github.com/NitinYadav354/Auto-Framing)
cd Auto-Framing

2. Install Dependencies: 
We rely on opencv-python for vision processing and numpy for matrix math:
pip install opencv-python numpy

3. Download the Brain (Required):
This project uses the YuNet ONNX model for lightning-fast face detection. To keep this repo lightweight, the model is not included.Click here to download face_detection_yunet_2023mar.onnxAction: Place the downloaded .onnx file in the root folder of this project (right next to your python script).

How to Run:
Simply execute the main script:
python main.py

ControlsKeyAction
1               1.5x Zoom (Medium Crop)
2               2x Zoom (Tight Crop)
W/A/S/D         Manual Override 
Q               Quit

Under the Hood;
How do we make it smooth?
Detection: Every frame, YuNet scans for faces.
Dead Zone Calculation: We calculate a "Tolerance Box" in the center of the current view.

Decision Logic:
Is the face inside the box? -> Do nothing (Keep video steady).
Is the face outside? -> Pan the offset coordinates towards the face at ~1.5% screen width per frame.
Rendering: The image is cropped based on the offset and resized back to the original resolution, creating a seamless zoom effect.

License:
This project is licensed under the MIT License - free to use and modify!