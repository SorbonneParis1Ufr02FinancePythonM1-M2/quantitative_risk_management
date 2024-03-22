import logging
from logging import config

from .helpers_serialize import get_serialized_data


def init_logger_from_file(logger_name: str, config_full_path: str):
    dict_config = get_serialized_data(full_path=config_full_path)
    log_file_path = dict_config.get("handlers").get("file").get("filename")
    config.dictConfig(dict_config)
    logger = logging.getLogger(logger_name)
    logger.info(f"start logger {logger_name}")
    logger.info(f"logger filename={log_file_path}")
    return logger, log_file_path
