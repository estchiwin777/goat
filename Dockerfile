FROM python:3.12-slim  

RUN python -m venv /venv  
ENV PATH="/venv/bin:$PATH"  

COPY requirements.txt /tmp/requirements.txt  
RUN pip install -r /tmp/requirements.txt 

COPY . /src  

WORKDIR /src  
# 1. เพิ่มบรรทัดนี้เพื่อรวบรวมไฟล์ CSS/JS ทั้งหมดไปไว้ในที่เดียว
RUN python manage.py collectstatic --noinput
# 2. ตั้งค่าให้ Django รู้ว่าตอนนี้คือโหมด Production (DEBUG=False)
ENV DJANGO_DEBUG_FALSE=1

# สั่งให้รัน migrate ก่อน แล้วค่อยรัน server
CMD ["gunicorn", "--bind", "0.0.0.0:8888", "mysite.wsgi:application"]