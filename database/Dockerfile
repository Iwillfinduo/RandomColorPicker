FROM python:3.10
WORKDIR /app
COPY . /app
EXPOSE 4343
RUN pip install -r requirements.txt
RUN mkdir -p data
CMD [ "python3", "main.py"]