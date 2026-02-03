FROM python:3.12-slim  

RUN python -m venv /venv  
ENV PATH="/venv/bin:$PATH"  

RUN pip install "django<6"
COPY . /src  

WORKDIR /src  

CMD ["/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8888"]