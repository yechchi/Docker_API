FROM python:3.9-slim
WORKDIR /app
COPY test_content.py .
RUN pip install requests
CMD ["python", "test_content.py"]