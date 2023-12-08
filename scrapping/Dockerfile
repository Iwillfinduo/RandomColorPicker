FROM python:3.10
WORKDIR /app
COPY . /app
RUN apt-get update
RUN pip install -r requirements.txt
RUN apt-get install -y libnss3 libdbus-1-3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libxkbcommon0 libatspi2.0-0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libasound2
RUN playwright install
CMD [ "python3", "scraping_api.py"]