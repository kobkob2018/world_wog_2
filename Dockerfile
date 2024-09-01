# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /wog_world

# Install dependencies
#install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1


