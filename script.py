
import os
import google.generativeai as genai
from dotenv import load_dotenv

# 從 .env 檔案載入環境變數
load_dotenv()

try:
    # 設定 API 金鑰
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "請在這裡貼上您真實的API金鑰":
        print("錯誤：請在 .env 檔案中設定您的 GEMINI_API_KEY。")
    else:
        genai.configure(api_key=api_key)

        # 建立模型
        model = genai.GenerativeModel('gemini-1.5-flash')

        # 準備提示
        prompt = "Explain how AI works in a few words"
        print(f"正在向 Gemini 發送提示：'{prompt}'")

        # 產生內容
        response = model.generate_content(prompt)

        # 列印結果
        print("\nGemini 的回覆：")
        print(response.text)
        print("\n驗證成功！您的 API 金鑰可以正常使用。")

except Exception as e:
    print(f"\n發生錯誤：{e}")
    print("驗證失敗。請檢查您的 API 金鑰是否正確，以及網路連線是否正常。")

