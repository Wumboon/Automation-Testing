
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

def is_text_present(self, text):
    return str(text) in self.driver.page_source

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



def testCase1():
    # Register User end to end 
    driver=webdriver.Chrome()
    driver.get("https://www.automationexercise.com/")
    driver.implicitly_wait(5)

    signupbutton=driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
    signupbutton.click()

    findClassElement(driver,"signup-form")
    
    create_account(driver)
    
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
    
    #driver.close()
        
        
        
def testCase2():
# Login user with correct email and password
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
        
    #driver.close()

def testCase3():
# Login user with incorrect email and password
    driver=webdriver.Chrome()
    driver.get("https://www.automationexercise.com/")
    driver.implicitly_wait(10)

    loginbutton=driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
    loginbutton.click()
    
    findClassElement(driver,"login-form")
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="login-email"]').send_keys("BadEmailTest@gmail.com")
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="login-password"]').send_keys("badPassword")
    driver.find_element(By.CSS_SELECTOR, 'button[data-qa="login-button"]').click()
    
    bd = driver.find_element(By.CSS_SELECTOR, 'form[action="/login"]').text
    
    if "Your email or password is incorrect" in bd:
        print("email and password incorrect found")
    else:
        print("error message did not appear for email/password incorrect")
        
    #driver.close()

def testCase4():
# Logout User
    driver=webdriver.Chrome()
    driver.get("https://www.automationexercise.com/")
    driver.implicitly_wait(5)

    if(driver.current_url=="https://www.automationexercise.com/"):
        print("Is currently on home page")
    else:
        print("not on home page current page is "+driver.current_url)
    
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
    
    driver.find_element(By.CSS_SELECTOR, 'a[href="/logout"]').click()
    if(driver.current_url=="https://www.automationexercise.com/login"):
        print("Successfully went back to Login page")
    else:
        print("not on login page current page is "+driver.current_url)
        
    #driver.close()

def testCase5():
# Register User with existing Email
    driver=webdriver.Chrome()
    driver.get("https://www.automationexercise.com/")
    driver.implicitly_wait(5)

    loginbutton=driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
    loginbutton.click()
    
    findClassElement(driver,"signup-form")
    
    
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="signup-name"]').send_keys("John")
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="signup-email"]').send_keys("LoggedInTest18457@gmail.com")
    driver.find_element(By.CSS_SELECTOR, 'button[data-qa="signup-button"]').click()
    
    bd = driver.find_element(By.CSS_SELECTOR, 'form[action="/signup"]').text
    
    if "Email Address already exist!" in bd:
        print("email address already exists found")
    else:
        print("error message did not appear for existing email address")
        
    #driver.close()
        

testCase1()
testCase2()
testCase3()
testCase4()
testCase5()
