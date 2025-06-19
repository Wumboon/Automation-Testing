
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randrange
#os.environ['PATH']+= r"C:/SeleniumDrivers"
class OpenWebpage:
    
    def __init__(self, driver):
        self.driver.get("https://www.automationexercise.com/")
        self.driver.implicitly_wait(5)
    def __new__(self):
        # Ensure the WebDriver is properly closed when the object is deleted
        return self.driver
    
class SignUpPage:
    def __init__(self,driver):
        self.driver=driver
        signupbutton=self.driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
        signupbutton.click()
        
    def accountCreated(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, 'h2[data-qa="account-created"]')
            print("found account created is visible")
        except:
            print("an exception occured finding account created" )  
        self.driver.find_element(By.CSS_SELECTOR, 'a[data-qa="continue-button"]').click()
        return self.driver
    
    def enterAccountInfo(self):
        self.driver.find_element(By.CLASS_NAME, "radio").click()
        self.driver.find_element(By.ID, "password").send_keys("QASUDEAR231")

        select=Select(self.driver.find_element(By.CSS_SELECTOR, 'select[data-qa="days"]'))
        select.select_by_visible_text("10")
        select=Select(self.driver.find_element(By.CSS_SELECTOR, 'select[data-qa="months"]'))
        select.select_by_visible_text("November")
        select=Select(self.driver.find_element(By.CSS_SELECTOR, 'select[data-qa="years"]'))
        select.select_by_visible_text("1998")

        self.driver.find_element(By.NAME, "newsletter").click()
        self.driver.find_element(By.NAME, "optin").click()

        self.driver.find_element(By.CSS_SELECTOR, 'input[data-qa="first_name"]').send_keys("John")
        self.driver.find_element(By.CSS_SELECTOR, 'input[data-qa="last_name"]').send_keys("Killabong")
        self.driver.find_element(By.CSS_SELECTOR, 'input[data-qa="company"]').send_keys("Amazon")
        self.driver.find_element(By.CSS_SELECTOR, 'input[data-qa="address"]').send_keys("7128 BerryHuckle Ave")
        self.driver.find_element(By.CSS_SELECTOR, 'input[data-qa="address2"]').send_keys("Unit 2")
        select=Select(self.driver.find_element(By.CSS_SELECTOR, 'select[data-qa="country"]'))
        select.select_by_visible_text("United States")
        self.driver.find_element(By.CSS_SELECTOR, 'input[data-qa="state"]').send_keys("CA")
        self.driver.find_element(By.CSS_SELECTOR, 'input[data-qa="city"]').send_keys("Palm Springs")
        self.driver.find_element(By.CSS_SELECTOR, 'input[data-qa="zipcode"]').send_keys("17283")
        self.driver.find_element(By.CSS_SELECTOR, 'input[data-qa="mobile_number"]').send_keys("16256750982")
        self.driver.find_element(By.CSS_SELECTOR, 'button[data-qa="create-account"]').click()
        return self.accountCreated()
        
    def createUser(self,email):
        #random_email="qatesting" + str(randrange(100000))+ "@gmail.com"
        self.driver.find_element(By.CSS_SELECTOR, 'input[data-qa="signup-name"]').send_keys("John")
        self.driver.find_element(By.CSS_SELECTOR, 'input[data-qa="signup-email"]').send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, 'button[data-qa="signup-button"]').click()
        
        try:
            WebDriverWait(self.driver,2).until(
                EC.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, 'form[action="/signup"]'),
                    'Email Address already exist!'
                ),
            )
            print("email address already exists")
            return self.driver
            #print("email found")
        except:
            print("successfully created email")
            return self.enterAccountInfo()
            #print("email not found")
            
        #return self.enterAccountInfo()
    
        
class SignInPage:
    #driver=webdriver.Chrome()
    def __init__(self, driver):
        self.driver=driver
        loginbutton=self.driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
        loginbutton.click()

    def LogInUser(self, username,password):
        self.driver.find_element(By.CSS_SELECTOR, 'input[data-qa="login-email"]').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, 'input[data-qa="login-password"]').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, 'button[data-qa="login-button"]').click()
        self.driver.implicitly_wait(3)
        if(self.driver.current_url=="https://www.automationexercise.com/login"):
            #raise Exception("Invalid User Login")
            print("Invalid User Login")
        else:
            print("successfully logged in")
        
        return self.driver
    
class HomePage:
    #driver=webdriver.Chrome()
    def __init__(self, driver):
        self.driver=driver
        if( self.driver.current_url=="https://www.automationexercise.com/"):
            print("User currently on home page")
        else:
            print("not on home page currently on " + self.driver.current_url)

    def LogOut(self):
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="/logout"]').click()
        self.driver.implicitly_wait(3)
        if(self.driver.current_url=="https://www.automationexercise.com/login"):
            print("Successfully went back to Login page")
        else:
            print("not on login page current page is "+ self.driver.current_url)
        return self.driver
    def deleteAccount(self):
        
        try:
            self.driver.find_element(By.CSS_SELECTOR, 'i[class="fa fa-user"]')
            print("found logged in as user is visible")
        except:
            print("an exception occured finding logged in as user" )

        self.driver.find_element(By.CSS_SELECTOR, 'a[href="/delete_account"]').click()
        try:
            self.driver.find_element(By.CSS_SELECTOR, 'h2[data-qa="account-deleted"]')
            print("found account deleted visible")
        except:
            print("an exception occured finding account deleted" )
            
        return self.driver
    def CheckLoggedInStatus(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, 'i[class="fa fa-user"]')
            print("found logged in as user is visible")
        except:
            print("an exception occured finding logged in as user" )




def findClassElement(driver,classname):
    try:
        driver.find_element(By.CLASS_NAME, classname)
        print("found "+ classname)
    except:
        print("an exception occured finding " + classname)

def is_text_present(self, text):
    return str(text) in self.driver.page_source


def testCase1():
    # Register User end to end
    driver=webdriver.Chrome()
    driver.get("https://www.automationexercise.com/")
    driver.implicitly_wait(5)
    random_email="qatesting" + str(randrange(100000))+ "@gmail.com"
    
    driver=SignUpPage(driver).createUser(random_email)
    
    driver=HomePage(driver).deleteAccount()
    
    
    #driver.close()
        
        
        
def testCase2():
# Login user with correct email and password
    driver=webdriver.Chrome()
    driver.get("https://www.automationexercise.com/")
    driver.implicitly_wait(5)

    driver=SignInPage(driver).LogInUser("LoggedInTest18457@gmail.com","TestingPassword91872")
    #driver=test.LogInUser("LoggedInTest18457@gmail.com","TestingPassword91872")
    
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
    driver.implicitly_wait(5)

    
    driver=SignInPage(driver).LogInUser("BadEmailTest@gmail.com","badPassword")
    #driver=test.LogInUser("BadEmailTest@gmail.com","badPassword")
    
    WebDriverWait(driver,30).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, 'form[action="/login"]'),
            'Your email or password is incorrect'
        ),
    )
        
    #driver.close()

def testCase4():
# Logout User
    driver=webdriver.Chrome()
    driver.get("https://www.automationexercise.com/")
    driver.implicitly_wait(5)
    
    homepage=HomePage(driver)
    
    loginbutton=driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
    loginbutton.click()
    
    driver=SignInPage(driver).LogInUser("LoggedInTest18457@gmail.com","TestingPassword91872")

    homepage=HomePage(driver)
    
    homepage.CheckLoggedInStatus()

    homepage.LogOut()
    
        
    #driver.close()

def testCase5():
# Register User with existing Email
    driver=webdriver.Chrome()
    driver.get("https://www.automationexercise.com/")
    driver.implicitly_wait(5)
    
    signup=SignUpPage(driver)
    driver=signup.createUser("LoggedInTest18457@gmail.com")
       
        
    #driver.close()
        

testCase1()
testCase2()
testCase3()
testCase4()
testCase5()
