import logging
from modules.api_integrations.misskey_client import MisskeyClient
from modules.api_integrations.ai_client import AIClient

class BotCore:
    def __init__(self):
        self.logger = self._setup_logger()
        self.misskey_client = MisskeyClient()
        self.ai_client = AIClient(api_key="你的ai-apikey")
    
    def _setup_logger(self):
        """初始化日志记录器"""
        logger = logging.getLogger('misskey_bot')
        logger.setLevel(logging.INFO)
        
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        # 控制台输出
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        
        # 文件输出
        fh = logging.FileHandler('misskey_bot.log')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        
        return logger
    
    def generate_and_post(self):
        """生成内容并发布到Misskey"""
        try:
            generated_text = self.ai_client.schedule_random_generation()
            self.logger.info(f"生成的文本: {generated_text}")
            return self.misskey_client.post_note(generated_text)
        except Exception as e:
            self.logger.error(f"生成文本时出错: {str(e)}")
            raise