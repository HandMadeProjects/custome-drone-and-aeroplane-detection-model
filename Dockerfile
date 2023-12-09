# Use an official TensorFlow runtime as a parent image
FROM tensorflow/tensorflow:latest-gpu

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install Python dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install tensorflow &&\
    pip3 install opencv-python &&\
    pip3 install colored

# Copy the current directory contents into the container at /app
COPY . /app

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python3", "your_script_name.py"]
