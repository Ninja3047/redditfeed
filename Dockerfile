FROM alpine:3.6

RUN apk add --no-cache python3 py3-pip

RUN mkdir /redditfeed

COPY requirements.txt /redditfeed
WORKDIR /redditfeed
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

COPY redditfeed.py /redditfeed

EXPOSE 5000

ENTRYPOINT ["python3", "redditfeed.py"]
