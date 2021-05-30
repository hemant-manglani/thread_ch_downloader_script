# Import Module
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import shutil

user_name = '@TheHatedOne'
password = '@TheHatedOne'

# file_links = ["https://" + user_name + ":" + password + "@archive.thehated7.workers.dev/0:/GeeksForGeeks/Data"
#                                                         "%20Structures%20and%20Algorithms%20(Self-Paced%20Course)/",
#               "https://" + user_name + ":" + password + "@archive.thehated7.workers.dev/0:/RBR Gate-2021/",
#               "https://" + user_name + ":" + password + "@archive.thehated7.workers.dev/0:/CodingNinjas/Aptitude/",
#               "https://" + user_name + ":" + password + "@archive.thehated7.workers.dev/0:/CodingNinjas/Advanced"
#                                                         "%20Data%20Structures/",
#               "https://" + user_name + ":" + password + "@archive.thehated7.workers.dev/0:/CodingNinjas/Data"
#                                                         "%20Structrures%20and%20Algorithms%20[Career%20Camp]/"][0]

file_links = "https://" + user_name + ":" + password + "@archive.thehated7.workers.dev/0:/Frontend%20Masters/Advanced%20JavaScript/"


# TODO: if links contains multiple folder and then links make it False
direct_videos_list = True


def wait_not_spinning(driver):
    try:
        return el and el is not None and 'spinner-border text-light m-5' != el.get_attribute('class')
    except:
        return True


def wait_stat(driver):
    waiting = wait(driver, 10)
    waiting.until(wait_not_spinning)


def move_files(move_folder_name, move_files_name, default_download_dir):
    move_folder_path = default_download_dir + move_folder_name
    try:
        for file_name in move_files_name:
            if not os.path.exists(move_folder_path):
                os.makedirs(move_folder_path)
            try:
                current_file_path = default_download_dir + file_name
                movable_file_path = default_download_dir + move_folder_name + "\\" + file_name

                shutil.move(current_file_path, movable_file_path)
            except Exception as e1:
                print("Not able to move :", e1)
    except:
        print("Ignore")

    try:
        for file in os.listdir(default_download_dir):
            if os.path.isfile(os.path.join(default_download_dir, file)):
                print("File : {}".format(file))
                shutil.move(file, move_folder_path)
    except:
        print("ignore")


def download_videos(driver, default_download_dir):
    element_drive = driver.find_elements_by_xpath("//div[@id='list' and @class='list-group text-break']/div/a")

    move_files_name_list = []
    folder_name = ""
    count = 1
    for child_ele in element_drive:
        if count <= 4:
            child_link_1 = child_ele.get_attribute('href')
            if "?a=view" not in child_link_1:
                folder_name = (child_link_1.split("/")[-2]).replace("%20", "")
                file_name = (child_link_1.split("/")[-1]).replace("%20", " ")
                move_files_name_list.append(file_name)
                driver.get(child_link_1)
                print(move_files_name_list)
                count += 1
        else:
            break
    time.sleep(30)
    if not direct_videos_list:
        move_files(folder_name, move_files_name_list, default_download_dir)


def fetch_element_download():
    global el
    final_elements_links = []
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
    download_path_file = open('download_path.txt', 'r')
    download_links = download_path_file.readlines()

    for file_link in download_links:

        default_download_dir = 'E:\\Download\\' + file_link.split("/")[-2] + "\\"
        print("default_download_dir", default_download_dir)

        try:
            os.makedirs(default_download_dir)
        except OSError as e:
            print("Already created")

        chrome_options = webdriver.ChromeOptions()
        prefs = {"download.default_directory": default_download_dir}
        chrome_options.add_experimental_option("prefs", prefs)
        chromedriver = r'C:\Users\Hemant\PycharmProjects\urlLib1\chromedriver.exe'

        driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)

        file_link_temp = file_link.replace("\n", "").split("archive")
        file_link = file_link_temp[0] + user_name + ":" + password + "@archive" + file_link_temp[-1]
        # Open URL
        driver.get(file_link)

        el = wait(driver, 30, ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='spinner-border text-light m-5']")))

        wait_stat(driver)

        if not direct_videos_list:

            elements = driver.find_elements_by_xpath("//div[@id='list' and @class='list-group text-break']/a")
            for ele in elements:
                ele_href = ele.get_attribute('href')
                print(ele_href)
                final_elements_links.append(ele_href)

            for ch_file_link in final_elements_links:
                driver.get(ch_file_link)

                el = wait(driver, 30, ignored_exceptions=ignored_exceptions).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@class='spinner-border text-light m-5']")))
                wait_stat(driver)
                download_videos(driver, default_download_dir)
        else:
            download_videos(driver, default_download_dir)


fetch_element_download()
