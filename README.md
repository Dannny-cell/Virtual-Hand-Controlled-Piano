# 🎹 Virtual Hand Controlled Piano

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%20%7C%203.11-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/MediaPipe-0.10.21-green?logo=google&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenCV-4.x-red?logo=opencv&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
  <img src="https://img.shields.io/badge/Platform-Windows-informational?logo=windows" />
</p>

<p align="center">
  A real-time virtual piano you play with your bare hands — no keyboard, no mouse, just gestures.
</p>

---

## 🎬 Demo

A live demonstration of the project is available on LinkedIn:

🔗 [Watch the demo on LinkedIn]
([https://www.linkedin.com/in/dannny-cell](https://www.linkedin.com/posts/dhananjay-jaiswal_python-opencv-mediapipe-activity-7352610206398193665-QDVB?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFFZA08BX6OKTQcoZqc35lnZX2f5IpgrC0Y))

---

## ✨ Features

| Feature | Description |
|---|---|
| 🖐 Real-time hand tracking | Uses MediaPipe to detect up to 21 hand landmarks per hand |
| 🎹 On-screen piano keyboard | Rendered directly on the live webcam feed via OpenCV |
| 👆 Hover detection | Highlights keys when a fingertip is positioned over them |
| 🎵 Press detection | Triggers a note when the finger bends downward past a threshold |
| 🔊 Audio playback | Plays real `.wav` piano samples with `pygame` |
| 💡 Visual feedback | Shows hover, pressed, and sustained note states in real time |
| 🧩 Modular codebase | Clean separation of concerns across dedicated Python modules |

---

## 🗂️ Project Structure

```
Virtual-Hand-Controlled-Piano/
├── piano.py           # Main entry point — runs the app loop
├── audio.py           # Loads and plays .wav note samples
├── collision.py       # Detects fingertip-to-key collisions
├── hand_tracking.py   # MediaPipe hand landmark detection
├── piano_layout.py    # Defines key positions and note mappings
├── rendering.py       # Draws the piano and overlays onto the frame
├── utils.py           # Shared helper functions
├── requirements.txt   # Pinned Python dependencies
└── README.md
```

---

## ⚙️ How It Works

```
Webcam Frame
     │
     ▼
MediaPipe Hand Tracking  ──►  21 Landmarks per hand
     │
     ▼
Fingertip Positions  ──►  Collision Detection against Key Regions
     │
     ├── Fingertip over key?  ──►  Highlight key (hover state)
     │
     └── Finger bent enough?  ──►  Play .wav sample + Press visual
```

1. **Capture** — OpenCV reads frames from your webcam.
2. **Track** — MediaPipe identifies all visible hand landmarks.
3. **Detect** — Each fingertip's position is tested against the piano key regions.
4. **Trigger** — A note plays when the finger bends past the press threshold.
5. **Render** — The piano, hover highlights, and pressed states are drawn over the live feed.

---

## 🖥️ Requirements

- **OS:** Windows (PowerShell used for venv activation)
- **Python:** 3.10 or 3.11 recommended
- **Hardware:** A working webcam
- **Audio:** Piano `.wav` sample files (see [Audio Samples](#-audio-samples) below)

---

## 📦 Installation

### 1. Clone the repository

```powershell
git clone https://github.com/Dannny-cell/Virtual-Hand-Controlled-Piano.git
cd Virtual-Hand-Controlled-Piano
```

### 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

> ⚠️ **Important:** This project uses `mediapipe==0.10.21` because it relies on the legacy `mp.solutions.hands` API. Newer versions of MediaPipe removed this interface and will cause errors.

---

## 🎵 Audio Samples

The app expects piano note `.wav` files in:

```
D:\piano_wav\
```

### Expected filenames

```
c3.wav   d3.wav   e3.wav   f3.wav   g3.wav   a3.wav   b3.wav
c#3.wav  d#3.wav  f#3.wav  g#3.wav  a#3.wav
c4.wav   d4.wav   e4.wav   f4.wav   g4.wav   a4.wav   b4.wav
c#4.wav  d#4.wav  f#4.wav  g#4.wav  a#4.wav
c5.wav
```

### Using a different folder

If your samples are stored elsewhere, open `audio.py` and update the `DEFAULT_SAMPLES_DIR` constant:

```python
DEFAULT_SAMPLES_DIR = r"C:\path\to\your\piano_wav"
```

### Where to get free piano samples

- [freesound.org](https://freesound.org) — search "piano note C4" etc.
- [University of Iowa MIS](https://theremin.music.uiowa.edu/MIS.html) — free high-quality samples
- [SampleSwap](https://sampleswap.org) — royalty-free audio library

---

## ▶️ Running the App

Make sure your virtual environment is active, then:

```powershell
.\.venv\Scripts\Activate.ps1
python piano.py
```

A window will open showing your webcam feed with the piano keyboard overlaid at the bottom.

---

## 🖐️ Controls

| Action | Result |
|---|---|
| Move fingertip over a key | Key highlights (hover) |
| Bend finger downward | Key press + note plays |
| Multiple fingers | Play chords |
| Press `Q` | Quit the application |

---

## 🛠️ Troubleshooting

### ❌ `module 'mediapipe' has no attribute 'solutions'`

You have a newer, incompatible version of MediaPipe installed. Fix it with:

```powershell
pip uninstall -y mediapipe
pip install --no-cache-dir mediapipe==0.10.21
```

### 🔇 No sound is playing

- Confirm `D:\piano_wav` exists (or that your custom path in `audio.py` is correct)
- Confirm the folder contains valid `.wav` files
- Confirm filenames match the expected format exactly (e.g. `c4.wav`, not `C4.wav` or `piano_c4.wav`)
- Check your system volume and audio output device

### 📷 Webcam window does not open

- Make sure your webcam is plugged in and not in use by another app (Teams, Zoom, etc.)
- Try changing the camera index in `piano.py`: `cv2.VideoCapture(0)` → `cv2.VideoCapture(1)`
- Confirm OpenCV installed correctly: `python -c "import cv2; print(cv2.__version__)"`

### ✋ Hand not detected

- Ensure good, even lighting on your hand
- Keep your hand within 40–70 cm of the webcam
- Avoid backgrounds that are similar in color to your skin tone

---

## 🧰 Tech Stack

| Library | Version | Purpose |
|---|---|---|
| [MediaPipe](https://google.github.io/mediapipe/) | 0.10.21 | Hand landmark detection |
| [OpenCV](https://opencv.org/) | 4.x | Webcam capture & rendering |
| [pygame](https://www.pygame.org/) | 2.x | `.wav` audio playback |
| [NumPy](https://numpy.org/) | 1.x | Array math for landmark coordinates |

---

## 📄 License

This project is released under the [MIT License](LICENSE).

---

<p align="center">Made with 🎹 and Python</p>
