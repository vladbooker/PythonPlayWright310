from pages.base_page import BasePage


class UserPage(BasePage):
    def create_user_v1(self, locator, user_info):

        self.fill_text(locator.USERNAME_FIELD_LOC, user_info.username)
        self.fill_text(locator.PASSWORD_FIELD_LOC, user_info.password)
        self.fill_text(locator.CONFIRM_PASSWORD_FIELD_LOC, user_info.password)
        self.fill_text(locator.FULLNAME_FIELD_LOC, user_info.username)
        self.fill_text(locator.EMAIL_FIELD_LOC, user_info.email)
        self.click_on_elem(locator.SAVE_USER_BTN_LOC)


    def create_user_v2(self, locator, username, password, confirm_password, fullname, email):

        self.fill_text(locator.USERNAME_FIELD_LOC, username)
        self.fill_text(locator.PASSWORD_FIELD_LOC, password)
        self.fill_text(locator.CONFIRM_PASSWORD_FIELD_LOC, confirm_password)
        self.fill_text(locator.FULLNAME_FIELD_LOC, fullname)
        self.fill_text(locator.EMAIL_FIELD_LOC, email)