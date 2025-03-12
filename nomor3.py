import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.browser = webdriver.Firefox()

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
               
    def test_4_add_contact(self):
        self.browser.get('http://localhost/DamnCRUD/create.php')
         

    @classmethod
    def tearDownClass(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2,warnings='ignore') 