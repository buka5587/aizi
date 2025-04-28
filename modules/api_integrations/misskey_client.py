import requests
from config import MisskeyConfig

class MisskeyClient:
    def __init__(self):
        self.config = MisskeyConfig()
        self.api_url = f"{self.config.site_url}/api/notes/create"
    
    def post_note(self, text: str) -> dict:
        """
        发布笔记到Misskey平台
        :param text: 要发布的文本内容
        :return: API响应结果
        """
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "i": self.config.account_token,
            "text": text
        }
        
        try:
            response = requests.post(self.api_url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"发布笔记失败: {e}")
            return {"error": str(e)}