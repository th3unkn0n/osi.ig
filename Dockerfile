FROM python:3

COPY main.py /
COPY .lib /
COPY requirements.txt /

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]
