# Use an official Python base image
FROM python:3.11-slim

# Set working directory in the container
WORKDIR /app

# Copy project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port that Flask will run on
EXPOSE 5000

# Define the command to run your app
CMD ["python", "app.py"]
