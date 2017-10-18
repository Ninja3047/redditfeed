FROM alpine:3.6

RUN apk add --no-cache python3 py3-pip

RUN mkdir /redditfeed

COPY requirements.txt /redditfeed
WORKDIR /redditfeed
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

COPY redditfeed.py /redditfeed

EXPOSE 5000

ENTRYPOINT ["/usr/bin/gunicorn", "-w 4", "-b 0.0.0.0:5000", "redditfeed:app"]
