# Python unit testing framework
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
# Appium Python client
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

# Open iOS simulator 11.2 and install TestApp
desired_caps = {
  "platformName": "iOS",
  "platformVersion": "15.1.1",
  "deviceName": "iPhone",
  "automationName": "XCUITest",
  "udid":"00008101-001A45520E01001E",
  "xcodeSigningId": "iPhone Developer",
  "xcodeOrgId": "373FXUUCZ6"
}

# Connect to Appium server on local host
driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)

# Test cases  
class Tests(unittest.TestCase):  
    #def setUp(self):
        
        # Enter first number
        #text1 = driver.find_element_by_accessibility_id("TextField1")
        #text1.click()
        #text1.send_keys("1")
        # Enter second number
        #text2 = driver.find_element_by_accessibility_id("TextField2")
        #text2.click()
        #text2.send_keys("1")
        # Compute sum
        #comp = driver.find_element_by_accessibility_id("ComputeSumButton")
        #comp.click()
        # Get answer
        #self.answer = driver.find_element_by_accessibility_id("Answer")

    def test_compute_sum(self): 
        el1 = driver.find_element_by_accessibility_id("Messages")
        el1.click()
        #el2 = driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name=\"OK\"]")
        #el2.click()
        el2 = driver.find_element_by_accessibility_id("composeButton")
        el2.click()
        driver.implicitly_wait(5000)
        el4 = driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Messages\"]/XCUIElementTypeWindow[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]")
        el4.click()
        el4.send_keys("3195405682")
        #el3 = driver.find_element_by_accessibility_id("2544190169")
        #el3.click()   
        #el3 = driver.find_element_by_accessibility_id("Galaxy")
        #el3.click()
        driver.implicitly_wait(5000)
        el3 = driver.find_element_by_accessibility_id("messageBodyField")
        el3.click()      
        driver.implicitly_wait(5000)
        el3.send_keys("QWERTYUIOPLKJHGFDSAZXCVBNM") 
        driver.implicitly_wait(5000)
        el4 = driver.find_element_by_accessibility_id("sendButton")
        el4.click()
        el3.send_keys("qwertyuiopasdfghjklzxcvbnm")
        el4.click()
        el3.send_keys("1234567890-/:;()$&@“.,?!’[]{}#%^*+=•¥£€><~|\_.,?!’")
        el4.click()  
        el3.send_keys("Ààśdfèwqžxç")
        el4.click()  
        #el3.send_keys("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way - in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only.")
        #driver.implicitly_wait(5000)
        #el4.click()

        #photo
        el3 = driver.find_element_by_accessibility_id("photoButton")
        el3.click()
        #el1 = driver.find_element_by_accessibility_id("FrontBackFacingCameraChooser")
        #el1.click()
        driver.implicitly_wait(50000)
        #driver.time.sleep(5000)
        #driver.WebDriverWait(driver, 1000)
        el1 = driver.find_element_by_accessibility_id("PhotoCapture")
        el1.click()
        driver.implicitly_wait(5000)
        el1 = driver.find_element_by_accessibility_id("Send")
        el1.click()

        #video
        driver.implicitly_wait(5000)
        el3 = driver.find_element_by_accessibility_id("photoButton")
        el3.click()
        driver.implicitly_wait(5000)
        #els4 = driver.find_element(By.xpath( "//*[@text='VIDEO']"))
        #els4[0].click()
        #el4 = driver.find_element_by_link_text("VIDEO").click()
        actions = TouchAction(driver)
        actions.tap(x=123, y=654).perform()
        
        #element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_accessibility_id("Frame rate"))
        #el2 = driver.find_element_by_accessibility_id("Frame rate")

        
        driver.implicitly_wait(5000)
        el1 = driver.find_element_by_accessibility_id("VideoCapture")
        actions.long_press(el1)
        actions.wait(5000)
        actions.release()
        actions.perform()
        driver.implicitly_wait(5000)
        
        #el1.click()
        
        #driver.pause(10)
        #driver.timeout().implicitly_wait(5000)
        #wait = WebDriverWait(driver, 5000)
        #time.sleep(5000)
        #actions= TouchAction(driver)
        #actions.wait(10000)
        #wait = WebDriverWait(driver, 30)
        #wait.until(EC.visibility_of_element_located(by.xpath("//android.widget.TextView[contains(@resource-id, '0:00:05')]")))
        #el2 = driver.find_element_by_accessibility_id("VideoCapture")
        #el2.click()
        #TouchAction(driver).tap(x=193, y=720).perform()
        #driver.implicitly_wait(5000)
        el1 = driver.find_element_by_accessibility_id("Send")
        el1.click()
        
        #back
        el3 = driver.find_element_by_xpath("//XCUIElementTypeNavigationBar[@name=\"CKChat\"]/XCUIElementTypeButton[1]")
        el3.click()
    #    self.assertEqual(self.answer.text, "2")
				
				#mdn2

        el2 = driver.find_element_by_accessibility_id("composeButton")
        el2.click()
        driver.implicitly_wait(5000)
        el4 = driver.find_element_by_xpath("//XCUIElementTypeApplication[@name=\"Messages\"]/XCUIElementTypeWindow[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]")
        el4.click()
        el4.send_keys("9132196572")
        #el3 = driver.find_element_by_accessibility_id("2544190169")
        #el3.click()   
        #el3 = driver.find_element_by_accessibility_id("Galaxy")
        #el3.click()
        driver.implicitly_wait(5000)
        el3 = driver.find_element_by_accessibility_id("messageBodyField")
        el3.click()      
        driver.implicitly_wait(5000)
        el3.send_keys("QWERTYUIOPLKJHGFDSAZXCVBNM") 
        driver.implicitly_wait(5000)
        el4 = driver.find_element_by_accessibility_id("sendButton")
        el4.click()
        el3.send_keys("qwertyuiopasdfghjklzxcvbnm")
        el4.click()
        el3.send_keys("1234567890-/:;()$&@“.,?!’[]{}#%^*+=•¥£€><~|\_.,?!’")
        el4.click()  
        el3.send_keys("Ààśdfèwqžxç")
        el4.click()  
        #el3.send_keys("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way - in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only.")
        #driver.implicitly_wait(5000)
        #el4.click()

        #photo
        el3 = driver.find_element_by_accessibility_id("photoButton")
        el3.click()
        #el1 = driver.find_element_by_accessibility_id("FrontBackFacingCameraChooser")
        #el1.click()
        driver.implicitly_wait(50000)
        #driver.time.sleep(5000)
        #driver.WebDriverWait(driver, 1000)
        actions.tap(x=267, y=658).perform()
        el1 = driver.find_element_by_accessibility_id("PhotoCapture")
        el1.click()
        driver.implicitly_wait(5000)
        el1 = driver.find_element_by_accessibility_id("Send")
        el1.click()

        #video
        driver.implicitly_wait(5000)
        el3 = driver.find_element_by_accessibility_id("photoButton")
        el3.click()
        driver.implicitly_wait(5000)
        #els4 = driver.find_element(By.xpath( "//*[@text='VIDEO']"))
        #els4[0].click()
        #el4 = driver.find_element_by_link_text("VIDEO").click()
        actions = TouchAction(driver)
        actions.tap(x=123, y=654).perform()
        
        #element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_accessibility_id("Frame rate"))
        #el2 = driver.find_element_by_accessibility_id("Frame rate")

        
        driver.implicitly_wait(5000)
        el1 = driver.find_element_by_accessibility_id("VideoCapture")
        actions.long_press(el1)
        actions.wait(5000)
        actions.release()
        actions.perform()
        driver.implicitly_wait(5000)
        
        #el1.click()
        
        #driver.pause(10)
        #driver.timeout().implicitly_wait(5000)
        #wait = WebDriverWait(driver, 5000)
        #time.sleep(5000)
        #actions= TouchAction(driver)
        #actions.wait(10000)
        #wait = WebDriverWait(driver, 30)
        #wait.until(EC.visibility_of_element_located(by.xpath("//android.widget.TextView[contains(@resource-id, '0:00:05')]")))
        #el2 = driver.find_element_by_accessibility_id("VideoCapture")
        #el2.click()
        #TouchAction(driver).tap(x=193, y=720).perform()
        #driver.implicitly_wait(5000)
        el1 = driver.find_element_by_accessibility_id("Send")
        el1.click()
        
        #back
        el3 = driver.find_element_by_xpath("//XCUIElementTypeNavigationBar[@name=\"CKChat\"]/XCUIElementTypeButton[1]")
        el3.click()
    #    self.assertEqual(self.answer.text, "2")  

    
# Run test cases  
unittest.main()   
