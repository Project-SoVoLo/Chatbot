FROM rasa/rasa:3.6.20-full

WORKDIR /app

# root로 전환해서 복사/권한 처리
USER root

# 프로젝트 복사하면서 소유주를 1001로 바로 맞춤
COPY --chown=1001:1001 . /app

# 디렉터리 보장 + 소유권 재확인 + latest 링크 생성(모델이 있으면)
RUN mkdir -p /app/models /app/.config \
 && chown -R 1001:1001 /app \
 && sh -lc 'latest=$(ls -t /app/models/*.tar.gz 2>/dev/null | grep -v "latest.tar.gz" | head -1 || true); [ -n "$latest" ] && ln -sf "$latest" /app/models/latest.tar.gz || true'

# 기본 유저로 복귀
USER 1001

EXPOSE 5005

# latest 링크가 있으면 그걸로 기동 (없어도 에러 안 남)
CMD ["run","--enable-api","--cors","*","--port","5005","--model","/app/models/latest.tar.gz"]
