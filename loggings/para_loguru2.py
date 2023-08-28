from multiprocessing import Pool
from loguru import logger
import workers_a
import workers_b

"""
for multiprocessing pool
"""

if __name__ == "__main__":
    logger.remove()
    logger.add("log/file.log", enqueue=True)

    worker = workers_a.Worker()
    with Pool(4, initializer=worker.set_logger, initargs=(logger, )) as pool:
        results = pool.map(worker.work, [1, 10, 100])

    with Pool(4, initializer=workers_b.set_logger, initargs=(logger, )) as pool:
        results = pool.map(workers_b.work, [1, 10, 100])

    logger.info("Done")