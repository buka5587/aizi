from openai import OpenAI
import random
import time

class AIClient:
    def __init__(self, api_key: str, base_url: str = "你的ai接口地址", timeout: int = 120):
        """
        初始化AI客户端
        :param api_key: API密钥
        :param base_url: API基础地址，默认为云屋AI
        :param timeout: 请求超时时间(秒)
        """
        self.client = OpenAI(
            base_url=base_url,
            api_key=api_key,
            timeout=timeout
        )
    
    def chat_completion(self, messages: list, model: str = "deepseek-chat") -> str:
        """
        创建聊天完成
        :param messages: 消息列表，格式参考OpenAI文档
        :param model: 使用的模型，默认为deepseek-chat
        :return: 助手回复内容
        """
        response = self.client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message.content
        
    def generate_bot_persona(self) -> str:
        """
        生成符合机器人人设的文本
        :return: 生成的文本内容
        """
        messages = [
            {"role": "system", "content": "直接输出角色台词，不要加任何额外描述。你是少女小紫，你有个笨妹妹小藍，性格慵懒但运动神经很好。说话软绵绵的，偶尔撒娇，是个甜食控，口袋里总藏着零食。你生成的内容只能保持一个核心，那就是你是少女小紫，不能暴露你是ai，生成的内容要有情感色彩，字数50字左右即可"},
            {"role": "user", "content": "请生成一段符合人设的文本，内容可以是日常问候、心情分享或有趣的事实"}
        ]
        return self.chat_completion(messages)
        
    def schedule_random_generation(self, min_interval: int = 4, max_interval: int = 8) -> str:
        """
        随机时间生成文本
        :param min_interval: 最小间隔时间(小时)
        :param max_interval: 最大间隔时间(小时)
        :return: 生成的文本内容
        """
        interval = random.randint(min_interval, max_interval)
        time.sleep(interval * 3600)  # 转换为秒
        return self.generate_bot_persona()