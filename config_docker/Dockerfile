FROM ubuntu:latest

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Update package repository and install required packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip supervisor postgresql-client postgresql-server-dev-all gcc g++ \
    curl netcat nano

# Upgrade pip and install gunicorn
RUN pip3 install --upgrade pip && pip3 install gunicorn

# Create working directory
WORKDIR /home/app

# Copy requirements and install them
COPY ./requirements.txt /home/app/
RUN pip3 install -r requirements.txt

# Copy your application files
COPY ./ /home/app

# Copy Supervisor configuration files
COPY ./config_docker/supervisord.conf /etc/supervisor/conf.d/

# Make entrypoint scripts executable
RUN chmod +x /home/app/config_docker/entrypoint.sh
RUN chmod +x /home/app/config_docker/supervisor.sh