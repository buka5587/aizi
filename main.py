from bot_core import BotCore

if __name__ == "__main__":
    bot = BotCore()
    while True:
        try:
            bot.generate_and_post()
        except KeyboardInterrupt:
            bot.logger.info("Misskey机器人正常退出")
            break
        except Exception as e:
            bot.logger.error(f"机器人运行出错: {str(e)}")