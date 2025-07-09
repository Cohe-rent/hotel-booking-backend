# Use official Python image
FROM python:3.12

# Set working directory
WORKDIR /app

# Copy requirements first
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest
COPY . .

# Expose your backend port (example: 5000)
EXPOSE 5000

# Command to run the app
# If Flask:
CMD ["python", "app.py"]
# If Django, replace with:
# CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]
