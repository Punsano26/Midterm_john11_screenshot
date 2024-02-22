from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

class Test026(unittest.TestCase):
   
    def testcase01(self):
        self.driver = None
        self.driver = webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")
        self.driver.get("http://127.0.0.1/test-jhone11/026/testcase.html")
        
        first = self.driver.find_element(By.ID, "firstName")
        lastname = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")
        submit = self.driver.find_element(By.ID, "submit")
        
        first.send_keys("johnjohn")
        lastname.send_keys("cononc")
        age.send_keys("2")
        submit.click()
        result = self.driver.find_element(By.ID, "firstname").text
        self.assertEqual("First Name:johnjohn", result)
        
        self.driver.save_screenshot("pngtest/testjhone01.png")
        self.driver.close()
        
      
    def testcase02(self):
        self.driver = None
        self.driver = webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")
        self.driver.get("http://127.0.0.1/test-jhone11/026/testcase.html")
        
        first = self.driver.find_element(By.ID, "firstName")
        lastname = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")
        submit = self.driver.find_element(By.ID, "submit")
        
        first.send_keys("Johnj")
        lastname.send_keys("canoncanoncano")
        age.send_keys("149")
        submit.click()
        result = self.driver.find_element(By.ID, "firstname").text
        self.assertEqual("First Name:Johnj", result)
        
   
        self.driver.save_screenshot("pngtest/testjhone02.png")
        self.driver.close()
        
    def testcase03(self):
        self.driver = None
        self.driver = webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")
        self.driver.get("http://127.0.0.1/test-jhone11/026/testcase.html")
        
        first = self.driver.find_element(By.ID, "firstName")
        lastname = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")
        submit = self.driver.find_element(By.ID, "submit")
        
        first.send_keys("Johnjo")
        lastname.send_keys("canoncanoncanon")
        age.send_keys("150")
        submit.click()
        time.sleep(2)
        result = self.driver.find_element(By.ID, "firstname").text
        self.assertEqual("First Name:Johnjo", result)
        
      
        self.driver.save_screenshot("pngtest/testjhone03.png")
        self.driver.close()
     
    def testcase04(self):
        self.driver = None
        self.driver = webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")
        self.driver.get("http://127.0.0.1/test-jhone11/026/testcase.html")
        
        first = self.driver.find_element(By.ID, "firstName")
        lastname = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")
        submit = self.driver.find_element(By.ID, "submit")
        
        first.send_keys("Johnjohnjohnjo")
        lastname.send_keys("canoncan")
        age.send_keys("75")
        submit.click()
        time.sleep(2)
        result = self.driver.find_element(By.ID, "firstname").text
        self.assertEqual("First Name:Johnjohnjohnjo", result)
        
     
        self.driver.save_screenshot("pngtest/testjhone04.png")
        self.driver.close()
        self.driver.close()
       
    def testcase05(self):
        self.driver = None
        self.driver = webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")
        self.driver.get("http://127.0.0.1/test-jhone11/026/testcase.html")
        
        first = self.driver.find_element(By.ID, "firstName")
        lastname = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")
        submit = self.driver.find_element(By.ID, "submit")
        
        first.send_keys("Johnjohnjohnjoh")
        lastname.send_keys("canoncan")
        age.send_keys("75")
        submit.click()
        
        result = self.driver.find_element(By.ID, "firstname").text
        self.assertEqual("First Name:Johnjohnjohnjoh", result)
        

        self.driver.save_screenshot("pngtest/testjhone05.png")
        self.driver.close()

    def testcase06(self):
        self.driver = None
        self.driver = webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")
        self.driver.get("http://127.0.0.1/test-jhone11/026/testcase.html")
        
        first = self.driver.find_element(By.ID, "firstName")
        lastname = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")
        submit = self.driver.find_element(By.ID, "submit")
        
        first.send_keys("john")
        lastname.send_keys("canoncan")
        age.send_keys("75")
        submit.click()
        self.driver.save_screenshot("pngtest/testjhone06.png")
        result = self.driver.find_element(By.CLASS_NAME, "container").text
        self.assertEqual("Personal Information Form", result)
        
     
        
        self.driver.close()
      
    def testcase08(self):
        self.driver = None
        self.driver = webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")
        self.driver.get("http://127.0.0.1/test-jhone11/026/testcase.html")
        
        first = self.driver.find_element(By.ID, "firstName")
        lastname = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")
        submit = self.driver.find_element(By.ID, "submit")
        
        first.send_keys("Johnjohn")
        lastname.send_keys("cano")
        age.send_keys("75")
        submit.click()
        self.driver.save_screenshot("pngtest/testjhone08.png")
        result = self.driver.find_element(By.CLASS_NAME, "container").text
        self.assertEqual("Personal Information Form", result)
        

        
        self.driver.close()
  
    def testcase10(self):
        self.driver = None
        self.driver = webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")
        self.driver.get("http://127.0.0.1/test-jhone11/026/testcase.html")
        
        first = self.driver.find_element(By.ID, "firstName")
        lastname = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")
        submit = self.driver.find_element(By.ID, "submit")
        
        first.send_keys("Johnjohn")
        lastname.send_keys("canoncan")
        age.send_keys("0")
        submit.click()
        self.driver.save_screenshot("pngtest/testjhone10.png")
        result = self.driver.find_element(By.CLASS_NAME, "container").text
        self.assertEqual("Personal Information Form", result)
        
      
        
        self.driver.close()
     
    def testcase11(self):
        self.driver = None
        self.driver = webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")
        self.driver.get("http://127.0.0.1/test-jhone11/026/testcase.html")
        
        first = self.driver.find_element(By.ID, "firstName")
        lastname = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")
        submit = self.driver.find_element(By.ID, "submit")
        
        first.send_keys("Johnjohn")
        lastname.send_keys("canoncan")
        age.send_keys("151")
        submit.click()
        self.driver.save_screenshot("pngtest/testjhone11.png")
        result = self.driver.find_element(By.CLASS_NAME, "container").text
        self.assertEqual("Personal Information Form", result)
        
     
        
        self.driver.close()
      
if __name__ == "__main__":
    unittest.main()


