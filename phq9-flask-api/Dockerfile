# 1) 베이스 이미지
FROM python:3.10-slim

# 2 ) 작업 디렉토리 설정
WORKDIR /app

# 3 ) 의존성 설치
COPY requirements.txt .
RUN pip install --default-timeout=120 --no-cache-dir -r requirements.txt

# 4 ) 나머지 소스 복사
COPY . .

# 5 ) 개발 서버 포트 5050
EXPOSE 5050

# 6 ) phq-9 모델 서버 실행
CMD ["python", "app.py"]