FROM python:3.12

WORKDIR /app

COPY /src /app/src/
COPY /pages /app/pages/
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "/app/src/main_1.py"]