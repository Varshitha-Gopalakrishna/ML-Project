import logging
import os
from datetime import datetime

# LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# logs_path = os.path.join(os.getcwd(),"logs", LOG_FILE)
# os.makedirs(logs_path, exist_ok=True)

# LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)


# logging.basicConfig(
#     filename= LOG_FILE_PATH,
#     format= "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level = logging.INFO
    
# )

# 1. Define logs folder path (just the directory)
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)     # ✅ Only create the folder

# 2. Define log file name separately
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)   # ✅ Combine folder + file

# 3. Setup logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    force= True   #C
)

logging.info(" Logging is configured and this is a test log entry")   #C

