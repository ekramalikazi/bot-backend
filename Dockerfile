FROM python:3.6
ENV FLASK_APP=app/app.py
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["-m", "flask", "run", "-h", "0.0.0.0", "-p", "8080"]
EXPOSE 8080