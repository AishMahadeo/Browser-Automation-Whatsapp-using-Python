from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os

def sentmessage(target,n,message):
    target = f'"{target}"'
    wait = WebDriverWait(browser,600)
    path = '//span[contains(@title,'+target+')]'
    ftarget = wait.until(EC.presence_of_element_located((By.XPATH,path)))
    ftarget.click()
    sleep(3)
    input_whatsapp = browser.find_element_by_class_name("_2A8P4")
    for i in range(n):
        input_whatsapp.send_keys(message,Keys.ENTER)

        
def sendmedia(target,file_path,n):
    target = f'"{target}"'
    wait = WebDriverWait(browser,600)
    path = '//span[contains(@title,'+target+')]'
    ftarget = wait.until(EC.presence_of_element_located((By.XPATH,path)))
    ftarget.click()
    for i in range(n):
        sleep(3)
        attach = browser.find_element_by_xpath('//div[@title = "Attach"]')
        attach.click()
        media = browser.find_element_by_xpath('//input[@accept = "image/*,video/mp4,video/3gpp,video/quicktime" ]')
        media.send_keys(file_path)
        sleep(3)
        send_btn = browser.find_element_by_xpath('//span[@data-icon="send"]')
        send_btn.click()

        
browser = webdriver.Chrome("C:/Users/Hrutik/Documents/PYTHON/chromedriver")
browser.get("https://web.whatsapp.com/")
print("scan the qr code to open whatsapp")
choice1 = input("Do you want to send the message:(y/n) ")
if choice1 == 'y' or choice1 == 'Y':
    target = input("Enter Name of your friend: ")
    message = input("enter message : ")
    n = int(input("enter number of times you want to send a message : "))
    sentmessage(target,n,message)

choice2 = input("Do you want to send the media file: (y/n) ")
if choice2 == 'y'or choice2 =='Y':
    target = input("Enter Name of your friend: ")
    file_path = input("Enter file path: ")
    n = int(input("enter number of times you want to send this message : "))
    assert os.path.exists(file_path),"Path error"
    file = open(file_path)
    sendmedia(target,file.name,n)
