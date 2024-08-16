class Loginpage:
    #Login Elements (Username,password,Login,Logout)
    username_id="emailId"
    password_id="passView"
    login_xpath="//button[@name='SignIn']"
    tv_xpath="//div[@id='myNavbar']/ul[2]/li[2]/a/span/span"
    logout_linktext="Log Out"

    def __init__(self,driver):
        self.driver=driver


    def setUsername(self,username):
        self.driver.find_element_by_id(self.username_id).clear()
        self.driver.find_element_by_id(self.username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(password)


    def clickLogin(self):
         self.driver.find_element_by_xpath(self.login_xpath).click()


    def clickTV(self):
        self.driver.find_element_by_xpath(self.tv_xpath).click()


    def clickLogout(self):
         self.driver.find_element_by_link_text(self.logout_linktext).click()






