class LoginPage():

    def __init__(self,browser):
        self.browser = browser

        self.signin_button_id = 'unav-desktop-header'
        self.username_textbox_id = "email"
        self.password_textbox_id = "pw"
        self.login_button_id = "login_submit"



    def click_signin(self):
        sigin = self.browser.find_element_by_id(self.signin_button_id)
        sigin.click()


    def enter_username(self, username):
        email = self.browser.find_element_by_id(self.username_textbox_id)
        email.send_keys(username)

    def enter_password(self,password):
        passwordtab = self.browser.find_element_by_id(self.password_textbox_id)
        passwordtab.send_keys(password)

    def click_login(self):
        Loginbtn = self.browser.find_element_by_xpath(self.login_button_id)
        Loginbtn.click()
