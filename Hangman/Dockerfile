# Use the official Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Python dependencies (if any)
RUN pip install --no-cache-dir -r requirements.txt || true

# Command to run the game
CMD ["python", "hangman.py"]
