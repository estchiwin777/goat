FROM python:3.12-slim  

# 1. เตรียม Environment (รันด้วย Root)
RUN python -m venv /venv  
ENV PATH="/venv/bin:$PATH"  
ENV PYTHONUNBUFFERED=1
ENV DJANGO_DEBUG_FALSE=1

# 2. ติดตั้ง Dependencies
COPY requirements.txt /tmp/requirements.txt  
RUN pip install --no-cache-dir -r /tmp/requirements.txt 

# 3. เตรียมไฟล์โปรเจกต์
COPY . /src  
WORKDIR /src  

# 4. จัดการ Static Files และสิทธิ์การใช้งาน
RUN python manage.py collectstatic --noinput
RUN adduser --uid 1234 nonroot && chown -R nonroot:nonroot /src /venv
USER nonroot

# 5. สั่งรันแอปบนพอร์ต 8080 (ให้ตรงกับ Networking)
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "mysite.wsgi:application"]