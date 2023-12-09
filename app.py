import cv2
import numpy as np
import tensorflow as tf
import time


from colored import fg, attr

# ANSI escape codes for colors
RED = fg('red')
GREEN = fg('green')
YELLOW = fg('yellow')
RESET = attr('reset')

# Load the pre-trained model
model_path = 'detection_model.h5'  # Update with your actual model file path
loaded_model = tf.keras.models.load_model(model_path)

# Load label map
label_map = {
    0: "No drone or aeroplane",
    1: "Aeroplane",
    2: "Drone"
}

# Set up the camera
cap = cv2.VideoCapture(0)  # Use 0 for the default camera, adjust if necessary

# Initialize variables for frame rate calculation
start_time = time.time()
frame_count = 0

__predicted_class = []

label = "setup"

while True:
    ret, image_np = cap.read()
    ogImage = image_np
    # Check if the image is not empty
    if image_np is not None:
        # Print image dimensions for debugging
        # print("Image dimensions before resize:", image_np.shape)

        # Calculate frame rate
        frame_count += 1
        elapsed_time = time.time() - start_time
        fps = frame_count / elapsed_time

        # Display frame rate in red color on the frame
        cv2.putText(ogImage, f"FPS: {fps:.2f}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)


        # Preprocess the image for the model
        image_np = cv2.resize(image_np, (224, 224))  # Adjust size as needed
        image_np = image_np / 255.0  # Normalize pixel values to be between 0 and 1
        image_np = np.expand_dims(image_np, axis=0)  # Add batch dimension

        # Print image dimensions after resize for debugging
        # print("Image dimensions after resize:", image_np.shape)

        # Run inference on the model
        prediction = loaded_model.predict(image_np)
        predicted_class = np.argmax(prediction)
        __predicted_class.append(predicted_class)

        # taking an average... 
        # if len(__predicted_class) == 10:
        #     print(predicted_class)
        #     label = label_map[predicted_class]

        label = label_map[predicted_class]
        print(GREEN + "----------------------------------------------------------------- label : " + label + str(predicted_class) + RESET)
            # Display custom label in blue color on the frame

        cv2.putText(ogImage, label, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)


        # Display the resulting image
        # cv2.imshow('Object Detection', cv2.resize(image_np.squeeze(), (800, 600)))
        cv2.imshow('Object Detection', ogImage)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
