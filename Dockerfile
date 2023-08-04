FROM python:3.9

RUN mkdir -p /student_app

COPY . /student_app

RUN python3 -m pip install -r /student_app/requirements.txt

EXPOSE 5000

CMD ['python','/student_app/app.py']
