FROM python:2.7
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ADD . /prod
WORKDIR /prod
EXPOSE 5000
CMD ["python", "run.py"]