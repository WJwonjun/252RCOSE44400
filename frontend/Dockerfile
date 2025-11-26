ARG PYTHON_VERSION=3.11.14-slim
FROM python:${PYTHON_VERSION}
RUN pip install flask requests
WORKDIR /frontend
COPY templates ./templates
COPY app_front.py .
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app_front.py"]
