import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        log_dir = os.path.join(project_root, "Logs")
        os.makedirs(log_dir, exist_ok=True)

        logger = logging.getLogger("nopcommerce")

        if not logger.handlers:
            log_file = os.path.join(log_dir, "automation.log")
            fhandler = logging.FileHandler(filename=log_file, mode='a')
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            fhandler.setFormatter(formatter)
            logger.addHandler(fhandler)
            logger.setLevel(logging.INFO)

        return logger

