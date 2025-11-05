# Rasa 공식 이미지 사용
FROM rasa/rasa:3.6.20-full

# 작업 디렉토리 설정
WORKDIR /app

# 프로젝트 복사
COPY . .

# 포트 노출 (Rasa 기본 포트)
EXPOSE 5005

# Rasa 서버 실행 (API + CORS 허용)
CMD ["rasa", "run", "--enable-api", "--cors", "*"]