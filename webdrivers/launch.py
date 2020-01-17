import os
from selenium import webdriver

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def create_marks(browser):

    f = open(os.path.expanduser("~/.ternest/user/your_marks.txt"), "w");
    marks_class = browser.find_elements_by_class_name("elp3")

    prev_ue = ""

    for marks_tag in marks_class:

        marks_line = marks_tag.find_elements_by_tag_name("td")

        if marks_line[1].text != prev_ue:
            f.write(" \n")
            f.write("#:# ")
            f.write(marks_line[1].text[4:])
            f.write(" #:#")
            f.write("\n")

        for i in range(3):
            if i == 0:
                f.write(marks_line[i].text[:-11])
                f.write(": ")
            if i == 2:
                f.write(marks_line[i].text)

        f.write("\n")
        prev_ue = marks_line[1].text

    f.close()

def check_for_new_marks(browser):

    count = 0
    mark_numerical = 0.0
    prev_marks_elements=[]

    try:
        prev_marks = open(os.path.expanduser("~/.ternest/user/your_marks.txt"), "r");
    except:
        browser.close()
        browser.quit()
        config.close()
        print(f"{bcolors.FAIL}Failed to open 'your_marks.txt'.{bcolors.ENDC}")
        exit()

    lines = prev_marks.readlines()

    for x in lines:
        if len(x) > 2:
            prev_marks_elements.append(x.split(':'))
    prev_marks.close()

    new_marks = open(os.path.expanduser("~/.ternest/cache/new_marks.txt"), "w");

    marks_class = browser.find_elements_by_class_name("elp3")

    prev_ue , counter , el_index = "" , 0 , 0

    for marks_tag in marks_class:

        marks_line = marks_tag.find_elements_by_tag_name("td")

        if prev_marks_elements[el_index][0] == '#':
            el_index += 1

        if(len(marks_line[2].text) != 0
            and marks_line[2].text.replace(" ", "")
            != prev_marks_elements[el_index][1][:12].replace(" ", "").replace("\n",""))
            and len(marks_line[2].text.replace(" ", "")) < 9):

            new_marks.write(marks_line[0].text[:-11])
            new_marks.write(": ")
            new_marks.write(marks_line[2].text)

            new_marks.write("\n")

            count += 1

        el_index += 1

    prev_marks.close()
    new_marks.close()

    return count

def ernest(browser):

    count = -1

    try:
        new_marks = open(os.path.expanduser("~/.ternest/cache/new_marks.txt"), "r");
    except:
        browser.close()
        browser.quit()
        print(f"{bcolors.FAIL}Failed to open 'new_marks.txt'.{bcolors.ENDC}")
        exit()

    download_blocks = browser.find_elements_by_class_name("neutral")

    if( len(download_blocks) == 0):
        browser.close()
        browser.quit()
        print(f"{bcolors.WARNING}Timeout or Incorect login.{bcolors.ENDC}")
        exit()

    block = download_blocks[0]
    elements = block.find_elements_by_tag_name("a")

    if( len(elements) == 0):
        browser.close()
        browser.quit()
        print(f"{bcolors.WARNING}Incorect login.{bcolors.ENDC}")
        exit()

    try:
        browser.get(elements[0].get_attribute("href"))
    except:
        browser.close()
        browser.quit()
        print(f"{bcolors.WARNING}Incorect login.{bcolors.ENDC}")
        exit()

    if(os.stat(os.path.expanduser("~/.ternest/user/your_marks.txt")).st_size):
        count = check_for_new_marks(browser)
    create_marks(browser)

    if( count == -1):
        print('Sucessfuly loaded all your marks.')
        print('Use ternest --show=all to see them or launch ternest again to check for new ones.')
    elif( count == 0):
        print('No new marks were added to Ernest.')
    elif(count == 1):
        print('Since you last used ternest, 1 new mark was added in:')
    else:
        print('Since you last used ternest, {:d} new marks were added in:'.format(count))

    if(count > 0):
        lines = new_marks.readlines()
        for line in lines:
            print('-> {:s}'.format(line.split(':')[0]), end='')

            mark_numerical = float(line.split(':')[1][:4])
            if mark_numerical < 5.0:
                print("     (you really fucked this one up)")
            elif mark_numerical < 7.0:
                print("     (warning: it's quite shit)")
            elif mark_numerical < 10.0:
                print("     (watch out, it's not great...)")
            elif mark_numerical > 10.0:
                print("     (the mark is ok, don't worry)")
            elif mark_numerical > 14.0:
                print("     (this is good stuff !!)")
            else:
                print("     (Unrecognized numerical value. This might be a bug.)")

        print('Use ternest --show=new to see your new marks.')

    new_marks.close()

if __name__== "__main__":
  main()
