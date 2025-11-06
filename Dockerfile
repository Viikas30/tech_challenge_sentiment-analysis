FROM python:3.9-slim
WORKDIR /app

# Install dependencies, including uvicorn
COPY requirements.txt .
RUN pip install -r requirements.txt
# NOTE: Ensure uvicorn is listed in your requirements.txt!
# If you plan on running with gunicorn for production, you'd install that here too.

COPY . .

# Change the CMD to execute uvicorn
# The command format is: uvicorn <module>:<app-instance> --host 0.0.0.0 --port 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]