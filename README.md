# 🧫 Siwiti Colony Counter

A desktop application for **automated bacterial colony counting from biological images**.

The Siwiti Colony Counter allows users to upload an image containing microbial colonies and automatically estimate the number of colonies using **computer vision and image-processing techniques**.

The project combines biotechnology with Python programming and computer vision to demonstrate how digital tools can support microbiological analysis.

---

## 📌 Project Overview

Counting microbial colonies manually can be time-consuming, especially when a culture plate contains a large number of colonies.

This project aims to provide a simple desktop-based solution that can:

- Upload colony images
- Display the selected image
- Process the image using computer vision
- Detect colony-like objects
- Estimate the number of colonies
- Display the counting result in the application
- Provide a user interface for connecting with a phone

---

## 🖥️ Application Interface

The application is built using **CustomTkinter**, providing a modern graphical user interface.

Main features include:

- 🏠 Home
- 👤 Profile
- ❓ Help
- 🧫 Upload Image
- ⚙️ Settings
- 📱 Link Phone
- 📊 Colony counting result

---

## 🧬 Biotechnology Application

The project demonstrates an application of programming and biotechnology.

In microbiology, colonies growing on culture media can be counted to estimate microbial concentration. Automated image analysis can assist researchers and laboratory personnel by reducing the amount of manual counting required.

The basic workflow is:

Biological Sample
       ↓
Culture Plate
       ↓
Image Acquisition
       ↓
Image Processing
       ↓
Colony Detection
       ↓
Colony Counting
       ↓
Result

---

## 🛠️ Technologies Used

### Python

Python is used as the main programming language.

It handles:

- Application logic
- Image processing
- File handling
- GUI interaction
- Colony detection

### CustomTkinter

Used to create the graphical user interface.

### OpenCV

OpenCV is used for computer vision and image processing.

Current processing includes techniques such as:

- Grayscale conversion
- Gaussian blurring
- Circle detection
- Image analysis

### Pillow

Pillow is used for loading and displaying images within the application.

### NumPy

NumPy supports numerical operations used during image processing.

---

## 📂 Project Structure

Siwiti-Colony-Counter/
│
├── main.py
├── class_counter.py
│
├── ui/
│   └── colony_counter.py
│
├── pages/
│   └── phone_connector.py
│
├── reusable_tasks/
│   └── tasks.py
│
├── assets/
│   ├── colony_counter.webp
│   ├── connect_phone.jfif
│   ├── dna_icon.jfif
│   ├── icon.ico
│   ├── images_colonies.jfif
│   ├── images_help.png
│   ├── images_home.jfif
│   ├── profile.jfif
│   └── settings.jfif
│
├── templates/
│   └── index.html
│
└── README.md

---

## ⚙️ Installation

### 1. Clone the repository


Move into the project directory:

cd Siwiti-Colony-Counter

### 2. Create a virtual environment

python -m venv .venv

Activate it on Windows:

.venv\Scripts\activate

### 3. Install dependencies

pip install customtkinter
pip install pillow
pip install opencv-python
pip install numpy

Or, if a `requirements.txt` file is available:

pip install -r requirements.txt

---

## ▶️ Running the Application

Run:

python main.py

The application window should open.

Select:

Upload Image

Choose a colony image and click:

Submit


The application processes the image and displays the estimated colony count.

---

## 🔬 Colony Detection

The colony detection module is implemented in:

class_counter.py


The main class is:

ColonyCounter

Example:

from class_counter import ColonyCounter

counter = ColonyCounter("sample.jpg")

result = counter.counter_colonies()

print(result["normal"])


The result is returned as a dictionary:

{
    "normal": number_of_colonies
}

---

## 🧪 Image Processing Pipeline

The current colony detection approach uses OpenCV.

The general processing pipeline is:

Input Image
     ↓
Convert to Grayscale
     ↓
Gaussian Blur
     ↓
Circle Detection
     ↓
Filter Detected Objects
     ↓
Count Colonies
     ↓
Return Result

The detection parameters can be adjusted depending on:

- Colony size
- Image resolution
- Lighting conditions
- Colony density
- Background characteristics
- Distance between colonies

Therefore, images with significantly different characteristics may require different detection parameters.

---



This component is intended to support connecting a mobile device with the desktop application for image acquisition or transfer.

Future versions can extend this feature to allow users to:

- Capture colony images using a smartphone
- Transfer images directly to the computer
- Process images automatically
- Send counting results back to the phone

---

## 🚀 Future Improvements

Planned improvements include:

- [ ] Improve colony detection accuracy
- [ ] Automatically separate touching colonies
- [ ] Improve detection under different lighting conditions
- [ ] Add colony-size filtering
- [ ] Add image preprocessing controls
- [ ] Add automatic image enhancement
- [ ] Display detected colonies visually
- [ ] Add result history
- [ ] Export results to CSV
- [ ] Export analysis reports
- [ ] Improve phone connectivity
- [ ] Add camera-based image acquisition
- [ ] Package the application as a Windows executable
- [ ] Add machine-learning-based colony classification

---

## 🎯 Project Goals

The main goal of the project is to demonstrate how **biotechnology, programming, and computer vision** can be combined to solve practical laboratory problems.

The project can be further developed into a laboratory-support tool for microbial enumeration and image-based biological analysis.

---

## 👨‍💻 Author

**Yoel Siwiti**

Biotechnology | Bioinformatics | Python | Data Analysis | Computer Vision

GitHub:  
https://github.com/yoelysiwiti

LinkedIn:  
www.linkedin.com/in/yoeli-siwiti-a7b354441
---

## 📄 License

This project is intended for educational, research, and development purposes.

A suitable open-source license can be added as the project develops.
``This version is good for your GitHub repository because it connects the project clearly to **biotechnology + Python + computer vision**, rather than making it look like just a Tkinter programming exercise.

If you give me your **actual GitHub username/repository name**, I can also replace the placeholders and make the README fully ready to paste into GitHub.
