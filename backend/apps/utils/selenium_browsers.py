from abc import ABC, abstractmethod

from django.conf import settings

from selenium import webdriver


class SeleniumBrowserBase(ABC):
    """
    Base class selenium browser base
    """

    def __init__(self):
        self.command_executor = settings.SELENIUM_HUB_URL
        self.driver = self._driver()
        super().__init__()

    def _driver(self):
        """
        Create  selenium-hub client
        :return: webdriver.Remote
        """
        options = self.options()
        return webdriver.Remote(command_executor=self.command_executor, options=options)

    @abstractmethod
    def options(self):
        """
        Browser options
        """
        pass

    def get(self, url):
        return self.driver.get(url)


class Chrome(SeleniumBrowserBase):
    def options(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=800,600")
        options.add_argument("--disable-dev-shm-usage")
        return options


class Firefox(SeleniumBrowserBase):
    def options(self):
        options = webdriver.FirefoxOptions()
        return options
