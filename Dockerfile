FROM python:3.10-slim

# Install required system packages
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && apt-get clean

RUN apt-get update && apt-get install -y \
    libsentencepiece-dev \
    && apt-get clean

# Install Poetry
# Install Poetry and configure it
RUN pip install poetry \
    && poetry config virtualenvs.in-project true

# Set up working directory
WORKDIR /app

RUN pip install --upgrade pip
# Pre-install torch manually with pip
RUN pip install torch==2.5.1

# Copy dependency files and install dependencies
COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-root

# Copy the rest of the application code
COPY . /app/

# Run the application
# CMD ["poetry", "run", "python", "app/queue_listener.py"]
CMD ["poetry", "run", "python", "app/queue_listener.py"]
