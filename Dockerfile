FROM python:3.12-slim  

RUN python -m venv /venv  
ENV PATH="/venv/bin:$PATH"  

RUN pip install "django<6"
COPY . /src  

WORKDIR /src  

# สั่งให้รัน migrate ก่อน แล้วค่อยรัน server
CMD ["sh", "-c", "/venv/bin/python manage.py migrate && /venv/bin/python manage.py runserver 0.0.0.0:8888"]