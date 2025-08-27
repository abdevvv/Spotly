# Use official Python image
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       gcc \
       libpq-dev \
       gdal-bin \
       binutils \
       libproj-dev \
       proj-data \
       proj-bin \
       libgeos-dev \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /code

# Install Python dependencies
COPY requirements.txt /code/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/
