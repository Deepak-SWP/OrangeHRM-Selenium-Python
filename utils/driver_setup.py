from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from utils.logger import logger


def get_driver():
    """Initialize Chrome Driver"""

    try:

        logger.info("Initializing Chrome Browser")

        chrome_options = Options()

        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--remote-allow-origins=*")

        service = Service(
            ChromeDriverManager().install()
        )

        driver = webdriver.Chrome(
            service=service,
            options=chrome_options
        )

        driver.implicitly_wait(10)

        driver.set_page_load_timeout(300)

        logger.info("Chrome Browser Launched Successfully")

        return driver

    except Exception as e:

        logger.error(
            f"Driver Initialization Failed: {e}"
        )

        raise