from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from time import sleep
from getpass import getpass
import json
import datetime
import sys

from cryptography.fernet import Fernet

def scrape(tag):
    """

    :param tag: 

    """
    cipher_suite = ""
    DEFAULT_ID = 100
    account = "userinfo.json"
    hasAuth = False
    user = ""
    login = ""
    password = ""

    if (tag == "-f"):
        try:
            with open(account) as f:
                
                print("File found. Reading...") 

                data = json.load(f)
                data_to_write = data

                account_rec = data
                user = account_rec["user"]
                login = account_rec["login"]
                password = account_rec["pass"]
                password = password[2:-1].encode()

                cipher_suite = Fernet(account_rec["key"].encode())

                hasAuth = True
       
        except FileNotFoundError:
            print("File not found. Continuing...")
               

    if not hasAuth:

        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        
        user = input("What's your twitter username (not display)? ")
        login = input("What's your login? (email/username) ")
        password = getpass("Type in your password. ")
        password = cipher_suite.encrypt(password.encode('utf-8'))

        account_rec = {
            "user": user,
            "login": login,
            "pass": password.decode(),
            "key": key.decode(),
        }

        if input("Do you want me to store your information in a text file? When you run this program again, you can append '-f' to automatically search your account. (y/n) ") == "y":
            try:
                with open(account) as f:
                    
                    print("File found. Writing...") 

                    data = json.load(f)
                    data_to_write = data

                    data_to_write = account_rec
           
            except FileNotFoundError:
                print("File not found. Creating...")
                with open(account, 'w') as f:
                   
                    data_to_write = account_rec
                    
            with open(account, 'w') as outfile:
                json.dump(data_to_write, outfile)
                print("Account info saved! Initiating scrape mode.")


    max_id = input("Type in the maximum number of tweets we'll collect. Otherwise, type n (default: 100). ") 
    if max_id == "n":
        max_id = DEFAULT_ID

    delay = 1  # time to wait on each page load before reading the page
    driver = webdriver.Firefox(executable_path="geckodriver")  # options are Chrome() Firefox() Safari()
    driver.implicitly_wait(10)

    twitter_ids_filename = 'all_ids.json'
    tweet_selector = 'article'
    id_selector = "a[href*=status]"

    user = user.lower()
    ids = []
    errors = []

    MAX_IDS = int(max_id)

    likes_url = f"https://twitter.com/{user}/likes"
    url = "https://twitter.com/login"
    driver.get(url)


    user_selector = 'div.css-1dbjc4n:nth-child(6) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)'
    pass_selector = 'div.css-1dbjc4n:nth-child(7) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)'
    error_selector = 'div.css-901oao:nth-child(3) > span:nth-child(1)'
    scrollElementIntoMiddle = "let viewPortHeight = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);" + "var elementTop = arguments[0].getBoundingClientRect().top;" + "window.scrollBy(0, elementTop-(viewPortHeight/2));";

    sleep(delay)

    try:
        print("Logging in..")
        found_user = driver.find_element_by_css_selector(user_selector)
        found_pass = driver.find_element_by_css_selector(pass_selector)

        found_user.send_keys(login)
        sleep(delay)
        
        print(password)
        password = cipher_suite.decrypt(password)
        password = str(password.decode('utf-8'))
        found_pass.send_keys(password, Keys.ENTER)
     
        sleep(delay)

        try:

            found_error = driver.find_element_by_css_selector(error_selector)
            print("Found error.")
            found_user = driver.find_element_by_css_selector(user_selector)
            # print(found_user)
            found_pass = driver.find_element_by_css_selector(pass_selector)
            # print(found_pass)

            found_user.send_keys(user)
            found_pass.send_keys(password, Keys.ENTER)

        
        except NoSuchElementReference:
            print("Successful login!")
        
        print("Checking profile...")
        sleep(delay)
        driver.get(likes_url)
        sleep(delay)
        found_tweets = driver.find_elements_by_css_selector(tweet_selector)
        increment = 5

        timeout = 0
        isEnd = 0
        MAX_END_TIMEOUT = 10
        
        while isEnd <= MAX_END_TIMEOUT:
            
            if len(ids) >= MAX_IDS:
                print("Reached max IDs.")
                break

            print("Looks like there's more. Continuing. . .")


            try:
                while isEnd <= MAX_END_TIMEOUT and len(ids) < MAX_IDS and len(found_tweets) >= increment:
                    print('Loading more tweets, scrolling. . . ')
                  
                  
                    sleep(delay)
                    found_tweets = driver.find_elements_by_css_selector(tweet_selector)
                    
                    numUnique = 0

                    for tweet in found_tweets:
                        
                        try:
                            metadata = tweet.find_element_by_css_selector(id_selector).get_attribute('href').replace("https://twitter.com", "")
                            id = tweet.find_element_by_css_selector(id_selector).get_attribute('href').split('/')[-1]
                
                            if id not in ids:
                                
                                print(f"ID: {id}, x-data: {metadata}")
                                ids.append(id)

                                numUnique += 1
                                isEnd = 0

                                if (len(ids) >= MAX_IDS):
                                    break
                            
                        
                        except StaleElementReferenceException as e:
                            print('Lost element reference.', tweet)

                    print('{} total tweets.'.format(len(ids)))

                    driver.execute_script(scrollElementIntoMiddle, found_tweets[-1])

                    timeout = 0

                    if numUnique == 0:
                         isEnd += 1

                    print("isEnd: " + str(isEnd))


            except NoSuchElementException:
                 print('None found.')

                 if not len(errors) == 0 and ids[-1] == errors[-1]["id"]:
                     timeout += 1

                 print("NonElement Timeout: " + str(timeout))
                 if timeout >= 10:
                     break

                 errors.append({"id": ids[-1], "num": len(ids)})
                 driver.execute_script(scrollElementIntoMiddle, found_tweets[-1])

                    
    except KeyboardInterrupt:
        print('CTRL+C.')

    try:
        with open(twitter_ids_filename) as f:
            
            data = json.load(f)
            data_to_write = data

            for i in ids:
                if i not in data:
                    data_to_write.append(i)

            print('Number of IDs: ', len(ids))
            print('Total Count: ', len(data_to_write))

    except FileNotFoundError:
        with open(twitter_ids_filename, 'w') as f:
            
            data = json.load(f)
            data_to_write = data

            for i in ids:
                if i not in data:
                    data_to_write.append(i)

            print('Number of IDs: ', len(ids))
            print('Total Count: ', len(data_to_write))

    with open(twitter_ids_filename, 'w') as outfile:
        json.dump(data_to_write, outfile)

    print('All done.')
    driver.close()
