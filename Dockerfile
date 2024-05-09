# Use Python 3.11 base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

#Install Required libraries for OpenCV in Python
RUN apt-get update && apt-get install -y python3-opencv

# Copy requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy Python code for gRPC service and protobuf files
COPY . .

# Expose gRPC server port
EXPOSE 50051

# Define the command to run the server
CMD ["python", "regionDetection.py"] 