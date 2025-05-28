import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import google.generativeai as genai

# .env 로드
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

app = Flask(__name__)
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    chat_log = data.get("chatLog", "")
    prompt = f"""아래는 사용자가 챗봇과 나눈 상담 내용이야.
                다음 형식으로 요약해줘 (형식 꼭 맞춰서 응답해):
                
                형식: 날짜 | 대화 요약 | 챗봇 피드백 | 감정상태
                
                조건:
                - 날짜는 생략해도 돼
                - 감정상태는 '긍정' / '중립' / '부정' 중 하나로 꼭 작성해
                - '|' 로 구분된 정확히 4개의 항목으로 반환해
                
                내용:
                {chat_log}
                
                요약:
                """
    try:
        response = model.generate_content(prompt)
        return jsonify({"summary": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5001)