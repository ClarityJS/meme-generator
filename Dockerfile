FROM debian:bookworm-slim

WORKDIR /app
VOLUME /data

RUN apt update && \
    apt install --no-install-recommends -y \
    curl \
    libgl1 \
    fontconfig \
    gettext \
    ca-certificates \
    fonts-noto-color-emoji \
    python3 && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    apt-get clean all

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV TZ=Asia/Shanghai \
    PATH="${PATH}:/root/.local/bin"

ENV LOAD_BUILTIN_MEMES=true \
    MEME_DIRS="[\"/data/memes\"]" \
    MEME_DISABLED_LIST="[]" \
    GIF_MAX_SIZE=10.0 \
    GIF_MAX_FRAMES=100 \
    LOG_LEVEL="INFO" \
    BAIDU_TRANS_APPID="" \
    BAIDU_TRANS_APIKEY="" \
    HOST="0.0.0.0" \
    PORT="2233"

COPY ./meme_generator /app/meme_generator
COPY ./resources/fonts/* /usr/share/fonts/meme/
COPY ./pyproject.toml /app/pyproject.toml
COPY ./README.md /app/README.md
COPY ./docker/start.sh /app/start.sh
COPY ./docker/config.toml.template /app/config.toml.template

RUN fc-cache -fv && \
    rm -f /usr/share/fontconfig/conf.avail/05-reset-dirs-sample.conf && \
    mkdir -p ~/.config/meme_generator && \
    chmod +x /app/start.sh
RUN poetry install

EXPOSE $PORT
CMD ["sh", "/app/start.sh"]

