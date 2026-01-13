import google.generativeai as genai
from .. import config

def summarize_text(text):
    if not config.GEMINI_API_KEY:
        print("錯誤：找不到 API Key，請檢查 .env 文件")
        return None

    try:
        genai.configure(api_key=config.GEMINI_API_KEY)
        model = genai.GenerativeModel(config.GEMINI_MODEL_NAME)

        # 限制處理的文本長度
        text_to_summarize = text[:config.MAX_TEXT_CHUNK_SIZE]

        print(f"正在使用 Gemini ({config.GEMINI_MODEL_NAME}) 生成摘要...")
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