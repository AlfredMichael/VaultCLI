# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install required dependencies
RUN pip install -r requirements.txt

# Create the Desktop directory for temporary files
RUN mkdir -p /root/Desktop

# Define the command to run your app
CMD ["python", "main.py"]
