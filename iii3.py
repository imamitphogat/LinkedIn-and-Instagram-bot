
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def wait_for_object(self , type, string):
        return WebDriverWait(self.browser, 3).until(EC.presence_of_element_located((type,string)))

def wait_for_objects(self , type, string):
        return WebDriverWait(self.browser, 15).until(EC.presence_of_all_elements_located((type,string)))


def read_usernames(filename):
    with open(filename, 'r') as file:
        usernames = [line.strip() for line in file]
    return usernames

def chunk_users(usernames, chunk_size):
    return [usernames[i:i + chunk_size] for i in range(0, len(usernames), chunk_size)]

def login_instagram(driver, username, password):
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(4)

    username_input = driver.find_element(By.NAME ,  'username')
    password_input = driver.find_element(By.NAME ,  'password')

    username_input.send_keys(username)
    time.sleep(4)
    password_input.send_keys(password)
    time.sleep(4)
    password_input.send_keys(Keys.RETURN)
    time.sleep(8)
    try:         
        username_input = driver.find_element(By.NAME ,  'username')
        password_input = driver.find_element(By.NAME ,  'password')

        username_input.send_keys(username)
        time.sleep(4)
        password_input.send_keys(password)
        time.sleep(4)
        password_input.send_keys(Keys.RETURN)
        time.sleep(8)
    except:
         pass

def send_messages(driver, users):
    for user in users:

        driver.get('https://www.instagram.com/direct/inbox/')
        time.sleep(4)

        try:
            notnow_button = driver.find_element(By.CSS_SELECTOR, 'button._a9--._a9_1')
            notnow_button.click()
        except:
             pass
                    
        time.sleep(4)
        senduser = driver.find_element(By.XPATH, "//div[contains(text(),'Send message')]")
        senduser.click()
        time.sleep(4)
        search_user = driver.find_element(By.XPATH, "//input[@placeholder='Search...']")
        search_user.click()
        search_user.send_keys(f"{user}")
        time.sleep(10)
        select_user = driver.find_element(By.XPATH, "(//div[@aria-label='Toggle selection'])[1]")
        select_user.click()
        time.sleep(4)
        chat_user = driver.find_element(By.XPATH, "//div[contains(text(),'Chat')]")
        chat_user.click()
        
        time.sleep(4)

        message_input = driver.find_element(By.XPATH, "(//p[@class='xat24cr xdj266r'])[1]")
        message_input.send_keys("Testing....") # message here
        message_input.send_keys(Keys.RETURN)
        time.sleep(4)

def logout_instagram(driver):
    driver.get('https://www.instagram.com/accounts/logout/')
    time.sleep(2)

def main():
    usernames = read_usernames('usernames.txt')
    user_groups = chunk_users(usernames, 10)

    accounts = [
        {'username': 'Account', 'password': 'your Password'},
        {'username': 'account', 'password': 'your password'},
        # Add more accounts as needed
    ]

    driver = webdriver.Chrome()

    for i, users in enumerate(user_groups):
        account = accounts[i % len(accounts)]
        login_instagram(driver, account['username'], account['password'])
        send_messages(driver, users)
        logout_instagram(driver)

    driver.quit()

if __name__ == '__main__':
    main()
