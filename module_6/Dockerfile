# Dockerfile

# 1. Use python:3.10 as the base environment
FROM python:3.10

# 2. Set the working directory to /module_6
WORKDIR /module_6

# 3. Copy requirements.txt into the container at /module_6
COPY requirements.txt /module_6/

# 4. Install requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application code into the container
COPY . /module_6

# 6. Expose port 8080
EXPOSE 8080

# 7. Start the Flask application
CMD ["python", "run.py"]