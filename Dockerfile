FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

COPY pyproject.toml uv.lock README.md ./
RUN uv sync --frozen --no-install-project

COPY src src
COPY api api
RUN uv sync --frozen

ENV PATH="/app/.venv/bin:$PATH"

CMD streamlit run api/main.py --server.address=0.0.0.0 --server.port=$PORT
