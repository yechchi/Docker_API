FROM python:3.9-slim
WORKDIR /app
COPY test_authz.py .
RUN pip install requests
CMD ["python", "test_authz.py"]