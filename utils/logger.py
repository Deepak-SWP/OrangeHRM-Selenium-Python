import logging
import os


# Hide unnecessary retry warnings
logging.getLogger("urllib3").setLevel(logging.ERROR)
logging.getLogger("WDM").setLevel(logging.ERROR)


# Create logs folder if not exists
if not os.path.exists("logs"):

    os.makedirs("logs")


# Logger Configuration
logging.basicConfig(
    filename="logs/automation.log",
    level=logging.INFO,
    format=(
        "%(asctime)s - "
        "%(levelname)s - "
        "%(message)s"
    )
)

logger = logging.getLogger()

logger.setLevel(logging.INFO)