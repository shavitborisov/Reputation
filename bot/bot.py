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
import os.path
import glob
import shutil

DOWNLOAD_FOLDER_PATH = r'C:\Users\USER\Downloads\*'

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

    def send_pic(self, pic_path):
        pass

    def read_pic_and_message(self, save_path):
        message = self.stream_read()

        img = self.driver.find_elements(By.CLASS_NAME, "_3IfUe")[-1]
        img.click()

        time.sleep(0.3)

        down_button = self.driver.find_elements(By.CLASS_NAME, "_2cNrC")[3]
        down_button.click()

        time.sleep(0.3)

        close_button = self.driver.find_elements(By.CLASS_NAME, "_2cNrC")[4]
        close_button.click()

        files = glob.glob(DOWNLOAD_FOLDER_PATH)
        max_file = max(files, key=os.path.getctime)

        shutil.copyfile(max_file, save_path)

        return message 

if __name__ == '__main__':
    s = stream()
    print(s.read_pic_and_message("bla.jpg"))