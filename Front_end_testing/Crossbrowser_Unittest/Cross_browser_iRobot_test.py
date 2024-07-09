# Crossbrowser Positive and Negative unittests for https://www.irobot.com

from selenium import webdriver
import AllureReports
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
import unittest
import time
import helpers_iRobot_CB as H
from faker import Faker
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service

fake = Faker()


# driver sleep from 1 to 15 seconds


def delay():
    time.sleep(random.randint(1, 5))


def scroll_to_element(iframe):
    pass


class ChromeAPositiveTests(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        ser = Service(r"C:/Webdriver/chromedriver.exe")
        options.add_argument('--headless')
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.set_window_size(1920, 1080)
        driver = webdriver.Chrome(service=ser, options=options)

    # As per unittest module, individual test should start with test

    def test_case_001_irobot(self):
        driver = self.driver
        # driver = webdriver.Chrome(service=ser, options=options)
        print("                                                                                                    ")
        print("                                               I_ROBOT                                         ")
        print("                                                                                                    ")
        print("-----------------------------------------POSITIVE TEST CASES ---------------------------------------")
        print("                                                                                                    ")

        # TC001
        print("                TC001                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Check title
        H.homepage_title_check(driver)

        # Verifying correct homepage
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.homepage_logo)))
        delay()
        driver.find_element(By.ID, 'us-products')
        driver.find_element(By.ID, 'us-offers-deals')
        driver.find_element(By.ID, 'us-why-irobot')

        # Verify and validate Login link
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, H.login_link))).click()
        delay()

        # Title check
        self.assertIn("Login Page | iRobot®", driver.title)
        H.login_title_check(driver)

        # Creating acct
        wait = WebDriverWait(driver, 6)
        wait.until(EC.element_to_be_clickable((By.ID, "register-tab"))).click()
        delay()

        # Filling out the form
        first_name = driver.find_element(By.XPATH, "//input[@id='gigya-textbox-62368141417735550']")
        first_name.clear()
        first_name.send_keys(fake.first_name())
        last_name = driver.find_element(By.XPATH, "//input[@id='gigya-textbox-48256792335834616']")
        last_name.clear()
        last_name.send_keys(fake.last_name())
        delay()
        email = driver.find_element(By.XPATH, "//input[@id='gigya-loginID-94607575331121620']")
        email.clear()
        email.send_keys(fake.email())
        driver.execute_script("window.scrollTo(0,700)")
        time.sleep(5)
        password = driver.find_element(By.XPATH, "//input[@id='gigya-password-48204272427543900']")
        password.clear()
        password.send_keys(H.password_1)
        conf_password = driver.find_element(By.XPATH, "//input[@id='gigya-password-98920497041796370']")
        conf_password.clear()
        conf_password.send_keys(H.password_1)
        delay()

        # Check boxes
        terms = driver.find_element(By.XPATH, "//label[contains(.,'I accept Terms & Conditions*')]")
        driver.execute_script("arguments[0].click();", terms)
        time.sleep(3)
        conditions = driver.find_element(By.XPATH, '//*[@type="checkbox" and @id="gigya-checkbox-131682473014535710"]')
        driver.execute_script("arguments[0].click();", conditions)
        time.sleep(3)
        agreement = driver.find_element(By.XPATH, '//*[@type="checkbox" and @id="gigya-checkbox-84396646538548260"]')
        driver.execute_script("arguments[0].click();", agreement)
        delay()

        # Create account
        driver.find_element(By.XPATH, "//input[contains(@value,'Create account')]").click()
        delay()

        # Scrolling up
        driver.execute_script("window.scrollTo(700,0)")
        H.login_title_check(driver)
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="gigya-otp-update-form"]/div[1]/label[1]')))
        driver.find_element(By.XPATH, "//input[contains(@value,'Verify')]")
        driver.find_element(By.XPATH, "//a[contains(text(),'Send a new code')]")
        driver.save_screenshot('registration_code_msg.png')

        # TC001 results
        print("----Message 'Enter the code sent to:' is present")
        print("                                                                                                     ")
        print("             TC001  PASS                                                                            ")
        print("        --------------------                                                                        ")

    def test_case_003_irobot(self):
        driver = self.driver

        # TC003
        print("                                                                                                     ")
        print("                TC003                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)

        # Verify homepage
        H.verify_homepage(driver)

        # Verify and validate Login link
        driver.find_element(By.XPATH, H.login_link).click()
        time.sleep(0.8)

        # Title check
        self.assertIn("Login Page | iRobot®", driver.title)
        H.login_title_check(driver)
        delay()

        # Loging in with existing valid credentials(email,password)
        #         driver.save_screenshot("345.png")
        email = driver.find_element(By.XPATH, H.login_email_box)
        email.clear()
        email.send_keys(H.login_email)
        delay()
        password = driver.find_element(By.XPATH, H.login_password_box)
        password.clear()
        password.send_keys(H.password_1)
        delay()
        driver.find_element(By.XPATH, "//input[contains(@value,'Log in')]").click()
        time.sleep(5)

        # Title check
        self.assertIn("Account Page | iRobot®", driver.title)
        H.account_page_title_check(driver)

        # Verify that it is an "Account page"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'My Account')]")))
        driver.find_element(By.XPATH, "//h2[contains(text(),'Profile')]")
        delay()

        # Scroll down
        driver.execute_script("window.scrollTo(0,600)")
        delay()

        # Adding new address fake
        driver.find_element(By.XPATH, "//h2[contains(text(),'Address Book')]")
        driver.find_element(By.XPATH, "//a[@href='/en_US/add-new-address'][contains(.,'Add New')]").click()
        time.sleep(5)

        # Title check
        if "Add New Address To Account | iRobot®" not in driver.title:
            raise Exception("ATTENTION! Title is different in iRobot home page")
        else:
            print("----Title check: Page has 'Add New Address To Account | iRobot®' title")

        # Verify that page is correct
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Address Book')]")))
        driver.find_element(By.XPATH, "//h2[contains(text(),'Add New Address')]")
        delay()

        # Adding new Address
        address_title = driver.find_element(By.XPATH, "//input[@id='addressId']")
        place = str(random.randint(0, 50))
        place_title = "Work" + place
        address_title.send_keys(place_title)
        driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys(fake.first_name())
        time.sleep(0.2)
        driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys(fake.last_name())
        driver.execute_script("window.scrollTo(0,700)")
        driver.find_element(By.XPATH, "//input[@id='address1']").send_keys(fake.street_address())
        delay()
        state = Select(driver.find_element(By.XPATH, "//select[@id='state']"))
        state.select_by_visible_text(H.state)
        delay()
        driver.execute_script("window.scrollTo(0,600)")
        driver.find_element(By.XPATH, "//input[@id='city']").send_keys(H.city)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='zipCode']").send_keys(H.zip_code)
        time.sleep(3)
        a = str(random.randint(200, 999))
        b = str(random.randint(1000, 9999))
        phone = a + "-" + a + "-" + b
        print(phone)
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='phone']").send_keys(phone)
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(text(),'Save')]").click()
        time.sleep(3)

        # Title check
        assert "Sites-iRobotUS-Site" in driver.title
        print("----Title check: Page has", driver.title + " as Page title")

        # Verify correct page
        driver.find_element(By.XPATH, "//a[contains(text(),'Add New')]")

        # Screenshot of the new added address
        driver.save_screenshot('address book.png')
        print("----New Address was added. Check screenshot")

        # TC003 results
        print("                                                                                                     ")
        print("             TC003  PASS                                                                            ")
        print("        --------------------                                                                        ")

    def test_case_004_irobot(self):
        driver = self.driver

        # TC004
        print("                                                                                                     ")
        print("                TC004                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)


        # Verify homepage
        H.verify_homepage(driver)

        # Verifying and validating "Products" menu
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='us-products']"))).click()
        print("----Products link is clickable")
        driver.find_element(By.XPATH, "//div[contains(@class,'dropdown-menu js-dropdown-menu right-in show')]")

        # items on dropdown menu
        wait.until(EC.visibility_of_element_located((By.ID, "us-roomba-robotic-vacuums")))
        wait.until(EC.visibility_of_element_located((By.ID, 'us-braava-robotic-mops')))
        time.sleep(0.5)
        wait.until(EC.visibility_of_element_located((By.ID, 'us-shop-all')))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[contains(.,'Quick Links')])[12]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Help Me Choose')])[1]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Compare Products')])[1]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Trade in')])[1]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Financing')])[1]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'eGift Cards')]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Shop Accessories')])[1]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Compare Products')])[2]")))
        print("----'Products' link is visible and dropdown menu functional and visible")

        # TC004 Results
        print("                                                                                                     ")
        print("             TC004  PASS                                                                            ")
        print("        --------------------                                                                        ")

    def test_case_005_irobot(self):
        driver = self.driver

        # TC005
        print("                                                                                                     ")
        print("                TC005                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)

        # Verify homepage
        H.verify_homepage(driver)

        # Verification and validation of "Why iRobot" link
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.ID, "us-why-irobot"))).click()

        # Verification and validation of "Why iRobot" dropdown menu
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='dropdown-menu js-dropdown-menu right-in show']")))
        wait.until(EC.visibility_of_element_located((By.ID, "why-irobot")))
        time.sleep(0.5)
        wait.until(EC.visibility_of_element_located((By.ID, "irobot-home-app")))
        time.sleep(0.6)
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[contains(.,'Quick Links')])[16]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'P.O.O.P. Promise')]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[contains(.,"Blog")])[1]')))
        time.sleep(0.4)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Help me choose')]")))

        print("----'Why iRobot' link is visible and clickable. Dropdown menu is visible and functional.")

        # TC005 Results
        print("                                                                                                     ")
        print("             TC005  PASS                                                                            ")
        print("        --------------------                                                                        ")

    def test_case_006_irobot(self):
        driver = self.driver

        # TC006
        print("                                                                                                     ")
        print("                TC006                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)

        # Verify homepage
        H.verify_homepage(driver)

        # Verification and validation of "Accessories" link
        delay()
        try:
            WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, "us-parts-accessories"))).click()
        except TimeoutException:
            print("ATTENTION! Can't find 'Accessories' link")
        delay()

        # Verification and validation of "Accessories" dropdown menu
        wait = WebDriverWait(driver, 3)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[@class='dropdown-menu js-dropdown-menu right-in show']")))
        wait.until(EC.visibility_of_element_located((By.ID, "us-roomba-parts-accessories")))
        time.sleep(0.5)
        wait.until(EC.visibility_of_element_located((By.ID, "us-braava-parts-accessories")))
        wait.until(EC.visibility_of_element_located((By.ID, "us-parts-bundles")))
        delay()
        wait.until(EC.visibility_of_element_located((By.ID, "us-aeris-handheld-irobot-parts-accessories")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[contains(.,'Quick Links')])[20]")))
        delay()
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(@class,'usefull-link')])[9]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(@class,'usefull-link')])[11]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Shop now')]")))

        print("----'Accessories' link is visible and clickable. Dropdown menu is visible and functional.")

        # TC006 results
        print("                                                                                                     ")
        print("             TC006  PASS                                                                            ")
        print("        --------------------                                                                        ")

    def test_case_007_irobot(self):
        driver = self.driver

        # TC007
        print("                                                                                                     ")
        print("                TC007                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)

        # Verify homepage
        H.verify_homepage(driver)

        # Verification and validation of "iRobot OS" link
        delay()
        try:
            WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, "us-irobot-os-menu"))).click()
        except WDE:
            print("ATTENTION! Can't find 'iRobot OS' link")
        delay()
        print("----'iRobot OS' link is clickable")

        # Title check:
        if "iRobot OS " not in driver.title:
            raise Exception("iRobot OS page has wrong Title!")
        else:
            print("----Title check: " + driver.title)

        # Verifying iRobot OS page
        try:
            WebDriverWait(driver, 4).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="us-irobot-os"]/div/div[1]/div/div/div/h2')))
            print("----'iRobot OS page is available")
            driver.get_screenshot_as_file('Screenshot_iRobotOS_page.png')
        except TimeoutException:
            print("ATTENTION! 'iRobot OS' page issue")
        driver.get_screenshot_as_file('iRobot_OS_page_error.png')

        # TC007 results
        print("                                                                                                     ")
        print("             TC007  PASS                                                                            ")
        print("        --------------------                                                                        ")

    def test_case_008_irobot(self):
        driver = self.driver

        # TC008
        print("                                                                                                     ")
        print("                TC008                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)
        delay()

        # Verify homepage
        H.verify_homepage(driver)

        # Verification and validation of "Shop by Lifestyle" link
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.ID, 'us-shop-by-lifestyle'))).click()
        delay()
        print("----'Shop by Lifestyle' link is clickable")

        # Verification and validation of "Shop by Lifestyle" dropdown menu
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="sg-navbar-collapse"]/div/div/nav/div[2]/ul/li[6]/div/ul')))
        delay()
        wait.until(EC.visibility_of_element_located((By.ID, "us-pet-owners-lifestyle")))
        wait.until(EC.visibility_of_element_located((By.ID, "us-tech-enthusiast-lifestyle")))
        wait.until(EC.visibility_of_element_located((By.ID, "us-busy-family-lifestyle")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[contains(.,'Quick Links')])[24]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Compare Products')])[3]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Shop all Robots')])[2]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Help Me Choose')])[2]")))

        print("----'Shop by Lifestyle' link is visible and clickable. Dropdown menu is visible and functional.")

        # TC008 results
        print("                                                                                                     ")
        print("             TC008  PASS                                                                            ")
        print("        --------------------                                                                        ")

    def tearDown(self):
        self.driver.quit()


class ChromeNegativeTests(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        # self.driver.maximize_window()
        self.driver.set_window_size(1920, 1080)

    # As per unittest module, individual test should start with test_

    def test_case_1_irobot(self):
        driver = self.driver
        print("                                                                                                    ")
        print("                                                I_ROBOT                                         ")
        print("                                                                                                    ")
        print("-----------------------------------------NEGATIVE TEST CASES ---------------------------------------")
        print("                                                                                                    ")
        # TC001
        print("                TC1                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Check title
        H.homepage_title_check(driver)

        # Verifying correct homepage
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.homepage_logo)))
        delay()
        driver.find_element(By.ID, 'us-products')
        driver.find_element(By.ID, 'us-offers-deals')
        driver.find_element(By.ID, 'us-why-irobot')

        # Verify and validate Login link
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, H.login_link))).click()
        delay()

        # Title check
        self.assertIn("Login Page | iRobot®", driver.title)
        H.login_title_check(driver)

        # Creating acct
        wait = WebDriverWait(driver, 6)
        wait.until(EC.element_to_be_clickable((By.ID, "register-tab"))).click()
        delay()

        # Filling out the form using invalid name
        first_name = driver.find_element(By.XPATH, "//input[@id='gigya-textbox-62368141417735550']")
        first_name.clear()

        # name = random.choice(["#", "!", "@", "$", "%", "&", "*", "(", ")", "-", "=", "+"])
        first_name.send_keys(H.name)
        last_name = driver.find_element(By.XPATH, "//input[@id='gigya-textbox-48256792335834616']")
        last_name.clear()
        last_name.send_keys(H.name)
        delay()
        email = driver.find_element(By.XPATH, "//input[@id='gigya-loginID-94607575331121620']")
        email.clear()
        email.send_keys(fake.email())
        driver.execute_script("window.scrollTo(0,700)")
        time.sleep(5)
        password = driver.find_element(By.XPATH, "//input[@id='gigya-password-48204272427543900']")
        password.clear()
        password.send_keys(H.password_1)
        conf_password = driver.find_element(By.XPATH, "//input[@id='gigya-password-98920497041796370']")
        conf_password.clear()
        conf_password.send_keys(H.password_1)
        delay()

        # Check boxes

        terms = driver.find_element(By.XPATH, "//label[contains(.,'I accept Terms & Conditions*')]")
        driver.execute_script("arguments[0].click();", terms)
        time.sleep(3)
        conditions = driver.find_element(By.XPATH, '//*[@type="checkbox" and @id="gigya-checkbox-131682473014535710"]')
        driver.execute_script("arguments[0].click();", conditions)
        time.sleep(3)
        agreement = driver.find_element(By.XPATH, '//*[@type="checkbox" and @id="gigya-checkbox-84396646538548260"]')
        driver.execute_script("arguments[0].click();", agreement)
        delay()

        # Create account
        driver.find_element(By.XPATH, "//input[contains(@value,'Create account')]").click()
        delay()

        # Scrolling up
        driver.execute_script("window.scrollTo(700,0)")
        delay()

        H.login_title_check(driver)

        delay()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="gigya-otp-update-form"]/div[1]/label[1]')))
        time.sleep(2)
        message = wait
        button = driver.find_element(By.XPATH, "//input[contains(@value,'Verify')]")

        link = driver.find_element(By.XPATH, "//a[contains(text(),'Send a new code')]")
        driver.save_screenshot('registration_code_msg.png')
        if link.is_displayed() or message.is_displayed() or button.is_displayed():
            print("----Registration is possible without valid name input")
            print("                                                                                                  ")
            print("             TC1  FAIL                                                                            ")
            print("        --------------------                                                                      ")
        else:
            print("                                                                                                  ")
            print("             TC1  PASS                                                                            ")
            print("        --------------------                                                                      ")

    def test_case_2_irobot(self):
        driver = self.driver

        # TC2
        print("                                                                                                     ")
        print("                TC2                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)

        # Verify homepage
        H.verify_homepage(driver)

        # Verify and validate Login link
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.login_link))).click()
        delay()

        # Title check
        self.assertIn("Login Page | iRobot®", driver.title)
        H.login_title_check(driver)

        # Login in with valid existing account
        email = driver.find_element(By.XPATH, H.login_email_box)
        email.clear()
        email.send_keys(H.email_1)
        delay()
        password = driver.find_element(By.XPATH, H.login_password_box)
        password.clear()
        password.send_keys(H.password_1)
        time.sleep(0.6)
        driver.find_element(By.XPATH, "//input[contains(@value,'Log in')]").click()
        delay()

        # Title check
        self.assertIn("Account Page | iRobot®", driver.title)
        H.account_page_title_check(driver)

        # Changing name to invalid name
        time.sleep(3)
        first_name = driver.find_element(By.XPATH, "//input[@id='gigya-textbox-firstName']")
        first_name.clear()
        invalid_name = str(random.randint(0, 9))
        first_name.send_keys(invalid_name)
        driver.execute_script("window.scrollTo(0,500)")
        delay()
        last_name = driver.find_element(By.XPATH, "//input[@id='gigya-textbox-lastName']")
        last_name.clear()
        last_name.send_keys(invalid_name)
        delay()
        update = driver.find_element(By.XPATH, "//input[contains(@value,'Update')]")
        if update.is_enabled():
            update.click()
            print("----User is able to update name using invalid name")
            print("                                                                                                  ")
            print("             TC2  FAIL                                                                            ")
            print("        --------------------                                                                      ")
        else:
            print("----User is not able to update name using invalid name")
            print("                                                                                                  ")
            print("             TC2  PASS                                                                           ")
            print("        --------------------                                                                      ")

    def test_case_3_irobot(self):
        driver = self.driver

        # TC3
        print("                                                                                                     ")
        print("                TC3                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)
        delay()

        # Verify homepage
        H.verify_homepage(driver)

        # Verify and validate Login link
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.login_link))).click()
        delay()

        # Title check
        self.assertIn("Login Page | iRobot®", driver.title)
        H.login_title_check(driver)
        delay()

        # Login in with existing valid credentials
        email = driver.find_element(By.XPATH, H.login_email_box)
        email.clear()
        email.send_keys(H.email_1)
        delay()
        password = driver.find_element(By.XPATH, H.login_password_box)
        password.clear()
        password.send_keys(H.password_1)
        time.sleep(0.6)
        driver.find_element(By.XPATH, "//input[contains(@value,'Log in')]").click()
        delay()

        # Title check
        self.assertIn("Account Page | iRobot®", driver.title)
        H.account_page_title_check(driver)
        delay()

        # Scrolling down
        driver.execute_script("window.scrollTo(0,500)")
        delay()

        # Add address link
        driver.find_element(By.XPATH, '(//a[contains(.,"Add New")])[1]').click()
        time.sleep(5)

        # Title check for new page
        self.assertIn("Add New Address To Account | iRobot®", driver.title)
        print("----Page has", driver.title + " as Page title")
        if "Add New Address To Account" not in driver.title:
            raise Exception("ATTENTION! Page Title is wrong!")
        delay()

        # Adding invalid address
        address_title = driver.find_element(By.XPATH, "//input[@id='addressId']")
        place = str(random.randint(0, 50))
        place_title = "Work" + place
        address_title.send_keys(place_title)
        first_name = driver.find_element(By.XPATH, "//input[@id='firstName']")
        first_name.send_keys(fake.first_name())
        delay()
        last_name = driver.find_element(By.XPATH, "//input[@id='lastName']")
        last_name.clear()
        last_name.send_keys(fake.last_name())
        driver.execute_script("window.scrollTo(0,500)")
        time.sleep(2)
        address = driver.find_element(By.XPATH, "//input[@id='address1']")
        address.clear()
        invalid_address = random.choices(["#", "!", "@", "$", "%", "&", "*", "(", ")", "-", "=", "+"], k=9)
        address.send_keys(invalid_address)
        delay()
        state = driver.find_element(By.XPATH, "//select[@id='state']")
        state.click()
        time.sleep(3)
        delay()
        dropdown = Select(state)
        dropdown.select_by_visible_text(H.state)
        delay()
        driver.find_element(By.XPATH, "//input[@id='city']").send_keys(H.city)
        driver.find_element(By.XPATH, "//input[@id='zipCode']").send_keys(H.zip_code)
        delay()
        a = str(random.randint(200, 999))
        b = str(random.randint(1000, 9999))
        phone = a + "-" + a + "-" + b
        driver.find_element(By.XPATH, "//input[@id='phone']").send_keys(phone)
        driver.find_element(By.XPATH, "//button[contains(text(),'Save')]").click()
        time.sleep(4)

        # Title check
        if self.assertIn("Sites-iRobotUS-Site", driver.title):
            print("----Page has", driver.title + " as Page title")
            print("----User is able to add invalid address")
            print("                                                                                                  ")
            print("             TC3  FAIL                                                                            ")
            print("        --------------------                                                                      ")
        else:
            print("----User is not able to add invalid address")
            print("                                                                                                  ")
            print("             TC3  PASS                                                                           ")
            print("        --------------------                                                                      ")

    def test_case_4_irobot(self):
        driver = self.driver

        # TC4
        print("                                                                                                     ")
        print("                TC4                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)
        delay()

        # Verify homepage
        H.verify_homepage(driver)

        # Scrolling down
        driver.execute_script("window.scrollTo(0,6500)")
        delay()

        # Signing up with invalid email
        email = driver.find_element(By.XPATH, "//input[contains(@class,'footer-email-input')]")
        email.clear()
        # a = str(random.choices(["#", "!", "@", "$", "%", "&", "*", "(", ")", "-", "=", "+"], k=4))
        b = str(random.randint(0, 100))
        # c = str(a + "@" + b)
        invalid_password = "####" + "@" + b + ".com"
        email.send_keys(invalid_password)
        delay()
        driver.find_element(By.XPATH, "//button[contains(text(),'Sign up')]").click()
        time.sleep(4)
        message = driver.find_element(By.XPATH, "/html/body/div/div[2]/p")

        # Title check anf results

        if "Your information has been submitted successfully" not in driver.title and message:
            print("----ATTENTION! Title is different")
            print("----Not able to sign up with invalid email")
            print("----User is not able to add invalid address")
            print("                                                                                                  ")
            print("             TC4  PASS                                                                           ")
            print("        --------------------                                                                      ")
        else:
            print("----Title check: Page has 'Your information has been submitted successfully' title")
            print("----Able to sign up with invalid email")
            print("                                                                                                  ")
            print("             TC4  FAIL                                                                            ")
            print("        --------------------                                                                      ")

    def test_case_5_irobot(self):
        driver = self.driver

        # TC5
        print("                                                                                                     ")
        print("                TC5                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)

        # Verify homepage
        H.verify_homepage(driver)
        delay()

        # Verify and validate Login link
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, H.login_link))).click()
        delay()

        # Title check
        self.assertIn("Login Page | iRobot®", driver.title)
        H.login_title_check(driver)

        # Loging in with existing valid credentials(email only)
        email = driver.find_element(By.XPATH, H.login_email_box)
        email.clear()
        email.send_keys(H.email_2)
        delay()
        password = driver.find_element(By.XPATH, H.login_password_box)
        password.clear()
        delay()
        driver.find_element(By.XPATH, "//input[contains(@value,'Log in')]").click()
        time.sleep(3)

        # Alert message
        alert_message = driver.find_element(By.XPATH, "//span[contains(text(),'This field is required')]")

        # TC5 results
        if self.assertIn("Login Page | iRobot®", driver.title) and alert_message:
            print("----Page has", driver.title + " as Page title")
            print("----Not able to log in with email only")
            print("                                                                                                  ")
            print("             TC5  PASS                                                                           ")
            print("        --------------------                                                                      ")
        else:
            print("----Page has", driver.title + " as Page title")
            print("----Able to log in with email only")
            print("                                                                                                  ")
            print("             TC5  FAIL                                                                           ")
            print("        --------------------                                                                      ")

    def test_case_6_irobot(self):
        driver = self.driver

        # TC6
        print("                                                                                                     ")
        print("                TC6                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)
        delay()

        # Verify homepage
        H.verify_homepage(driver)
        delay()

        # Verify and validate Login link
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.login_link))).click()
        delay()

        # Title check
        self.assertIn("Login Page | iRobot®", driver.title)
        H.login_title_check(driver)

        # Loging in with existing valid credentials(password only)
        email = driver.find_element(By.XPATH, H.login_email_box)
        email.clear()
        delay()
        password = driver.find_element(By.XPATH, H.login_password_box)
        password.clear()
        password.send_keys(H.password_1)
        delay()
        driver.find_element(By.XPATH, "//input[contains(@value,'Log in')]").click()
        time.sleep(3)

        # Alert message
        alert_message = driver.find_element(By.XPATH, "//span[contains(text(),'This field is required')]")
        delay()
        # TC6 results
        if "Login Page | iRobot®" in driver.title and alert_message:
            print("----Page has", driver.title + " as Page title")
            print("----Not able to log in with password only")
            print("                                                                                                  ")
            print("             TC6  PASS                                                                           ")
            print("        --------------------                                                                      ")
        else:
            print("----Page has", driver.title + " as Page title")
            print("----Able to log in with password only")
            print("                                                                                                  ")
            print("             TC6  FAIL                                                                           ")
            print("        --------------------                                                                      ")

    def test_case_7_irobot(self):
        driver = self.driver

        # TC7
        print("                                                                                                     ")
        print("                TC7                                                                           ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)
        delay()

        # Verify homepage
        H.verify_homepage(driver)
        delay()

        # Verify and validate Login link
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.login_link))).click()
        delay()

        # Title check
        self.assertIn("Login Page | iRobot®", driver.title)
        H.login_title_check(driver)
        delay()

        # Forgot the password link
        driver.find_element(By.XPATH, "//a[contains(text(),'Forgot your password?')]").click()
        delay()

        # Title check
        self.assertIn("Login Page | iRobot®", driver.title)
        print("----Page has", driver.title + " as Page title")
        if "Login" not in driver.title:
            raise Exception("ATTENTION! Page Title is wrong!")

        # Verifying page

        driver.find_element(By.XPATH, "//label[contains(text(),'Forgot password? Please enter your email address a')]")
        driver.find_element(By.XPATH, "//label[contains(text(),'Your reset link will expire after one hour.')]")

        # Entering invalid email
        invalid_email = driver.find_element(By.XPATH, "//input[@id='gigya-textbox-loginID']")
        invalid_email.clear()
        r = str(random.choice(["#", "!", "@", "$", "%", "&", "*", "(", ")", "-", "=", "+"]))
        invalid_email.send_keys(r)
        driver.execute_script("window.scrollTo(0,500)")
        delay()
        driver.find_element(By.XPATH, "//input[contains(@value,'Send')]").click()
        delay()
        driver.execute_script("window.scrollTo(500,0)")

        # TC7 results
        reset_link = driver.find_element(By.XPATH, '(//label[@data-binding="true"])[32]')
        spam_folder = driver.find_element(By.XPATH, '(//label[@data-binding="true"])[34]')
        please_contact = driver.find_element(By.XPATH, '(//label[@data-binding="true"])[35]')
        delay()

        if reset_link and spam_folder and please_contact:
            print("----Able to enter invalid email successfully")
            print("                                                                                                  ")
            print("             TC7  FAIL                                                                           ")
            print("        --------------------                                                                      ")
        else:
            print("----Not able to enter invalid email successfully")
            print("                                                                                                  ")
            print("             TC7  PASS                                                                           ")
            print("        --------------------                                                                      ")

    def test_case_8_irobot(self):
        driver = self.driver

        # TC8
        print("                                                                                                     ")
        print("                TC8                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)
        delay()

        # Verify homepage
        H.verify_homepage(driver)
        delay()

        # Order status link
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Order Status')])[1]"))).click()
        delay()

        # Title check
        H.login_title_check(driver)

        # Checking order status using valid existing email
        order = driver.find_element(By.XPATH, "//input[@id='trackorder-form-number']")
        order.clear()
        email = driver.find_element(By.XPATH, "//input[@id='trackorder-form-email']")
        email.clear()
        email.send_keys(H.email_2)
        driver.execute_script("window.scrollTo(0,400)")
        delay()
        driver.find_element(By.XPATH, "//button[contains(text(),'Find Order')]").click()
        delay()

        # TC8 results
        alert = driver.find_element(By.XPATH, "//div[@id='form-number-error']")
        if alert:
            print("----Not able to check order status using only email")
            print("                                                                                                  ")
            print("             TC8  PASS                                                                           ")
            print("        --------------------                                                                      ")
        else:
            print("----Able to check order status using only email")
            print("                                                                                                  ")
            print("             TC8  FAIL                                                                           ")
            print("        --------------------                                                                      ")


class EdgeAPositiveTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.EdgeOptions()
        ser = Service(r'C:/Webdriver/msedgedriver.exe')
        options.add_argument('--headless')
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
        driver = self.driver
        self.driver.set_window_size(1920, 1080)
        driver = webdriver.Edge(service=ser, options=options)
# As per unittest module, individual test should start with test

    def test_case_001_irobot(self):
        driver = self.driver
        print("                                                                                                    ")
        print("                                               I_ROBOT                                         ")
        print("                                                                                                    ")
        print("-----------------------------------------POSITIVE TEST CASES ---------------------------------------")
        print("                                                                                                    ")

        # TC001
        print("                TC001                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Check title
        H.homepage_title_check(driver)

        # Verifying correct homepage
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.homepage_logo)))
        delay()
        driver.find_element(By.ID, 'us-products')
        driver.find_element(By.ID, 'us-offers-deals')
        driver.find_element(By.ID, 'us-why-irobot')

        # Verify and validate Login link
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.login_link))).click()
        delay()

        # Title check
        self.assertIn("Login Page | iRobot®", driver.title)
        H.login_title_check(driver)

        # Creating acct
        wait = WebDriverWait(driver, 6)
        wait.until(EC.element_to_be_clickable((By.ID, "register-tab"))).click()
        delay()

        # Filling out the form
        first_name = driver.find_element(By.XPATH, "//input[@id='gigya-textbox-62368141417735550']")
        first_name.clear()
        first_name.send_keys(fake.first_name())
        last_name = driver.find_element(By.XPATH, "//input[@id='gigya-textbox-48256792335834616']")
        last_name.clear()
        last_name.send_keys(fake.last_name())
        delay()
        email = driver.find_element(By.XPATH, "//input[@id='gigya-loginID-94607575331121620']")
        email.clear()
        email.send_keys(fake.email())
        driver.execute_script("window.scrollTo(0,700)")
        time.sleep(5)
        password = driver.find_element(By.XPATH, "//input[@id='gigya-password-48204272427543900']")
        password.clear()
        password.send_keys(H.password_1)
        conf_password = driver.find_element(By.XPATH, "//input[@id='gigya-password-98920497041796370']")
        conf_password.clear()
        conf_password.send_keys(H.password_1)
        delay()

        # Check boxes
        terms = driver.find_element(By.XPATH, "//label[contains(.,'I accept Terms & Conditions*')]")
        driver.execute_script("arguments[0].click();", terms)
        time.sleep(3)
        conditions = driver.find_element(By.XPATH,
                                         '//*[@type="checkbox" and @id="gigya-checkbox-131682473014535710"]')
        driver.execute_script("arguments[0].click();", conditions)
        time.sleep(3)
        agreement = driver.find_element(By.XPATH,
                                        '//*[@type="checkbox" and @id="gigya-checkbox-84396646538548260"]')
        driver.execute_script("arguments[0].click();", agreement)
        delay()

        # Create account
        driver.find_element(By.XPATH, "//input[contains(@value,'Create account')]").click()
        delay()

        # Scrolling up
        driver.execute_script("window.scrollTo(700,0)")
        H.login_title_check(driver)
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="gigya-otp-update-form"]/div[1]/label[1]')))
        driver.find_element(By.XPATH, "//input[contains(@value,'Verify')]")
        driver.find_element(By.XPATH, "//a[contains(text(),'Send a new code')]")
        driver.save_screenshot('registration_code_msg.png')

        # TC001 results
        print("----Message 'Enter the code sent to:' is present")
        print(
            "                                                                                                     ")
        print(
            "             TC001  PASS                                                                            ")
        print(
            "        --------------------                                                                        ")

    def test_case_003_irobot(self):
        driver = self.driver

        # TC003
        print("                                                                                                     ")
        print("                TC003                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)

        # Verify homepage
        H.verify_homepage(driver)

        # Verify and validate Login link
        driver.find_element(By.XPATH, H.login_link).click()
        time.sleep(0.8)

        # Title check
        self.assertIn("Login Page | iRobot®", driver.title)
        H.login_title_check(driver)
        delay()

        # Loging in with existing valid credentials(email,password)
        email = driver.find_element(By.XPATH, H.login_email_boxEdge)
        email.clear()
        email.send_keys(H.login_email)
        delay()
        password = driver.find_element(By.XPATH, H.login_password_box)
        password.clear()
        password.send_keys(H.password_1)
        delay()
        driver.find_element(By.XPATH, "//input[contains(@value,'Log in')]").click()
        time.sleep(3)

        # Title check
        self.assertIn("Account Page | iRobot®", driver.title)
        H.account_page_title_check(driver)

        # Verify that it is an "Account page"
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'My Account')]")))
        driver.find_element(By.XPATH, "//h2[contains(text(),'Profile')]")
        delay()

        # Scroll down
        driver.execute_script("window.scrollTo(0,600)")
        delay()

        # Adding new address fake
        driver.find_element(By.XPATH, "//h2[contains(text(),'Address Book')]")
        driver.find_element(By.XPATH, "//a[@href='/en_US/add-new-address'][contains(.,'Add New')]").click()
        delay()

        # Title check
        if "Add New Address To Account | iRobot®" not in driver.title:
            raise Exception("ATTENTION! Title is different in iRobot home page")
        else:
            print("----Title check: Page has 'Add New Address To Account | iRobot®' title")

        # Verify that page is correct
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Address Book')]")))
        driver.find_element(By.XPATH, "//h2[contains(text(),'Add New Address')]")

        # Adding new Address
        address_title = driver.find_element(By.XPATH, "//input[@id='addressId']")
        place = str(random.randint(0, 50))
        place_title = "Work" + place
        address_title.send_keys(place_title)
        driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys(fake.first_name())
        time.sleep(0.2)
        driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys(fake.last_name())
        driver.execute_script("window.scrollTo(0,700)")
        driver.find_element(By.XPATH, "//input[@id='address1']").send_keys(fake.street_address())
        delay()
        state = Select(driver.find_element(By.XPATH, "//select[@id='state']"))
        state.select_by_visible_text(H.state)
        delay()
        driver.execute_script("window.scrollTo(0,600)")
        driver.find_element(By.XPATH, "//input[@id='city']").send_keys(H.city)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='zipCode']").send_keys(H.zip_code)
        time.sleep(3)
        a = str(random.randint(200, 999))
        b = str(random.randint(1000, 9999))
        phone = a + "-" + a + "-" + b
        print(phone)
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='phone']").send_keys(phone)
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(text(),'Save')]").click()
        time.sleep(3)

        # Title check
        assert "Sites-iRobotUS-Site" in driver.title
        print("----Title check: Page has", driver.title + " as Page title")

        # Verify correct page
        driver.find_element(By.XPATH, "//a[contains(text(),'Add New')]")

        # Screenshot of the new added address
        driver.save_screenshot('address book.png')
        print("----New Address was added. Check screenshot")

        # TC003 results
        print("                                                                                                     ")
        print("             TC003  PASS                                                                            ")
        print("        --------------------                                                                        ")

    def test_case_004_irobot(self):
        driver = self.driver

        # TC004
        print("                                                                                                     ")
        print("                TC004                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)

        # Verify homepage
        H.verify_homepage(driver)

        # Verifying and validating "Products" menu
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='us-products']"))).click()
        print("----Products link is clickable")
        driver.find_element(By.XPATH, "//div[contains(@class,'dropdown-menu js-dropdown-menu right-in show')]")

        # items on dropdown menu
        wait.until(EC.visibility_of_element_located((By.ID, "us-roomba-robotic-vacuums")))
        wait.until(EC.visibility_of_element_located((By.ID, 'us-braava-robotic-mops')))
        time.sleep(0.5)
        wait.until(EC.visibility_of_element_located((By.ID, 'us-shop-all')))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[contains(.,'Quick Links')])[12]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Help Me Choose')])[1]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Compare Products')])[1]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Trade in')])[1]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Financing')])[1]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'eGift Cards')]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Shop Accessories')])[1]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Compare Products')])[2]")))
        print("----'Products' link is visible and dropdown menu functional and visible")

        # TC004 Results
        print("                                                                                                     ")
        print("             TC004  PASS                                                                            ")
        print("        --------------------                                                                        ")

    def test_case_005_irobot(self):
        driver = self.driver

        # TC005
        print("                                                                                                     ")
        print("                TC005                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)

        # Verify homepage
        H.verify_homepage(driver)

        # Verification and validation of "Why iRobot" link
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.ID, "us-why-irobot"))).click()

        # Verification and validation of "Why iRobot" dropdown menu
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='dropdown-menu js-dropdown-menu right-in show']")))
        wait.until(EC.visibility_of_element_located((By.ID, "why-irobot")))
        time.sleep(0.5)

        wait.until(EC.visibility_of_element_located((By.ID, "irobot-home-app")))
        time.sleep(0.6)
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[contains(.,'Quick Links')])[16]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'P.O.O.P. Promise')]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[contains(.,"Blog")])[1]')))
        time.sleep(0.4)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Help me choose')]")))

        print("----'Why iRobot' link is visible and clickable. Dropdown menu is visible and functional.")

        # TC005 Results
        print("                                                                                                     ")
        print("             TC005  PASS                                                                            ")
        print("        --------------------                                                                        ")

    def test_case_006_irobot(self):
        driver = self.driver

        # TC006
        print("                                                                                                     ")
        print("                TC006                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)

        # Verify homepage
        H.verify_homepage(driver)

        # Verification and validation of "Accessories" link
        delay()
        try:
            WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, "us-parts-accessories"))).click()
        except TimeoutException:
            print("ATTENTION! Can't find 'Accessories' link")
        delay()

        # Verification and validation of "Accessories" dropdown menu
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@class='dropdown-menu js-dropdown-menu right-in show']")))
        wait.until(EC.visibility_of_element_located((By.ID, "us-roomba-parts-accessories")))
        time.sleep(0.5)
        wait.until(EC.visibility_of_element_located((By.ID, "us-braava-parts-accessories")))
        wait.until(EC.visibility_of_element_located((By.ID, "us-parts-bundles")))
        delay()
        wait.until(EC.visibility_of_element_located((By.ID, "us-aeris-handheld-irobot-parts-accessories")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[contains(.,'Quick Links')])[20]")))
        delay()
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(@class,'usefull-link')])[9]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(@class,'usefull-link')])[11]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Shop now')]")))

        print("----'Accessories' link is visible and clickable. Dropdown menu is visible and functional.")

        # TC006 results
        print("                                                                                                     ")
        print("             TC006  PASS                                                                            ")
        print("        --------------------                                                                        ")

    def test_case_007_irobot(self):
        driver = self.driver

        # TC007
        print("                                                                                                     ")
        print("                TC007                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)

        # Verify homepage
        H.verify_homepage(driver)

        # Verification and validation of "iRobot OS" link
        delay()
        try:
            WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, "us-irobot-os-menu"))).click()
        except WDE:
            print("ATTENTION! Can't find 'iRobot OS' link")
        delay()
        print("----'iRobot OS' link is clickable")

        # Title check:
        if "iRobot OS " not in driver.title:
            raise Exception("iRobot OS page has wrong Title!")
        else:
            print("----Title check: " + driver.title)

        # Verifying iRobot OS page
        try:
            WebDriverWait(driver, 4).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="us-irobot-os"]/div/div[1]/div/div/div/h2')))
            print("----'iRobot OS page is available")
            driver.get_screenshot_as_file('Screenshot_iRobotOS_page.png')
        except TimeoutException:
            print("ATTENTION! 'iRobot OS' page issue")
        driver.get_screenshot_as_file('iRobot_OS_page_error.png')

        # TC007 results
        print("                                                                                                     ")
        print("             TC007  PASS                                                                            ")
        print("        --------------------                                                                        ")

    def test_case_008_irobot(self):
        driver = self.driver

        # TC008
        print("                                                                                                     ")
        print("                TC008                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)
        delay()

        # Verify homepage
        H.verify_homepage(driver)

        # Verification and validation of "Shop by Lifestyle" link
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.ID, 'us-shop-by-lifestyle'))).click()
        delay()
        print("----'Shop by Lifestyle' link is clickable")

        # Verification and validation of "Shop by Lifestyle" dropdown menu
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="sg-navbar-collapse"]/div/div/nav/div[2]/ul/li[6]/div/ul')))
        delay()
        wait.until(EC.visibility_of_element_located((By.ID, "us-pet-owners-lifestyle")))
        wait.until(EC.visibility_of_element_located((By.ID, "us-tech-enthusiast-lifestyle")))
        wait.until(EC.visibility_of_element_located((By.ID, "us-busy-family-lifestyle")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[contains(.,'Quick Links')])[24]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Compare Products')])[3]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Shop all Robots')])[2]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Help Me Choose')])[2]")))

        print("----'Shop by Lifestyle' link is visible and clickable. Dropdown menu is visible and functional.")

        # TC008 results
        print("                                                                                                     ")
        print("             TC008  PASS                                                                            ")
        print("        --------------------                                                                        ")

    def tearDown(self):
        self.driver.quit()


class EdgeNegativeTests(unittest.TestCase):
    def setUp(self):
        options = webdriver.EdgeOptions()
        options.add_argument('--headless')
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
        # self.driver.maximize_window()
        self.driver.set_window_size(1920, 1080)

    # As per unittest module, individual test should start with test_

    def test_case_1_irobot(self):
        driver = self.driver
        print("                                                                                                    ")
        print("                                                I_ROBOT                                         ")
        print("                                                                                                    ")
        print("-----------------------------------------NEGATIVE TEST CASES ---------------------------------------")
        print("                                                                                                    ")
        # TC001
        print("                TC1                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Check title
        H.homepage_title_check(driver)

        # Verifying correct homepage
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.homepage_logo)))
        delay()
        driver.find_element(By.ID, 'us-products')
        driver.find_element(By.ID, 'us-offers-deals')
        driver.find_element(By.ID, 'us-why-irobot')

        # Verify and validate Login link
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, H.login_link))).click()
        delay()

        # Title check
        self.assertIn("Login Page | iRobot®", driver.title)
        H.login_title_check(driver)

        # Creating acct
        wait = WebDriverWait(driver, 6)
        wait.until(EC.element_to_be_clickable((By.ID, "register-tab"))).click()
        delay()

        # Filling out the form using invalid name
        first_name = driver.find_element(By.XPATH, "//input[@id='gigya-textbox-62368141417735550']")
        first_name.clear()

        # name = random.choice(["#", "!", "@", "$", "%", "&", "*", "(", ")", "-", "=", "+"])
        first_name.send_keys(H.name)
        last_name = driver.find_element(By.XPATH, "//input[@id='gigya-textbox-48256792335834616']")
        last_name.clear()
        last_name.send_keys(H.name)
        delay()
        email = driver.find_element(By.XPATH, "//input[@id='gigya-loginID-94607575331121620']")
        email.clear()
        email.send_keys(fake.email())
        driver.execute_script("window.scrollTo(0,700)")
        time.sleep(5)
        password = driver.find_element(By.XPATH, "//input[@id='gigya-password-48204272427543900']")
        password.clear()
        password.send_keys(H.password_1)
        conf_password = driver.find_element(By.XPATH, "//input[@id='gigya-password-98920497041796370']")
        conf_password.clear()
        conf_password.send_keys(H.password_1)
        delay()

        # Check boxes

        terms = driver.find_element(By.XPATH, "//label[contains(.,'I accept Terms & Conditions*')]")
        driver.execute_script("arguments[0].click();", terms)
        time.sleep(3)
        conditions = driver.find_element(By.XPATH, '//*[@type="checkbox" and @id="gigya-checkbox-131682473014535710"]')
        driver.execute_script("arguments[0].click();", conditions)
        time.sleep(3)
        agreement = driver.find_element(By.XPATH, '//*[@type="checkbox" and @id="gigya-checkbox-84396646538548260"]')
        driver.execute_script("arguments[0].click();", agreement)
        delay()

        # Create account
        driver.find_element(By.XPATH, "//input[contains(@value,'Create account')]").click()
        delay()

        # Scrolling up
        driver.execute_script("window.scrollTo(700,0)")
        delay()

        H.login_title_check(driver)

        delay()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="gigya-otp-update-form"]/div[1]/label[1]')))
        time.sleep(2)
        message = wait
        button = driver.find_element(By.XPATH, "//input[contains(@value,'Verify')]")

        link = driver.find_element(By.XPATH, "//a[contains(text(),'Send a new code')]")
        driver.save_screenshot('registration_code_msg.png')
        if link.is_displayed() or message.is_displayed() or button.is_displayed():
            print("----Registration is possible without valid name input")
            print("                                                                                                  ")
            print("             TC1  FAIL                                                                            ")
            print("        --------------------                                                                      ")
        else:
            print("                                                                                                  ")
            print("             TC1  PASS                                                                            ")
            print("        --------------------                                                                      ")

    def test_case_2_irobot(self):
        driver = self.driver

        # TC2
        print("                                                                                                     ")
        print("                TC2                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)

        # Verify homepage
        H.verify_homepage(driver)

        # Verify and validate Login link
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.login_link))).click()
        delay()

        # Title check
        self.assertIn("Login Page | iRobot®", driver.title)
        H.login_title_check(driver)

        # Login in with valid existing account
        email = driver.find_element(By.XPATH, H.login_email_box)
        email.clear()
        email.send_keys(H.email_1)
        delay()
        password = driver.find_element(By.XPATH, H.login_password_box)
        password.clear()
        password.send_keys(H.password_1)
        time.sleep(0.6)
        driver.find_element(By.XPATH, "//input[contains(@value,'Log in')]").click()
        delay()

        # Title check
        self.assertIn("Account Page | iRobot®", driver.title)
        H.account_page_title_check(driver)

        # Changing name to invalid name
        time.sleep(3)
        first_name = driver.find_element(By.XPATH, "//input[@id='gigya-textbox-firstName']")
        first_name.clear()
        invalid_name = str(random.randint(0, 9))
        first_name.send_keys(invalid_name)
        driver.execute_script("window.scrollTo(0,500)")
        delay()
        last_name = driver.find_element(By.XPATH, "//input[@id='gigya-textbox-lastName']")
        last_name.clear()
        last_name.send_keys(invalid_name)
        delay()
        update = driver.find_element(By.XPATH, "//input[contains(@value,'Update')]")
        if update.is_enabled():
            update.click()
            print("----User is able to update name using invalid name")
            print("                                                                                                  ")
            print("             TC2  FAIL                                                                            ")
            print("        --------------------                                                                      ")
        else:
            print("----User is not able to update name using invalid name")
            print("                                                                                                  ")
            print("             TC2  PASS                                                                           ")
            print("        --------------------                                                                      ")

    def test_case_3_irobot(self):
        driver = self.driver

        # TC3
        print("                                                                                                     ")
        print("                TC3                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)
        delay()

        # Verify homepage
        H.verify_homepage(driver)

        # Verify and validate Login link
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.login_link))).click()
        delay()

        # Title check
        self.assertIn("Login Page | iRobot®", driver.title)
        H.login_title_check(driver)

        # Login in with existing valid credentials
        email = driver.find_element(By.XPATH, H.login_email_box)
        email.clear()
        email.send_keys(H.email_1)
        delay()
        password = driver.find_element(By.XPATH, H.login_password_box)
        password.clear()
        password.send_keys(H.password_1)
        time.sleep(0.6)
        driver.find_element(By.XPATH, "//input[contains(@value,'Log in')]").click()
        delay()

        # Title check
        self.assertIn("Account Page | iRobot®", driver.title)
        H.account_page_title_check(driver)
        delay()

        # Scrolling down
        driver.execute_script("window.scrollTo(0,500)")
        delay()

        # Add address link
        driver.find_element(By.XPATH, '(//a[contains(.,"Add New")])[1]').click()
        delay()

        # Title check for new page
        self.assertIn("Add New Address To Account | iRobot®", driver.title)
        print("----Page has", driver.title + " as Page title")
        if "Add New Address To Account" not in driver.title:
            raise Exception("ATTENTION! Page Title is wrong!")
        delay()

        # Adding invalid address
        address_title = driver.find_element(By.XPATH, "//input[@id='addressId']")
        place = str(random.randint(0, 50))
        place_title = "Work" + place
        address_title.send_keys(place_title)
        first_name = driver.find_element(By.XPATH, "//input[@id='firstName']")
        first_name.send_keys(fake.first_name())
        delay()
        last_name = driver.find_element(By.XPATH, "//input[@id='lastName']")
        last_name.clear()
        last_name.send_keys(fake.last_name())
        driver.execute_script("window.scrollTo(0,500)")
        time.sleep(2)
        address = driver.find_element(By.XPATH, "//input[@id='address1']")
        address.clear()
        invalid_address = random.choices(["#", "!", "@", "$", "%", "&", "*", "(", ")", "-", "=", "+"], k=9)
        address.send_keys(invalid_address)
        delay()
        state = driver.find_element(By.XPATH, "//select[@id='state']")
        state.click()
        time.sleep(3)
        delay()
        dropdown = Select(state)
        dropdown.select_by_visible_text(H.state)
        delay()
        driver.find_element(By.XPATH, "//input[@id='city']").send_keys(H.city)
        driver.find_element(By.XPATH, "//input[@id='zipCode']").send_keys(H.zip_code)
        delay()
        a = str(random.randint(200, 999))
        b = str(random.randint(1000, 9999))
        phone = a + "-" + a + "-" + b
        driver.find_element(By.XPATH, "//input[@id='phone']").send_keys(phone)
        driver.find_element(By.XPATH, "//button[contains(text(),'Save')]").click()
        time.sleep(4)

        # Title check
        if self.assertIn("Sites-iRobotUS-Site", driver.title):
            print("----Page has", driver.title + " as Page title")
            print("----User is able to add invalid address")
            print("                                                                                                  ")
            print("             TC3  FAIL                                                                            ")
            print("        --------------------                                                                      ")
        else:
            print("----User is not able to add invalid address")
            print("                                                                                                  ")
            print("             TC3  PASS                                                                           ")
            print("        --------------------                                                                      ")

    def test_case_4_irobot(self):
        driver = self.driver

        # TC4
        print("                                                                                                     ")
        print("                TC4                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)
        delay()

        # Verify homepage
        H.verify_homepage(driver)

        # Scrolling down
        driver.execute_script("window.scrollTo(0,6500)")
        delay()

        # Signing up with invalid email
        email = driver.find_element(By.XPATH, "//input[contains(@class,'footer-email-input')]")
        email.clear()
        # a = str(random.choices(["#", "!", "@", "$", "%", "&", "*", "(", ")", "-", "=", "+"], k=4))
        b = str(random.randint(0, 100))
        # c = str(a + "@" + b)
        invalid_password = "####" + "@" + b + ".com"
        email.send_keys(invalid_password)
        delay()
        driver.find_element(By.XPATH, "//button[contains(text(),'Sign up')]").click()
        time.sleep(4)
        message = driver.find_element(By.XPATH, "/html/body/div/div[2]/p")

        # Title check anf results

        if "Your information has been submitted successfully" not in driver.title and message:
            print("----ATTENTION! Title is different")
            print("----Not able to sign up with invalid email")
            print("----User is not able to add invalid address")
            print("                                                                                                  ")
            print("             TC4  PASS                                                                           ")
            print("        --------------------                                                                      ")
        else:
            print("----Title check: Page has 'Your information has been submitted successfully' title")
            print("----Able to sign up with invalid email")
            print("                                                                                                  ")
            print("             TC4  FAIL                                                                            ")
            print("        --------------------                                                                      ")

    def test_case_5_irobot(self):
        driver = self.driver

        # TC5
        print("                                                                                                     ")
        print("                TC5                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)

        # Verify homepage
        H.verify_homepage(driver)
        delay()

        # Verify and validate Login link
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, H.login_link))).click()
        delay()

        # Title check
        self.assertIn("Login Page | iRobot®", driver.title)
        H.login_title_check(driver)

        # Loging in with existing valid credentials(email only)
        email = driver.find_element(By.XPATH, H.login_email_box)
        email.clear()
        email.send_keys(H.email_2)
        delay()
        password = driver.find_element(By.XPATH, H.login_password_box)
        password.clear()
        delay()
        driver.find_element(By.XPATH, "//input[contains(@value,'Log in')]").click()
        time.sleep(3)

        # Alert message
        alert_message = driver.find_element(By.XPATH, "//span[contains(text(),'This field is required')]")

        # TC5 results
        if self.assertIn("Login Page | iRobot®", driver.title) and alert_message:
            print("----Page has", driver.title + " as Page title")
            print("----Not able to log in with email only")
            print("                                                                                                  ")
            print("             TC5  PASS                                                                           ")
            print("        --------------------                                                                      ")
        else:
            print("----Page has", driver.title + " as Page title")
            print("----Able to log in with email only")
            print("                                                                                                  ")
            print("             TC5  FAIL                                                                           ")
            print("        --------------------                                                                      ")

    def test_case_6_irobot(self):
        driver = self.driver

        # TC6
        print("                                                                                                     ")
        print("                TC6                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)
        delay()

        # Verify homepage
        H.verify_homepage(driver)
        delay()

        # Verify and validate Login link
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.login_link))).click()
        delay()

        # Title check
        self.assertIn("Login Page | iRobot®", driver.title)
        H.login_title_check(driver)

        # Loging in with existing valid credentials(password only)
        email = driver.find_element(By.XPATH, H.login_email_box)
        email.clear()
        delay()
        password = driver.find_element(By.XPATH, H.login_password_box)
        password.clear()
        password.send_keys(H.password_1)
        delay()
        driver.find_element(By.XPATH, "//input[contains(@value,'Log in')]").click()
        time.sleep(3)

        # Alert message
        alert_message = driver.find_element(By.XPATH, "//span[contains(text(),'This field is required')]")
        delay()
        # TC6 results
        if "Login Page | iRobot®" in driver.title and alert_message:
            print("----Page has", driver.title + " as Page title")
            print("----Not able to log in with password only")
            print("                                                                                                  ")
            print("             TC6  PASS                                                                           ")
            print("        --------------------                                                                      ")
        else:
            print("----Page has", driver.title + " as Page title")
            print("----Able to log in with password only")
            print("                                                                                                  ")
            print("             TC6  FAIL                                                                           ")
            print("        --------------------                                                                      ")

    def test_case_7_irobot(self):
        driver = self.driver

        # TC7
        print("                                                                                                     ")
        print("                TC7                                                                           ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)
        delay()

        # Verify homepage
        H.verify_homepage(driver)
        delay()

        # Verify and validate Login link
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, H.login_link))).click()
        delay()

        # Title check
        self.assertIn("Login Page | iRobot®", driver.title)
        H.login_title_check(driver)

        # Forgot the password link
        driver.find_element(By.XPATH, "//a[contains(text(),'Forgot your password?')]").click()
        delay()

        # Title check
        self.assertIn("Login Page | iRobot®", driver.title)
        print("----Page has", driver.title + " as Page title")
        if "Login" not in driver.title:
            raise Exception("ATTENTION! Page Title is wrong!")

        # Verifying page

        driver.find_element(By.XPATH, "//label[contains(text(),'Forgot password? Please enter your email address a')]")
        driver.find_element(By.XPATH, "//label[contains(text(),'Your reset link will expire after one hour.')]")

        # Entering invalid email
        invalid_email = driver.find_element(By.XPATH, "//input[@id='gigya-textbox-loginID']")
        invalid_email.clear()
        r = str(random.choice(["#", "!", "@", "$", "%", "&", "*", "(", ")", "-", "=", "+"]))
        invalid_email.send_keys(r)
        driver.execute_script("window.scrollTo(0,500)")
        delay()
        driver.find_element(By.XPATH, "//input[contains(@value,'Send')]").click()
        delay()
        driver.execute_script("window.scrollTo(500,0)")

        # TC7 results
        reset_link = driver.find_element(By.XPATH, '(//label[@data-binding="true"])[32]')
        spam_folder = driver.find_element(By.XPATH, '(//label[@data-binding="true"])[34]')
        please_contact = driver.find_element(By.XPATH, '(//label[@data-binding="true"])[35]')
        delay()

        if reset_link and spam_folder and please_contact:
            print("----Able to enter invalid email successfully")
            print("                                                                                                  ")
            print("             TC7  FAIL                                                                           ")
            print("        --------------------                                                                      ")
        else:
            print("----Not able to enter invalid email successfully")
            print("                                                                                                  ")
            print("             TC7  PASS                                                                           ")
            print("        --------------------                                                                      ")

    def test_case_8_irobot(self):
        driver = self.driver

        # TC8
        print("                                                                                                     ")
        print("                TC8                                                                            ")
        print("        --------------------                                                                        ")

        # Opening iRobot site
        driver.get(H.iRobot_url)

        # Check API
        H.homepage_api_check(driver)

        # Title check
        H.homepage_title_check(driver)
        delay()

        # Verify homepage
        H.verify_homepage(driver)
        delay()

        # Order status link
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Order Status')])[1]"))).click()
        delay()

        # Title check
        H.login_title_check(driver)

        # Checking order status using valid existing email
        order = driver.find_element(By.XPATH, "//input[@id='trackorder-form-number']")
        order.clear()
        email = driver.find_element(By.XPATH, "//input[@id='trackorder-form-email']")
        email.clear()
        email.send_keys(H.email_2)
        driver.execute_script("window.scrollTo(0,400)")
        delay()
        driver.find_element(By.XPATH, "//button[contains(text(),'Find Order')]").click()
        delay()

        # TC8 results
        alert = driver.find_element(By.XPATH, "//div[@id='form-number-error']")
        if alert:
            print("----Not able to check order status using only email")
            print("                                                                                                  ")
            print("             TC8  PASS                                                                           ")
            print("        --------------------                                                                      ")
        else:
            print("----Able to check order status using only email")
            print("                                                                                                  ")
            print("             TC8  FAIL                                                                           ")
            print("        --------------------                                                                      ")


def teardown(self):
    self.driver.quit()


if __name__ == "__main__":
    unittest.main(AllureReports)
