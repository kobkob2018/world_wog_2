# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /wog_world

# Copy requirements.txt into the container
COPY ../requirements.txt /wog_world/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /wog_world/

# Expose port 8000
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1