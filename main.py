
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from random import randrange
#os.environ['PATH']+= r"C:/SeleniumDrivers"

def findClassElement(driver,classname):
    try:
        driver.find_element(By.CLASS_NAME, classname)
        print("found "+ classname)
    except:
        print("an exception occured finding " + classname)

def create_account(driver):
    random_email="qatesting" + str(randrange(100000))+ "@gmail.com"
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="signup-name"]').send_keys("John")
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="signup-email"]').send_keys(random_email)
    driver.find_element(By.CSS_SELECTOR, 'button[data-qa="signup-button"]').click()

    findClassElement(driver,"login-form")

    driver.find_element(By.CLASS_NAME, "radio").click()
    driver.find_element(By.ID, "password").send_keys("QASUDEAR231")

    select=Select(driver.find_element(By.CSS_SELECTOR, 'select[data-qa="days"]'))
    select.select_by_visible_text("10")
    select=Select(driver.find_element(By.CSS_SELECTOR, 'select[data-qa="months"]'))
    select.select_by_visible_text("November")
    select=Select(driver.find_element(By.CSS_SELECTOR, 'select[data-qa="years"]'))
    select.select_by_visible_text("1998")

    driver.find_element(By.NAME, "newsletter").click()
    driver.find_element(By.NAME, "optin").click()

    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="first_name"]').send_keys("John")
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="last_name"]').send_keys("Killabong")
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="company"]').send_keys("Amazon")
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="address"]').send_keys("7128 BerryHuckle Ave")
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="address2"]').send_keys("Unit 2")
    select=Select(driver.find_element(By.CSS_SELECTOR, 'select[data-qa="country"]'))
    select.select_by_visible_text("United States")
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="state"]').send_keys("CA")
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="city"]').send_keys("Palm Springs")
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="zipcode"]').send_keys("17283")
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="mobile_number"]').send_keys("16256750982")
    driver.find_element(By.CSS_SELECTOR, 'button[data-qa="create-account"]').click()
    # return random_email
# def verifyCSSExist(tag, type, name):
#     print("'"+tag+'['+type+'='+'"'+name+'"'+']'+"'")
#     try:
#         driver.find_element(By.CSS_SELECTOR, "'"+tag+'['+type+'='+'"'+name+'"'+']'+"'")
#         print("found "+ name)
#     except:
#         print(" not found "+name)



def testCase1():
    driver=webdriver.Chrome()
    driver.get("https://www.automationexercise.com/")
    driver.implicitly_wait(5)

    signupbutton=driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
    signupbutton.click()

    findClassElement(driver,"signup-form")
    
    create_account(driver)
    #verifyCSSExist('h2','data-qa',"account-created")
    
    try:
        driver.find_element(By.CSS_SELECTOR, 'h2[data-qa="account-created"]')
        print("found account created is visible")
    except:
        print("an exception occured finding account created" )
        
    driver.find_element(By.CSS_SELECTOR, 'a[data-qa="continue-button"]').click()

    try:
        driver.find_element(By.CSS_SELECTOR, 'i[class="fa fa-user"]')
        print("found logged in as user is visible")
    except:
        print("an exception occured finding logged in as user" )

    driver.find_element(By.CSS_SELECTOR, 'a[href="/delete_account"]').click()

    try:
        driver.find_element(By.CSS_SELECTOR, 'h2[data-qa="account-deleted"]')
        print("found account deleted visible")
    except:
        print("an exception occured finding account deleted" )
        
        
        
def testCase2():
    driver=webdriver.Chrome()
    driver.get("https://www.automationexercise.com/")
    driver.implicitly_wait(5)

    loginbutton=driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
    loginbutton.click()
    
    findClassElement(driver,"login-form")
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="login-email"]').send_keys("LoggedInTest18457@gmail.com")
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="login-password"]').send_keys("TestingPassword91872")
    driver.find_element(By.CSS_SELECTOR, 'button[data-qa="login-button"]').click()
    
    try:
        driver.find_element(By.CSS_SELECTOR, 'i[class="fa fa-user"]')
        print("found logged in as user is visible")
    except:
        print("an exception occured finding logged in as user" )

def testCase3():
    driver=webdriver.Chrome()
    driver.get("https://www.automationexercise.com/")
    driver.implicitly_wait(5)

    loginbutton=driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
    loginbutton.click()

testCase1()
testCase2()
testCase3()