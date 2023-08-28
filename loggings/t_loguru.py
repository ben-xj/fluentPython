# %%
from loguru import logger

# %%
logger.debug("this is a debug log")

logger.info("this is a info log")

logger.warning("this is a warning log")

logger.error("this is a error log")

logger.critical("this is a critical log")

# %%
logger.info("this is {}", "a info log")
logger.info("this is {}", 3)
logger.info("this is {:.2f}", 3)

# %%
logger.add("log/file_1.log")  # sink

logger.info("this is a info log")

# %%
logger.add("log/file_2.log", rotation='10 KB')

for i in range(100):
    logger.info("this is a info log")
    logger.debug("this is a debug log")
    logger.warning("this is a warning log")
    logger.error("this is a error log")
    logger.critical("this is a critical log")
