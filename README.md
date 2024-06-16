# Temple Run Controller Using Body Gesture

This project demonstrates a novel way to control the Temple Run game using body gestures captured via a webcam. Using computer vision and machine learning techniques, the script detects specific poses and translates them into keyboard inputs to control the game.

## Video Demo
[![Watch the video](path_to_thumbnail)](path_to_your_video)

## Table of Contents
- [Introduction](#introduction)
- [Technology Stack](#technology-stack)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Introduction

The Temple Run Controller Using Body Gesture project allows users to play Temple Run using their body movements. The program captures video input from a webcam, detects specific poses using the MediaPipe library, and converts these poses into corresponding keyboard inputs to control the game. This innovative method of interaction provides a fun and engaging way to play Temple Run.

## Technology Stack

- **Python**: The programming language used for the script.
- **OpenCV**: For video capture and image processing.
- **MediaPipe**: For pose detection and tracking.
- **pynput**: To simulate keyboard inputs.
- **TensorFlow Lite**: For model inference (optional, based on warnings seen).
- **pygetwindow**: To manage the game window focus.

## Setup Instructions

### Prerequisites

- Python 3.x
- Webcam
- Temple Run game installed on your computer

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/your_username/temple-run-controller.git
    cd temple-run-controller
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    venv\Scripts\activate   # On Windows
    source venv/bin/activate  # On macOS/Linux
    ```

3. Install the required libraries:

    ```sh
    pip install -r requirements.txt
    ```

4. Ensure your `requirements.txt` includes the following dependencies:

    ```plaintext
    opencv-python
    mediapipe
    pynput
    numpy<2.0.0
    pygetwindow
    ```

### Running the Project

1. Start the Temple Run game.
2. Run the script:

    ```sh
    python main.py
    ```

3. Ensure the game window is active to receive keyboard inputs.

## Usage

- **Up Gesture**: Raise both arms to simulate jumping.
- **Down Gesture**: Move your body down to simulate sliding.
- **Left Gesture**: Move your left hand to the left to turn left.
- **Right Gesture**: Move your right hand to the right to turn right.

The script will detect these gestures and translate them into corresponding keyboard inputs to control the character in the Temple Run game.

## Acknowledgements

- [MediaPipe](https://google.github.io/mediapipe/) by Google for providing the pose detection solution.
- [OpenCV](https://opencv.org/) for the powerful computer vision functions.
- [pynput](https://pynput.readthedocs.io/) for the easy-to-use keyboard input simulation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

