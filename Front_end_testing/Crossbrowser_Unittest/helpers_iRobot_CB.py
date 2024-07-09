
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
import random
import requests


# iRobot URL
iRobot_url = "https://www.irobot.com/"


# Homepage API check
def homepage_api_check(driver):
    print("----API check: Url has", requests.get("https://www.irobot.com/").status_code, "as status Code")
    code = requests.get("https://www.irobot.com/").status_code
    if code == 200:
        print("----API response code is OK")
    else:
        print("ATTENTION!  API response code is not 200", "Current code is:", code)


# Homepage title check
def homepage_title_check(driver):
    if "iRobot®: Robot Vacuums and Mops" not in driver.title:
        raise Exception("ATTENTION! Title is different in iRobot home page")
    else:
        print("----Title check: Page has iRobot®: Robot Vacuums and Mops title")


# Homepage iRobot logo
homepage_logo = "//a[contains(@class,'logo-home s-header__logo-home')]"


# Home page verify
def verify_homepage(driver):
    try:
        WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((
                By.XPATH, "//a[contains(@class,'logo-home s-header__logo-home')]")))
    except TimeoutException:
        print("ATTENTION! Can't find iRobot logo on the homepage")


# Login link
login_link = "(//span[contains(.,'Login')])[1]"


# Login page title check
def login_title_check(driver):
    if "Login Page | iRobot®" not in driver.title:
        raise Exception("ATTENTION! Title is different in Login page")
    else:
        print("----Title check: Page has 'Login Page | iRobot®' title")


# Registration password
password_1 = "Aa1234567890!"

# Registration email
email_1 = "cimihi3144@fna6.com"
email_2 = "sotodig265@crodity.com"

city = "San Antonio"
state = "Texas"


zip_code = "78253"



# Login email box
login_email_box = "//input[@id='gigya-loginID-111298689147766560']"
login_email_boxEdge = '//*[@id="gigya-loginID-111298689147766560"]'

# Login password box
login_password_box = "//input[@id='gigya-password-17588167012738688']"

# Login email
login_email = "sotodig265@crodity.com"


# Title check account page
def account_page_title_check(driver):
    print("----Title check: Page has", driver.title + " as Page title")
    if "Account" not in driver.title:
        raise Exception("ATTENTION!  Title is wrong!")


name = random.choice(["#", "!", "@", "$", "%", "&", "*", "(", ")", "-", "=", "+"])



