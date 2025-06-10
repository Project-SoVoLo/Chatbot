# Python 기반 이미지
FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /app

# 코드 복사
COPY . /app

# 필요한 패키지 설치
RUN pip install --upgrade pip && pip install -r requirements.txt

# 포트 설정 & 실행
EXPOSE 8080
CMD ["python", "app.py"]