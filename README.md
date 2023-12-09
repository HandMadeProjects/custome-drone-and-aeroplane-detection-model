# Drone and Aeroplane Detection Project

This project uses a pre-trained model for detecting drones and aeroplanes in real-time using a webcam. The model is loaded using TensorFlow, and the results are displayed on the camera feed.

## Prerequisites

- Python 3
- OpenCV
- TensorFlow
- Colored (for colored console output)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/HandMadeProjects/custome-drone-and-aeroplane-detection-model.git
    cd your_repository
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python app.py
    ```

## Project Structure

- `app.py`: The main script for running the drone and aeroplane detection.
- `detection_model.h5`: Pre-trained model file for object detection.
- `requirements.txt`: List of Python dependencies.

## Usage

1. Ensure that your webcam is connected and accessible.

2. Run the application:

    ```bash
    python app.py
    ```

3. The camera feed will open, and the detected objects (drone, aeroplane, or none) will be displayed along with the frame rate.

4. Press 'q' to exit the application.

## Customization

- You can update the model path in `app.py` if your pre-trained model is located elsewhere.

- Adjust the label map in `app.py` to match the class labels of your model.

## Acknowledgements

- The pre-trained model used in this project was trained on drone, aeroplane, noise dataset.

- Model Trained on Kaggle : https://www.kaggle.com/code/mrappplg/custome-drone-and-aeroplane-detection-model

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
