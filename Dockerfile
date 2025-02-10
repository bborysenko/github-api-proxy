# Use an official Python runtime as a parent image.
FROM python:3.12-slim

# Set the working directory in the container.
WORKDIR /app

# Copy the requirements file into the container and install dependencies.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container.
COPY . .

# Set environment variables for Flask.
# FLASK_APP points to the module that should be run.
# FLASK_RUN_HOST ensures the server listens on all network interfaces.
ENV FLASK_APP=app/server.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port 5000 for the Flask app.
EXPOSE 5000

# Command to run the application.
CMD ["flask", "run"]
