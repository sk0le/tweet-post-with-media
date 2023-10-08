import time
import twitterbot as tb

bot = tb.Twitterbot("@123ad2336377", "rubikovakocka")
# logging in
bot.login()

time.sleep(5)

bot.post_tweet("Testing", "C:\\Users\\amel.islamovic_bbm\\Downloads\\Rectangle 30.png")