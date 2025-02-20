# Use base Python image
FROM python:3.9.6-buster

# Set working directory inside the container
WORKDIR /app

# Copy repo into container
COPY . .

# Install any requirements

RUN pip install --no-cache-dir -r requirements.txt

# Run Python program
CMD [ "python", "./main.py" ]