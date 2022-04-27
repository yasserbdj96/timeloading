# docker build -t timeloading-docker .
# docker run -i -t timeloading-docker
# 
FROM python:3.9

WORKDIR /wrdir

COPY ./examples.py /wrdir
COPY ./timeloading /wrdir/timeloading
COPY ./requirements.txt /wrdir/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /wrdir/requirements.txt

CMD ["python", "examples.py"]