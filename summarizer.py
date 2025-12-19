import os
import google.generativeai as genai
from dotenv import load_dotenv

def summarize_text(text):
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("錯誤：找不到 API Key")
        return None

    try:
        genai.configure(api_key=api_key)
        
        # 使用您环境中可用的、正确的免费模型 gemini-flash-latest
        model = genai.GenerativeModel('gemini-flash-latest')

        # 限制處理的文本長度
        max_chunk_size = 15000
        text_to_summarize = text[:max_chunk_size]

        print("正在使用 Gemini (gemini-flash-latest) 生成摘要...")
        response = model.generate_content(
            f"請為以下內容提供簡潔的書評摘要：\n\n{text_to_summarize}"
        )
        
        if response.parts:
            return response.text
        else:
            print("警告：模型沒有返回任何內容。可能是因為安全限制或输入问题。")
            return None

    except Exception as e:
        print(f"調用 Gemini API 時發生錯誤：{e}")
        return None