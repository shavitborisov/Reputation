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

DOWNLOAD_FOLDER_PATH = r'C:\Users\USER\Downloads'
BOT_PATH = r"C:\Users\USER\Desktop\tmp_hack\Reputation"


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
        time.sleep(0.2)
       
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
        photo_name = os.path.join(BOT_PATH, pic_path)

        add_something_button = self.driver.find_elements(By.CLASS_NAME, "_26lC3")[5]
        add_something_button.click()

        time.sleep(0.26)

        pic_and_vid_button =  self.driver.find_elements(By.CLASS_NAME, "_2t8DP")[0]
        #pic_and_vid_button.click()

        time.sleep(0.32)

        input_photo = pic_and_vid_button.find_elements(By.TAG_NAME, "input")[0]
        input_photo.send_keys(photo_name)

        time.sleep(1)

        send_pic = self.driver.find_elements(By.CLASS_NAME, "_1w1m1")[0]
        send_pic.click()

        time.sleep(1)

    def read_pic_and_message(self, save_path):
        message = self.stream_read()

        time.sleep(0.4)

        img = self.driver.find_elements(By.CLASS_NAME, "_1bJJV")[-1]
        img.click()

        time.sleep(0.3)

        down_button = self.driver.find_elements(By.CLASS_NAME, "_2cNrC")[3]
        down_button.click()

        time.sleep(0.3)

        close_button = self.driver.find_elements(By.CLASS_NAME, "_2cNrC")[4]
        close_button.click()

        files = glob.glob(DOWNLOAD_FOLDER_PATH + r"\*")
        max_file = max(files, key=os.path.getctime)

        shutil.copyfile(max_file, save_path)

        time.sleep(1)

        return message 

if __name__ == '__main__':
    pass