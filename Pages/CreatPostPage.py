class CreatePost():

    def __init__(self, browser):
        self.browser = browser

        self.CreatePost_button_id="startPostButton"
        self.Plus_button_xpath="//*[@id='toggle_topic_list']/i"
        self.topics_select_xpath="//*[@id='list_item']"
        self.title_textbox_xpath = "//*[@id='post-title-textbox']"
        self.body_textbox_css = "#editor > div.ck.ck-reset.ck-editor.ck-rounded-corners > div.ck.ck-editor__main > div"
        self.post_button_id = "submit-post-button"
        self.AdvancedTracking_menu_css = "#navAdvancedTracking > a > p"


    def click_createpost(self):
        createpost = self.browser.find_element_by_css_selector(self.CreatePost_button_id)
        createpost.click()

    def click_plusbutton(self):
        plusbutton = self.browser.find_element_by_css_selector(self.Plus_button_xpath)
        plusbutton.click()

    def click_topics(self):
        topics = self.browser.find_element_by_css_selector(self.topics_select_xpath)
        topics.click()

    def enter_title(self,title):
        titlepost = self.browser.find_element_by_id(self.title_textbox_xpath)
        titlepost.send_keys(title)

    def enter_body(self,body):
        bodypost = self.browser.find_element_by_id(self.body_textbox_css)
        bodypost.send_keys(body)


    def click_postbutton(self):
        postbutton = self.browser.find_element_by_css_selector(self.post_button_id)
        postbutton.click()

