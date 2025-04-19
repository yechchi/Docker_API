FROM python:3.9-slim
WORKDIR /app
COPY test_auth.py .
RUN pip install requests
CMD ["python", "test_auth.py"]