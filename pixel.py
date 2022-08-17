# pitching machine for android msg app. witten by Jason Yoon. 07/09/2021
# Android environment
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains

desired_caps = {
    "platformName" : "Android",
    "platformVersion" :"12",
    "automationName" : "uiautomator2",
    "deviceName" :"pixel"
}

wait_duration = 5000
#driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
mdn1 = '3195405682\\n'
mdn2 = '9132196572\\n'
mdn3 = '2548569735\\n'
mdn4 = '9728802159\\n'

def open_msg_thread(mdn):
    el1 = driver.find_element_by_accessibility_id("Messages")
    el1.click()

    driver.implicitly_wait(wait_duration)
    el7 = driver.find_element_by_accessibility_id('Start chat')
    el7.click()

    driver.implicitly_wait(wait_duration)
    el8 = driver.find_element_by_id('com.google.android.apps.messaging:id/recipient_text_view')
    el8.click()

    driver.implicitly_wait(wait_duration)
    el9 = driver.find_element_by_id('com.google.android.apps.messaging:id/recipient_text_view')
    el9.send_keys(mdn)
    

    driver.implicitly_wait(wait_duration)
    el10 = driver.find_element_by_id('com.google.android.apps.messaging:id/compose_message_text')


def send_text():
    driver.implicitly_wait(wait_duration)
    el7 = driver.find_element_by_id("com.google.android.apps.messaging:id/compose_message_text")
    el7.send_keys("QWERTYUIOPASDFGHJKLZXCVBNM")

    driver.implicitly_wait(wait_duration)
    el8 = driver.find_element_by_id("com.google.android.apps.messaging:id/send_message_button_icon")
    el8.click()

    el7.send_keys("qwertyuiopasdfghjklzxcvbnm")
    el8.click()

    el7.send_keys("ññññññññññ")
    el8.click()

    el7.send_keys("Á, Â, Ã, È, É, Ï, Ñ, Ö")
    el8.click()

    el7.send_keys("+×÷=/_<>[]!@#$%^&*()-':;,?`~\|€£¥₩°•○●□■♤♡◇♧☆▪¤《》¡¿,.")
    el8.click()

    el7.send_keys("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way - in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only.")
    el8.click()

def send_picture():
    driver.implicitly_wait(wait_duration)
    el19 = driver.find_element_by_accessibility_id("Attach from camera or gallery")
    el19.click()

    driver.implicitly_wait(wait_duration)
    el9 = driver.find_element_by_accessibility_id("Switch to full screen camera")
    el9.click()

#driver.implicitly_wait(wait_duration)
#el3 = driver.find_element_by_accessibility_id("Front camera switch")
#el3.click()

    actions = TouchAction(driver)
    actions.wait(wait_duration)

    driver.implicitly_wait(wait_duration)
    el2 = driver.find_element_by_id("com.google.android.apps.messaging:id/shutter_button_ring")
    driver.implicitly_wait(wait_duration)
    el2.click()

    driver.implicitly_wait(wait_duration)
    el3 = driver.find_element_by_accessibility_id("Attach to Message")
    el3.click()

    driver.implicitly_wait(wait_duration)
    el4 = driver.find_element_by_id("com.google.android.apps.messaging:id/send_message_button_icon")
    el4.click()
    
def send_video():
    driver.implicitly_wait(wait_duration)
    el3 = driver.find_element_by_accessibility_id("Switch to full screen camera")
    el3.click()

#efdf2dbb-256c-41d4-9de8-247686d21231

#driver.implicitly_wait(wait_duration)
#el2 = driver.find_elements_by_xpath("//*[@text='Record video']")[0]
#el2.click()

    el4 = driver.find_element_by_accessibility_id("Video mode")
    el4.click()

    driver.implicitly_wait(wait_duration)
    el5 = driver.find_element_by_accessibility_id("Start recording video")
    actions = TouchAction(driver)
    actions.long_press(el5)
    actions.wait(wait_duration)
    actions.release()
    actions.perform()
    driver.implicitly_wait(wait_duration)

#    actions = TouchAction(driver)
#    actions.wait(wait_duration)

#driver.implicitly_wait(wait_duration)
#el1 = driver.find_element_by_id("com.sec.android.app.camera:id/stop_button_icon")
#el1.click()

#driver.implicitly_wait(wait_duration)
#els4 = driver.find_elements_by_xpath("//*[@text='OK']")
#els4[0].click()
#driver.implicitly_wait(5)
#el5 = driver.find_element_by_accessibility_id("Start recording video")
#el5.click()
    driver.implicitly_wait(6000)
    el8 = driver.find_element_by_accessibility_id("Attach to Message")
    el8.click()
    el9 = driver.find_element_by_id("com.google.android.apps.messaging:id/send_message_button_icon")
    el9.click()


def send_audio():
    el1 = driver.find_element_by_id("com.google.android.apps.messaging:id/audio_button_view_microphone_icon")
    actions = TouchAction(driver)
    actions.long_press(el1)
    actions.wait(wait_duration)
    actions.release()
    actions.perform()
    driver.implicitly_wait(wait_duration)
    el4 = driver.find_element_by_id("com.google.android.apps.messaging:id/send_message_button_icon")
    el4.click()

###UI changed 12/2/2021

#el6 = driver.find_element_by_xpath("//android.view.ViewGroup[@content-desc=\"Location\"]/android.widget.ImageView")
#el6.click()
#el7 = driver.find_element_by_xpath("//android.view.ViewGroup[@content-desc=\"Contacts\"]/android.widget.TextView")
#el7.click()
def send_locations():


    driver.implicitly_wait(wait_duration)
    el0 = driver.find_element_by_id("com.google.android.apps.messaging:id/plus_button")
    el0.click()
#driver.implicitly_wait(wait_duration)
#el1 = driver.find_element_by_accessibility_id("Share a location")
#el1.click()

    el6 = driver.find_element_by_xpath("//android.view.ViewGroup[@content-desc=\"Location\"]/android.widget.ImageView")
    el6.click()

#el1 = driver.find_element_by_id("com.google.android.apps.messaging:id/location_category_permission_view")
#el1.click()
#el2 = driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_foreground_only_button")
#el2.click()
#driver.implicitly_wait(5)
#el3 = driver.find_element_by_id("com.google.android.apps.messaging:id/location_content_category_view")
#el3.click()

    el1 = driver.find_element_by_accessibility_id("Search")
    el1.click()
    el2 = driver.find_element_by_id("com.google.android.apps.messaging:id/search_src_text")
    el2.send_keys("6625 Excellence Way")
    driver.implicitly_wait(wait_duration)
    el3 = driver.find_element_by_id("com.google.android.apps.messaging:id/search_result_name")
    el3.click()

    driver.implicitly_wait(wait_duration)
    el4 = driver.find_element_by_id("com.google.android.apps.messaging:id/select_location_bar_send_icon_container")
    el4.click()
    
def send_contacts():
#driver.implicitly_wait(wait_duration)
#actions = TouchAction(driver)
#actions.press(x=119, y=1931)  
#actions.wait(1000) 
#actions.move_to(x=156, y=1001)   
#actions.release()   
#actions.perform()

#driver.implicitly_wait(wait_duration)
#el1 = driver.find_element_by_accessibility_id("Tap to share a contact")
#el1.click()
    el7 = driver.find_element_by_xpath("//android.view.ViewGroup[@content-desc=\"Contacts\"]/android.widget.TextView")
    el7.click()

    el1 = driver.find_element_by_accessibility_id("Search contacts")
    el1.click()
#els2 = driver.find_elements_by_xpath("//*[@text='File']")
#els2[0].click()
    el2 = driver.find_element_by_id("com.google.android.contacts:id/search_view")
    el2.send_keys("test")
#el1 = driver.find_element_by_id("com.samsung.android.app.contacts:id/search_src_text")
#el1.send_keys("test")
    el2 = driver.find_element_by_accessibility_id("Test")
    el2.click()
    el4 = driver.find_element_by_id("com.google.android.apps.messaging:id/send_message_button_icon")
    el4.click()

################################################



open_msg_thread(mdn1)
send_text()
send_picture()
send_video()
send_audio()
send_locations()
send_contacts()

#exit app
driver.back()
driver.back()
driver.back()



##########################



open_msg_thread(mdn2)
send_text()
send_picture()
send_video()
send_audio()
send_locations()
send_contacts()

#exit app
driver.back()
driver.back()
driver.back()







