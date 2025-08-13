
# Cool Face Blurring Script (OpenCV + dlib)

![Face Blur Banner](https://github.com/Kieranmcm07/Face_Blur_Webcam/blob/main/assets/bannerexample.png?raw=true)

> A real-time Python script that detects faces using your webcam and applies a strong Gaussian blur for privacy, fun, or content creation.

```bash
python face_blur.py
Loading face detector...
Starting webcam...
Found 1 face(s).
```

## Features

* 🖥 Live Face Detection: Detects faces instantly using OpenCV’s Haar cascade.
* 😎 Strong Blur Effect: Obscures faces while keeping the background clear.
* 📊 Face Count Updates: Console updates only when the number of faces changes.
* 🎨 Colored Console Output: Uses Colorama for easy-to-read status messages.
* 🛑 Quick Exit: Press **Q** to exit cleanly without errors.

## Getting Started

### Prerequisites

* Python 3.8+
* A working webcam
* pip installed

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Kieranmcm07/Face_Blur_Webcam.git
```

2. Navigate to the folder:

```bash
cd Face_Blur_Webcam
```

3. Install required packages:

```bash
pip install opencv-python colorama
```

### Running the Script

```bash
python face_blur.py
```

* Webcam starts automatically
* Faces will be blurred in real-time
* Press **Q** to exit

## Settings

| Feature        | Description                        | Code Location         |
| :------------- | :--------------------------------- | :-------------------- |
| Blur Strength  | Higher kernel size = stronger blur | `GaussianBlur` line   |
| Padding        | Expands blur area around the face  | `pad = int(0.15 * w)` |
| Console Colors | Change message colors              | `Fore.YELLOW`, etc.   |

## Troubleshooting

1. **Webcam won’t start?**

   * Make sure no other program is using the camera
   * Check OS camera permissions

2. **No faces detected?**

   * Try better lighting
   * Adjust `scaleFactor` and `minNeighbors`

3. **Laggy video?**

   * Lower blur kernel size `(e.g., 25, 25)`
   * Reduce frame resolution

## License

This project is licensed under the MIT License – see [LICENSE](LICENSE) for details.

### Created with ⚡ by Kieranmcm07

<p align="center">
  <img src="https://img.shields.io/github/stars/Kieranmcm07/Face_Blur_Webcam?style=social" />
  <img src="https://img.shields.io/github/issues/Kieranmcm07/Face_Blur_Webcam?color=purple" />
  <img src="https://img.shields.io/github/license/Kieranmcm07/Face_Blur_Webcam" />
</p>

## Contribution

Pull requests welcome! Ideas include:

* Pixelation option instead of blur
* Video file support
* Adjustable blur strength in-script

```bash
# Build instructions
fork https://github.com/Kieranmcm07/Face_Blur_Webcam
git checkout -b feature/improvement
git commit -am 'Add new feature'
git push origin feature/improvement
Open Pull Request
```