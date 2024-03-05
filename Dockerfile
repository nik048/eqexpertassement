FROM python:3.11.5

ARG USER_NAME=equalexperts
RUN adduser  $USER_NAME

WORKDIR /opt/app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chown -R $USER_NAME /opt/app
RUN chmod -R 777 /opt/app
USER $USER_NAME

EXPOSE 8080
CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080" ]

