import logging
import os

from datetime import datetime
from datetime import date

LOG_FILE = (
    # Create the name of the file
    f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
)


logs_path = os.path.join(os.getcwd(), "logs", f"{date.today()}")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
