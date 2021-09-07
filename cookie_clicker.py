import math
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from apscheduler.schedulers.background import BackgroundScheduler

class CookieClicker():
    def __init__(self):
        self.driver = webdriver.Chrome("/Users/phedayat/Desktop/sel_cookie/chromedriver")
        self.driver.get("https://orteil.dashnet.org/cookieclicker/")
        cookie_wait = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "bigCookie")))
        
        self.cookie = self.driver.find_element_by_id("bigCookie")
        self.scheduler = BackgroundScheduler()
        self.cookie_count = 0

        self.init_clicker()

    def init_clicker(self):
        self.scheduler.add_job(self.product_click, 'interval', id='product_click', seconds=3)
        self.scheduler.add_job(self.upgrade_click, 'interval', id='upgrade_click', seconds=15)
        self.scheduler.start()
        self.rapid_click(1000)

    def shutdown_clicker(self):
        self.scheduler.shutdown()
        self.driver.close()

    def rapid_click(self, n):
        self.scheduler.pause_job('product_click')
        self.scheduler.pause_job('upgrade_click')
        for i in range(n):
            self.cookie.click()
            self.cookie.click()
            self.cookie.click()
            sleep(.0005)
        self.scheduler.resume_job('product_click')
        self.scheduler.resume_job('upgrade_click')

    def get_cookie_count(self):
        x = int(float(self.driver.find_element_by_xpath("//*[@id='cookies']").text.split(" ")[0]))
        return x

    def product_click(self):
        xpath = "//*[@id='products']/*[@class='product unlocked enabled']"
        products = self.driver.find_elements_by_xpath(xpath)
        products.reverse()
        for p in products:
            try:
                pt = p.text.split(" ")
                if pt[1] <= self.get_cookie_count():
                    p.click()
            except:
                print("Exception occurred (products)")
            # pl = p.text.split("\n")
            # buy_count = math.floor(self.get_cookie_count() / int(pl[1]))
            # for i in range(buy_count):
            #     p.click()

    def upgrade_click(self):
        xpath = "//*[@id='upgrades']/*[@class='crate upgrade enabled']"
        upgrades = self.driver.find_elements_by_xpath(xpath)
        for u in upgrades:
            try:
                u.click()
            except:
                print("Exception occurred (upgrade)")

if __name__ == "__main__":
    c = CookieClicker()
    r = input("Command: ")
    while r != "q":
        r = input("Command: ")
        args = r.split(" ")
        if args[0] == "r":
            c.rapid_click(int(args[1]))
    input("wait")
    c.shutdown_clicker()
