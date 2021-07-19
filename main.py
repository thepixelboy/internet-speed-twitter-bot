import os
from selenium import webdriver
from dotenv import load_dotenv


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot(os.getenv("CHROME_DRIVER_PATH"))
bot.get_internet_speed()
bot.tweet_at_provider()
