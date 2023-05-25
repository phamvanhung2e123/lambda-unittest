# Container image that runs your code
FROM python:3.9.13
WORKDIR /app
COPY requirements.txt ./
COPY tests/aws.config /root/.aws/config
RUN pip install --no-cache-dir -r requirements.txt
CMD ["pytest", "-v", "tests"]

