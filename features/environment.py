from utils.logger import logger
from datetime import datetime
import os


def before_scenario(context, scenario):
    """Execute Before Every Scenario"""

    logger.info(f"Starting Scenario: {scenario.name}")


def after_scenario(context, scenario):
    """Execute After Every Scenario"""

    logger.info(f"Completed Scenario: {scenario.name}")

    # Screenshot Capture on Failure
    if scenario.status == "failed":

        if not os.path.exists("screenshots/failures"):
            os.makedirs("screenshots/failures")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        screenshot_name = f"screenshots/failures/{scenario.name}_{timestamp}.png"

        context.driver.save_screenshot(screenshot_name)

        logger.error(f"Screenshot captured: {screenshot_name}")

    if hasattr(context, "driver"):

        context.driver.quit()

        logger.info("Browser Closed Successfully")