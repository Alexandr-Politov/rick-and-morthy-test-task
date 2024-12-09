FROM python:3.12
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code

# Install the application dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy in the source code
COPY . /code/
