from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import json

class EasyApplyLinkedin:
    def __init__(self,data):
        """This section contains data from config.json"""
        self.your_login = data['email']
        self.your_password = data['password']
        self.keywords = data['keywords']
        self.location = data['location']
        self.telephone_number = data['telephone_number']
        self.driver = webdriver.Chrome(executable_path=data['driver_path']) 
        
    def login_linkedin(self):
        """This section makes sign in into linkedin"""
        self.driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
        cookie_accept_button = self.driver.find_element(By.CLASS_NAME, value="artdeco-global-alert-action")
        cookie_accept_button.click()
        time.sleep(5)
        username_field = self.driver.find_element(By.ID, value="username")
        password_field = self.driver.find_element(By.ID, value="password")
        username_field.send_keys(self.your_login)
        password_field.send_keys(self.your_password)
        password_field.send_keys(Keys.ENTER)
    def find_job(self):
        """This section goes into jobs section and search for the job and location from our given data """
        making_msg_small = self.driver.find_element(By.CLASS_NAME, value="msg-overlay-bubble-header__details")
        making_msg_small.click()
        jobs_section = self.driver.find_element(By.XPATH, value='//*[@id="global-nav"]/div/nav/ul/li[3]/a')
        jobs_section.click()
        time.sleep(5)
        job_search_field = self.driver.find_element(By.CSS_SELECTOR, value='.jobs-search-box__container .jobs-search-box__input .jobs-search-box__inner .relative .jobs-search-box__text-input')
        job_search_field.send_keys(self.keywords)
        time.sleep(5)
        job_search_field.send_keys(Keys.ENTER)
        time.sleep(5)
        job_location_field = self.driver.find_element(By.XPATH, value="//input[@aria-label='City, state, or zip code']")
        job_location_field.clear()
        time.sleep(2)
        job_location_field.send_keys(self.location)
        job_location_field.send_keys(Keys.ENTER)

    def filter(self):
        """This section filter found jobs as per having easy apply """
        easy_apply = self.driver.find_element(By.XPATH, value="//button[@aria-label='Easy Apply filter.']")
        easy_apply.click()

    def ignore_application(self):
        ignore = self.driver.find_element(By.CLASS_NAME, value="mercado-match")
        ignore.click()
        time.sleep(2)
        discard = self.driver.find_element(By.XPATH, value="//button[@data-control-name='discard_application_confirm_btn']").click()
    def apply_all_jobs(self):
        all_related_jobs = self.driver.find_elements(By.CLASS_NAME, value="job-card-container")

        for job in all_related_jobs:
            
            job.click()
            time.sleep(3)

            apply = self.driver.find_element(By.CLASS_NAME, value="jobs-apply-button")
            apply.click()
            time.sleep(3)

            submit_button = self.driver.find_element(By.CSS_SELECTOR, value="footer button")
            phone = self.driver.find_element(By.CLASS_NAME, value="fb-single-line-text__input")
            
            if submit_button.get_attribute('aria-label') == "Continue to next step": 
                    self.ignore_application()
            else:
                phone.clear()
                time.sleep(2)
                phone.send_keys(self.telephone_number)
                submit_application = self.driver.find_element(By.XPATH, value="//button[@aria-label='Submit application']")
                print(submit_application.text) 
                self.ignore_application()
                
            time.sleep(3)
            
if __name__ == "__main__":
    with open("config.json") as config_file:
        data = json.load(config_file)

    bot = EasyApplyLinkedin(data)
    bot.login_linkedin()
    time.sleep(10)
    bot.find_job()
    time.sleep(8)
    bot.filter()
    time.sleep(5)
    bot.apply_all_jobs()





