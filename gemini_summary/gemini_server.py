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
                이 내용을 기반으로 다음 정보를 요약해서 정리해줘:

                - 날짜 (없으면 생략 가능)
                - 대화 요약 (한두 줄)
                - 감정 상태 (긍정/중립/부정)
                - 챗봇의 피드백 요지 
                내용:
                \n\n{chat_log}\n\n 
                요약:"""
    try:
        response = model.generate_content(prompt)
        return jsonify({"summary": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5001)