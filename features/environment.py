from utils.logger import logger


def before_scenario(context, scenario):
    """Execute Before Every Scenario"""

    logger.info(f"Starting Scenario: {scenario.name}")


def after_scenario(context, scenario):
    """Execute After Every Scenario"""

    logger.info(f"Completed Scenario: {scenario.name}")

    if hasattr(context, "driver"):

        context.driver.quit()

        logger.info("Browser Closed Successfully")