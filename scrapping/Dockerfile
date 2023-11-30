FROM python:3.10
WORKDIR /app
COPY . /app
EXPOSE 6969
RUN pip install -r requirements.txt
RUN playwright install
CMD [ "/bin/ls", "-l" ]
CMD [ "python3", "scraping_api.py"]