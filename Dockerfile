FROM python:3.12-slim  

RUN python -m venv /venv  
ENV PATH="/venv/bin:$PATH"  

COPY requirements.txt /tmp/requirements.txt  
RUN pip install -r /tmp/requirements.txt 

COPY . /src  

WORKDIR /src  

# สั่งให้รัน migrate ก่อน แล้วค่อยรัน server
CMD ["gunicorn", "--bind", ":8888", "mysite.wsgi:application"]