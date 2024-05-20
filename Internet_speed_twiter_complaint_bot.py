import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN=100
PROMISED_UP=10
X_EMAIL="YOUR EMAIL"
X_PASSWORD="YOUR PASSWORD"

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_experimental_option("detach", True)
        self.driver=webdriver.Chrome(chrome_option)
        self.down=25.34
        self.up=1.46

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        self.go=self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        self.go.click()
        time.sleep(60)
        self.down=self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        time.sleep(7)
        self.up=self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        time.sleep(7)
        print(self.down)
        print(self.up)

    def tweet_at_provider(self):
        self.driver.get(url="https://x.com/")
        time.sleep(10)
        self.sign_in=self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div/span/span')
        self.sign_in.click()
        time.sleep(7)
        self.email_input=self.driver.find_element(By.NAME,'text')
        self.email_input.send_keys(X_EMAIL)
        time.sleep(7)
        self.email_input.send_keys(Keys.ENTER)
        time.sleep(5)
        self.password_input=self.driver.find_element(By.NAME,'password')
        self.password_input.send_keys(X_PASSWORD)
        time.sleep(7)
        self.password_input.send_keys(Keys.ENTER)
        time.sleep(10)
        message=f"Hey Internet provider why my Internet speed is {self.down}down/{self.up}up,when i pay for {PROMISED_DOWN}down/{PROMISED_UP}up"
        self.compose_message=self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        self.compose_message.send_keys(message)
        time.sleep(5)
        self.tweet_button=self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        self.tweet_button.click()
bot=InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()



