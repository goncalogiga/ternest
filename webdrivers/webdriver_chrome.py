import os
from selenium import webdriver

import launch

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():

    try:
        browser = webdriver.Firefox()
        config = open("../user/config.txt","r")
        line = config.readline()
        browser.get(line[7:])

    except:
        browser.close()
        browser.quit()
        print(f"{bcolors.FAIL}Message: Failed to open the given url.{bcolors.ENDC}")

    launch.ernest(browser)

    browser.close()
    browser.quit()

if __name__== "__main__":
  main()
