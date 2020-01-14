import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException

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

    url = ""

    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options,service_log_path=os.devnull)
    browser.set_page_load_timeout(3)

    try:
        config = open(os.path.expanduser("~/.ternest/user/config.txt"),"r")
    except:
         print(f"{bcolors.FAIL}Can't open config.txt.{bcolors.ENDC}")
         browser.quit()
         browser.close()
         config.close()
         exit()

    line = config.readlines()
    print("Opening Ernest and checking for new marks...")

    start_of_url = "https://wo.u-strasbg.fr/app/WebObjects/ResultatsExamens.woa/wa/rechercherEtudiant2?dateNaissance="
    url = start_of_url + line[0][16:-1] + "&codeEtudiant=" + line[1][15:-1] + "&entete=N"

    for i in range(4):
         try:
             browser.get(url)
             break

         except TimeoutException:
             continue

         except WebDriverException:
             i = 3
             break

         if i == 3:
             browser.close()
             browser.quit()
             config.close()
             print(f"{bcolors.FAIL}Connection failed.{bcolors.ENDC}")
             exit()

    config.close()
    launch.ernest(browser)

    browser.close()
    browser.quit()

if __name__== "__main__":
  main()
