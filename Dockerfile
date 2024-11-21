FROM python:3.12-slim

WORKDIR /src

COPY pyproject.toml poetry.lock ./

RUN apt-get update && rm -rf /var/lib/apt/lists
RUN pip install poetry --no-cache-dir
RUN poetry env use python3.12
RUN poetry install --no-dev

COPY ./start.sh ./
COPY ./src ./src

EXPOSE 8000
RUN chmod +x ./start.sh
CMD ["./start.sh"]
