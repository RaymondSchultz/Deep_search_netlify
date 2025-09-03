# Use an official, lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your requirements file into the container
COPY requirements.txt .

# Install all the Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy all your project files (app.py, etc.) into the container
COPY . .

# Tell Cloudflare which port your app will run on
EXPOSE 8501

# The command to start your Streamlit app when the container launches
CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.enableCORS", "false", "--server.enableXsrfProtection", "false"]
