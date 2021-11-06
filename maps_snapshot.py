# maps_snapshot.py - a program to search strings from a list to Google Maps and automatically save screenshots/image files to a folder

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time


# CONSTANTS - your environment variables for chromedriver.exe
CHROMEDRIVER_PATH = os.environ.get("CHROMEDRIVER_EXECUTABLE")
# List of states/places in Malaysia
CONTENTS = ['Johor', 
            'Kedah', 
            'Kelantan', 
            'Kuala Lumpur', 
            'Malacca', 
            'Negeri Sembilan', 
            'Pahang', 
            'Penang', 
            'Perak', 
            'Perlis', 
            'Sabah', 
            'Sarawak', 
            'Selangor', 
            'Terengganu']


# #------------------WEBDRIVER CONFIGURATION----------------
def configure_chrome_driver():
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument("--incognito")
    # Removes listening message on terminal window
    chrome_option.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_option)
    driver.maximize_window()
    return driver


driver = configure_chrome_driver()


# #-------------------SAVE SCREENSHOT----------------
def save_screenshot(file_path):
    '''Saves the screenshots in a specific directory'''
    driver.save_screenshot(file_path)
    print(f"File saved: {file_path}")
    time.sleep(1)


#-----------------SEARCH STATES----------------
def search(list_items, directory):
    '''Loops thorugh input list to search for places in Google Maps'''

    # Google Maps URL
    url = "https://www.google.com.my/maps"
    driver.get(url)
    search_box = driver.find_element_by_xpath('//*[@id="searchboxinput"]')
    i = 0
    while (i < len(list_items)):
        # Loop through contents of list
        for item in list_items:
            search_box.send_keys(str(item))
            # Press enter
            search_box.send_keys(Keys.RETURN)
            driver.implicitly_wait(5)
            # Hide side pannel
            side_button = driver.find_element_by_xpath('//*[@id="pane"]/div/div[3]')
            side_button.click()
            time.sleep(2)
            # Take screenshots
            save_screenshot(f"{directory}/{item + '.png'}")
            side_button.click()
            search_box.clear()      
            i+=1
    print("\nDONE!")
    # Exit chromedriver
    driver.quit()
    # Open folder that contains saved images
    os.startfile(directory)
    return        

