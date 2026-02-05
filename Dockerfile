FROM python:3.12-slim  

RUN python -m venv /venv  
ENV PATH="/venv/bin:$PATH"  

RUN pip install "django<6" gunicorn whitenoise
COPY . /src  

WORKDIR /src  

# สั่งให้รัน migrate ก่อน แล้วค่อยรัน server
CMD ["gunicorn", "--bind", ":8888", "superlists.wsgi:application"]