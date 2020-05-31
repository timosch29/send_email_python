FROM python:3.7-alpine

COPY ./src/ /src

# make all app files readable (solves issue when dev in Windows, but building in Ubuntu)
RUN chmod -R 755  /src/

ENTRYPOINT ["python"]

CMD ["/src/send_email.py"]
