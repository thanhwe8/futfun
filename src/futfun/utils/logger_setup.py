import logging
from datetime import datetime
from pathlib import Path

def get_logger(name: str = __name__, log_prefix: str = "futfun"):
    base_dir = Path(__file__).resolve().parent.parent
    log_dir = base_dir / "logging"
    log_dir.mkdir(exist_ok=True)

    today_str = datetime.now().strftime("%Y%m%d")
    log_file = log_dir / f"{today_str}_{log_prefix}.app"

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:  # avoid duplicate handlers
        # File handler
        file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
        file_handler.setLevel(logging.INFO)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
