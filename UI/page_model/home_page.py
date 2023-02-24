from UI.page_model.base_page import BasePage


class HomePage(BasePage):

    @property
    def url(self):
        return 'https://' + super(HomePage, self).url + '/'
