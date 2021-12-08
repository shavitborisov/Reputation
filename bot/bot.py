# coding: utf-8
"""
Filename: streamable.py
About: Wraps a readable and writable stream
"""
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

WAIT_FOR_PHONE_CONNECTION = 10

class stream:
    driver = 0
   
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://web.whatsapp.com/")
        print("starting to wait")
        time.sleep(WAIT_FOR_PHONE_CONNECTION)
        print("done waiting!")
       
    def stream_write(self, string_to_write):
        element = self.driver.find_element_by_class_name("_2S1VP")
        element.send_keys(string_to_write)
        self.driver.find_element_by_class_name("_35EW6").click()
       
    def stream_read(self):
        previous_text = self.driver.find_elements_by_class_name("XELVh")[-1]
        previous_num = self.driver.find_elements_by_class_name("_3zb-j")[-1]
        time.sleep(0.05)
        new_text = self.driver.find_elements_by_class_name("XELVh")[-1]
        new_num = self.driver.find_elements_by_class_name("_3zb-j")[-1]
       
        while previous_text == new_text and previous_num == new_num:
            time.sleep(0.1)
            new_text = self.driver.find_elements_by_class_name("XELVh")[-1]
            new_num = self.driver.find_elements_by_class_name("_3zb-j")[-1]
       
        if previous_text != new_text:
            return new_text.text.strip()
           
        return new_num.text.strip() 


if __name__ == '__main__':
    s = stream()
    s.stream_write("Hello")