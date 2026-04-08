# Virtual Hand Controlled Piano

This project is a real-time virtual piano that uses your webcam, MediaPipe hand tracking, and OpenCV rendering. You play notes by hovering a fingertip over a piano key and bending the finger to trigger a press.

## Features

- Real-time hand tracking with MediaPipe
- Virtual piano keyboard rendered on the webcam feed
- Hover, press, and sustain feedback on screen
- Modular Python codebase for hand tracking, collision detection, rendering, and audio

## Project Structure

```text
Virtual-Hand-Controlled-Piano/
|-- piano.py
|-- audio.py
|-- collision.py
|-- hand_tracking.py
|-- piano_layout.py
|-- rendering.py
|-- utils.py
|-- requirements.txt
|-- README.md
```

## How It Works

1. The webcam feed is captured with OpenCV.
2. MediaPipe detects hand landmarks for visible fingers.
3. Fingertip positions are checked against the on-screen piano key regions.
4. A note is played when a fingertip is over a key and the finger bends enough to count as a press.
5. The app shows the current hover, pressed, and sustained notes in real time.

## Requirements

- Python 3.10 or 3.11 recommended
- A working webcam
- Windows PowerShell
- Piano `.wav` sample files

## Python Dependencies

Install the exact dependencies from:

```powershell
pip install -r requirements.txt
```

Current pinned dependency note:

- `mediapipe==0.10.21` is used because this project relies on the legacy `mp.solutions.hands` API.

## Setup

Clone the repository and create a virtual environment:

```powershell
git clone https://github.com/Dannny-cell/Virtual-Hand-Controlled-Piano.git
cd Virtual-Hand-Controlled-Piano
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Audio Samples

This project expects piano note `.wav` files to be available in:

```text
D:\piano_wav
```

Each file should be named after the note, for example:

```text
c3.wav
d3.wav
e3.wav
f3.wav
g3.wav
a3.wav
b3.wav
c4.wav
c#3.wav
d#3.wav
...
c5.wav
```

If your samples are stored somewhere else, update `DEFAULT_SAMPLES_DIR` in `audio.py`.

## Run

From the project folder:

```powershell
.\.venv\Scripts\Activate.ps1
python piano.py
```

## Controls

- Show your hand clearly in front of the webcam
- Move a fingertip over a piano key to hover it
- Bend the finger downward to press the key
- Press `q` to quit the application

## Troubleshooting

### MediaPipe error: `module 'mediapipe' has no attribute 'solutions'`

Use the pinned dependency version:

```powershell
pip uninstall -y mediapipe
pip install --no-cache-dir mediapipe==0.10.21
```

### No sound is playing

- Make sure `D:\piano_wav` exists
- Make sure the folder contains valid `.wav` files
- Make sure the note names match the expected filenames

### Webcam window does not open

- Check that your webcam is connected
- Close other apps that may already be using the camera
- Make sure OpenCV installed successfully

## Future Improvements

- Make the sample directory configurable from an environment variable or command-line argument
- Add unit tests for collision detection and note formatting
- Add a proper `config.py` for runtime settings
- Improve README setup with screenshots or GIFs

## License

This project is released under the MIT License.
