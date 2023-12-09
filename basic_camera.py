import cv2
import time

# Open the default camera (0 represents the default camera)
cap = cv2.VideoCapture(0)

# Initialize variables for frame rate calculation
start_time = time.time()
frame_count = 0

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Calculate frame rate
    frame_count += 1
    elapsed_time = time.time() - start_time
    fps = frame_count / elapsed_time

    # Display frame rate in red color on the frame
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow('Laptop Camera', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
