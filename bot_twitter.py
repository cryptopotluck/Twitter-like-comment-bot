from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

coin = 'ethereum'
posts = [f'Theirs a lot of free trading tools on https://cryptopotluck.com/free that would help you watch {coin}', f'I use https://cryptopotluck.com/coins/ to stay up to date on {coin}',f'on the track we are headed we will be rich if we stick with {coin}', f'only down for {coin}', f'only up for {coin}', 'exciting times', 'trash', 'quality', 'You should post this on my forum I think my community would really dig your prospective. https://cryptopotluck.com/post','follow?', f'I\'m a little scared about the future of {coin}',f'pumped to see where {coin} goes from here', f'{coin}, time ;)', 'I really liked this', 'maybe you could elaborate more?', 'interesting', 'not bad', 'cool idea', 'Really awesome post', 'We share a similar prospective', 'cool tweet', 'I\'m digging it', '<3', 'bullish', 'bearish', 'FOMO', 'Fud', 'Fair', 'Not sure about this', 'moon', f'I\'m thinking the same thing about {coin}', f'{coin}, is totally bearish', f'{coin}, is totally bullish', 'ready to make some money', f'Really enjoy your prospective on {coin}, made a cool app that might help you research more. Check out https://cryptopotluck.com/coins/']

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()


    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get(f'https://twitter.com/search?q={hashtag}&src=typd')
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(3)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]
            for link in links:
                bot.get(f'https://twitter.com{link}')
                try:
                    bot.find_element_by_class_name('HeartAnimation').click()
                    form = bot.find_element_by_class_name('is-reply')
                    time.sleep(2)
                    form.click()
                    input_element = bot.find_element_by_css_selector(f"div[id='tweet-box-reply-to-{link[-19:]}")
                    time.sleep(2)
                    input_element.send_keys(random.choice(posts))
                    time.sleep(4)
                    input_element.send_keys(Keys.COMMAND, Keys.RETURN)
                    time.sleep(8)

                except Exception as ex:
                    time.sleep(60)



ed = TwitterBot('#add username', '#add password')
ed.login()
ed.like_tweet(coin)