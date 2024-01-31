FROM python:3.8
COPY . /app
WORKDIR /app
ENV PYTHONPATH .
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt
COPY *.py /app/
EXPOSE 7531
CMD ["python", "main.py"]