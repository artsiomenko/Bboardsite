from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Registration_User(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()

    def test_regictration_and_login(self):
        self.selenium.get(self.live_server_url + '')
        register = self.selenium.find_element(By.NAME, 'register')
        register.click()
        username = self.selenium.find_element(By.NAME, 'username')
        username.send_keys('Анжелика')
        email = self.selenium.find_element(By.NAME, 'email')
        email.send_keys('aya@anadeainc.com')
        password1 = self.selenium.find_element(By.NAME, 'password1')
        password1.send_keys('SavoskoSasha21')
        password2 = self.selenium.find_element(By.NAME, 'password2')
        password2.send_keys('SavoskoSasha21')
        first_name = self.selenium.find_element(By.NAME, 'first_name')
        first_name.send_keys('Анжелика')
        last_name = self.selenium.find_element(By.NAME, 'last_name')
        last_name.send_keys('Артеменко')
        registration_button = self.selenium.find_element(By.XPATH, '/html/body/div[2]/section/form/div[8]/button')
        registration_button.click()
        login = self.selenium.find_element(By.NAME, 'login')
        login.click()
        username = self.selenium.find_element(By.NAME, 'username')
        username.send_keys('Анжелика')
        password = self.selenium.find_element(By.NAME, 'password')
        password.send_keys('SavoskoSasha21')
        login_button = self.selenium.find_element(By.XPATH, '/html/body/div[2]/section/form/div[3]/button')
        login_button.click()
        assert 'Здравствуйте, Анжелика Артеменко!' in self.selenium.page_source

    def tearDown(self):
        self.selenium.quit()


