import os

from constants import LOGGER_NAME, LOGGING_CONFIG_FILE, OPEN_LOGGING_FILE
from helpers.helpers_logging import init_logger_from_file
from model import Model
from repository import Repository
from view import View


def main():
    logging_config_full_path = os.path.join(os.path.dirname(__file__), LOGGING_CONFIG_FILE)
    os.makedirs(os.path.dirname(logging_config_full_path), exist_ok=True)
    logger, logger_file_path = init_logger_from_file(logger_name=LOGGER_NAME, config_full_path=logging_config_full_path)
    logger.info(f"logger_file_path={logger_file_path}")
    if OPEN_LOGGING_FILE and logger_file_path:
        os.startfile(logger_file_path)

    repo = Repository()
    repo.get_data()
    model = Model(repo)
    view = View(repo, model)

    view.to_streamlit()
    view.plot_asset_prices()
    view.plot_portfolio_returns()
    view.display_covariance()
    view.display_portfolio_volatility()
    view.plot_portfolio_volatility()

    logger.info("End program")


if __name__ == "__main__":
    main()
