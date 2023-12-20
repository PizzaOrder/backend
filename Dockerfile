FROM python:3.11

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="$PATH:/root/.local/bin"

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --only main

COPY . .

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

EXPOSE 80
