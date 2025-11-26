ARG PYTHON_VERSION=3.11.14-slim
FROM python:${PYTHON_VERSION}
RUN pip install flask
WORKDIR /backend
RUN mkdir -p /data
COPY app_back.py .
EXPOSE 5001
ENTRYPOINT ["python"]
CMD ["app_back.py"]
