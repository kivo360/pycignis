FROM ghcr.io/br3ndonland/inboard:fastapi

# Install Python requirements
COPY poetry.lock pyproject.toml /app/
WORKDIR /app/
RUN poetry install --no-dev --no-interaction --no-root

# Install Python app
COPY package /app/package
ENV APP_MODULE=package.main:app
# RUN command already included in base image
