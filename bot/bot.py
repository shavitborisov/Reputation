# coding: utf-8
"""
Filename: streamable.py
About: Wraps a readable and writable stream
"""
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


WAIT_FOR_PHONE_CONNECTION = 15

class stream:
    driver = 0
   
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://web.whatsapp.com/")
        print("starting to wait")
        time.sleep(WAIT_FOR_PHONE_CONNECTION)
        print("done waiting!")
       
    def stream_write(self, string_to_write):
        element = self.driver.find_elements(By.CLASS_NAME, "_13NKt")[1] #TODO sometime smart
        element.send_keys(string_to_write)
        self.driver.find_element(By.CLASS_NAME,"_4sWnG").click()
       
    def stream_read(self):
        previous_text = self.driver.find_elements(By.CLASS_NAME, "i0jNr")[-1]
        #previous_num = self.driver.find_elements_by_class_name("_3zb-j")[-1]
        time.sleep(0.05)
        new_text = self.driver.find_elements(By.CLASS_NAME, "i0jNr")[-1]
        #new_num = self.driver.find_elements_by_class_name("_3zb-j")[-1]
       
        while previous_text == new_text:
            time.sleep(0.1)
            new_text = self.driver.find_elements(By.CLASS_NAME, "i0jNr")[-1]
            #new_num = self.driver.find_elements_by_class_name("_3zb-j")[-1]
       
        if previous_text != new_text:
            return new_text.text.strip()
           
        return new_num.text.strip()

if __name__ == '__main__':
    s = stream()
    s.stream_write((s.stream_read()))