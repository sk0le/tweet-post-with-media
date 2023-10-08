from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
'''Uncomment the below line when running in linux'''
# from pyvirtualdisplay import Display
import time, os
 
class Twitterbot:
 
    def __init__(self, email, password):
 
        """Constructor
 
        Arguments:
            email {string} -- registered twitter email
            password {string} -- password for the twitter account
        """
 
        self.email = email
        self.password = password
 
        current_directory = os.getcwd()
        file_name = "driver/geckodriver.exe" 
        file_path = os.path.join(current_directory, file_name)

        self.bot = webdriver.Firefox(service=webdriver.firefox.service.Service(executable_path=file_path))
 
    def login(self):
        """
            Method for signing in the user 
            with the provided email and password.
        """

        try:
 
            bot = self.bot
            # fetches the login page
            bot.get('https://twitter.com/i/flow/login')
            # adjust the sleep time according to your internet speed
            time.sleep(3)
    
            usernameInput = bot.find_element("xpath", '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
            usernameInput.send_keys(self.email)
            time.sleep(2)
            usernameInput.send_keys(Keys.RETURN)
            time.sleep(2)
            passwordInput = bot.find_element("xpath", "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
            passwordInput.send_keys(self.password)
            time.sleep(2)
            passwordInput.send_keys(Keys.RETURN)

            print("Successfully logged into account.")
            return True
        
        except Exception as e:
            print("There has been some error.")
            print(e)
            return False
    
    def post_tweet(self, tweet_text, tweet_image):
        bot=self.bot

        print("Trying to tweet...")

        bot.get("https://twitter.com/compose/tweet")

        # button = bot.find_element("xpath", "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]")
        # button.click()
        time.sleep(4)

        input = bot.find_element("xpath", "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div")
        input.send_keys(tweet_text)
        time.sleep(2)

        image = bot.find_element("xpath", "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/input")
        image.send_keys(tweet_image)

        time.sleep(2)

        post = bot.find_element("xpath", "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]")
        post.click()

        print("Tweeted successfully.")
        time.sleep(5)
        bot.quit()

    