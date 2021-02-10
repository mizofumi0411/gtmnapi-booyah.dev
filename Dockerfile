FROM python:3.8

RUN apt update -y

WORKDIR /app

COPY src/requirements.txt .

RUN pip install -r requirements.txt

RUN ls -la /app

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8880"]

#CMD ["/bin/bash", "/app/launch.sh"]
