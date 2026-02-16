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

RUN adduser --uid 1234 nonroot
USER nonroot

# สั่งให้รัน migrate ก่อน แล้วค่อยรัน server
CMD ["gunicorn", "--bind", "0.0.0.0:8888", "mysite.wsgi:application"]FROM python:3.12-slim  

RUN python -m venv /venv  
ENV PATH="/venv/bin:$PATH"  

COPY requirements.txt /tmp/requirements.txt  
RUN pip install -r /tmp/requirements.txt 

COPY . /src  
WORKDIR /src  

# รวบรวมไฟล์ Static
RUN python manage.py collectstatic --noinput

# ตั้งค่า Environment มาตรฐาน
ENV DJANGO_DEBUG_FALSE=1
ENV PYTHONUNBUFFERED=1

# แก้ไขสิทธิ์ให้ nonroot เข้าถึงไฟล์ใน /src ได้
RUN adduser --uid 1234 nonroot && chown -R nonroot:nonroot /src
USER nonroot

# ใช้พอร์ตจากตัวแปรระบบ (ห้ามระบุเลขตายตัว)
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "mysite.wsgi:application"]