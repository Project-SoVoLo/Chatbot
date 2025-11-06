FROM rasa/rasa:3.6.20-full

WORKDIR /app
COPY . /app

# 모델/설정 디렉터리 보장 + 소유권을 컨테이너 기본 유저(1001)로
RUN mkdir -p /app/models /app/.config && chown -R 1001:1001 /app

# 가장 최신 모델을 latest.tar.gz 심볼릭 링크로 지정(없어도 에러 안 나게)
RUN bash -lc 'ls /app/models/*.tar.gz >/dev/null 2>&1 && ln -sf "$(ls -t /app/models/*.tar.gz | head -1)" /app/models/latest.tar.gz || true'

USER 1001
EXPOSE 5005
CMD ["rasa","run","--enable-api","--cors","*","--port","5005","--model","/app/models/latest.tar.gz"]
