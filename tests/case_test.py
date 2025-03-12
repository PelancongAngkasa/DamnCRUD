import unittest, os
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class TestDamnCRUD(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        option = webdriver.FirefoxOptions()
        option.add_argument('--headless')
        cls.browser = webdriver.Firefox(options=option)
        try:
            cls.url = os.environ['URL']
        except:
            cls.url = "http://localhost/DamnCRUD/src"

    def test_1_valid_creds(self):
        self.browser.get('http://localhost/DamnCRUD/login.php')
        expected_result = "Howdy, damn admin!"        
        self.browser.find_element(By.ID, "inputUsername").send_keys("admin")
        self.browser.find_element(By.ID, "inputPassword").send_keys("nimda666!")
        self.browser.find_element(By.XPATH, "//button[@type='submit']").click()
        actual_result = self.browser.find_element(By.XPATH, "//div[@class='container']/h2").text
        self.assertIn(expected_result, actual_result)

    def test_2_invalid_username(self):           
        self.browser.get('http://localhost/DamnCRUD/login.php')
        expected_result = "Damn, wrong credentials!!"
        self.browser.find_element(By.ID, "inputUsername").send_keys("invalid_user")
        self.browser.find_element(By.ID, "inputPassword").send_keys("nimda666!")
        self.browser.find_element(By.XPATH, "//button[@type='submit']").click()
        actual_result = self.browser.find_element(By.XPATH, "//div[@class='checkbox mb-3']/label").text
        self.assertIn(expected_result, actual_result)
        
    def test_3_invalid_password(self):
        self.browser.get('http://localhost/DamnCRUD/login.php')           
        expected_result = "Damn, wrong credentials!!"
        self.browser.find_element(By.ID, "inputUsername").send_keys("admin")
        self.browser.find_element(By.ID, "inputPassword").send_keys("invalid_password")
        self.browser.find_element(By.XPATH, "//button[@type='submit']").click()
        actual_result = self.browser.find_element(By.XPATH, "//div[@class='checkbox mb-3']/label").text
        self.assertIn(expected_result, actual_result)

    def wait_for_url(self, url, timeout=10):
        WebDriverWait(self.browser, timeout).until(
            lambda driver: driver.current_url == url
        )

    def test_4_add_contact(self):
        self.browser.get('http://localhost/DamnCRUD/create.php')
        expected_result = "PelancongAngkasa"
        self.browser.find_element(By.ID, "name").send_keys("PelancongAngkasa")
        self.browser.find_element(By.ID, "email").send_keys("pelancongangkasa@email.com")
        self.browser.find_element(By.ID, "phone").send_keys("08123456789")
        self.browser.find_element(By.ID, "title").send_keys("Attacker")
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/form/input[5]").click()
        try:
            actual_result = self.browser.find_element(By.XPATH, "//table[@id='employee']//td[contains(text(), 'PelancongAngkasa')]").text
        except:
        # Jika tidak ditemukan, klik tombol "Next" untuk ke halaman berikutnya
            try:
                self.browser.find_element(By.XPATH, '//*[@id="employee_next"]/a').click()
                actual_result = self.browser.find_element(By.XPATH, "//table[@id='employee']//td[contains(text(), 'PelancongAngkasa')]").text
            except:
                actual_result = ""

        self.assertIn(expected_result, actual_result)
    
    def test_5_sign_out(self):
        self.browser.get('http://localhost/DamnCRUD/index.php')  
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/a[3]").click()
        expected_url = 'http://localhost/DamnCRUD/login.php'
        actual_url = self.browser.current_url
        self.assertEqual(expected_url, actual_url)


    @classmethod
    def tearDownClass(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2,warnings='ignore') 