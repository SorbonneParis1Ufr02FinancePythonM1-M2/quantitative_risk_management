import os

from constants import LOGGER_NAME, LOGGING_CONFIG_FILE
from helpers.helpers_logging import init_logger_from_file
from model import Model
from repository import Repository
from view import View


def main():
    """
    Program entry point.
    repo is Repository object. This object will contain all data including configuration data
    model is a Model object. It will handle all computations.
    view is a View object. It will be in charge of all results display tasks
    :return: None
    """
    # Log initialization
    logging_config_full_path = os.path.join(os.path.dirname(__file__), LOGGING_CONFIG_FILE)
    os.makedirs(os.path.dirname(logging_config_full_path), exist_ok=True)
    logger = init_logger_from_file(logger_name=LOGGER_NAME, config_full_path=logging_config_full_path)

    repo = Repository()
    view = View()
    view.set_repository(repo)
    view.init_streamlit()
    repo.get_data()
    model = Model(repo)

    view.set_model(model)

    view.plot_asset_prices()
    view.plot_portfolio_returns()
    view.display_covariance()
    view.display_portfolio_volatility()
    view.plot_portfolio_volatility()

    logger.info("End program")


if __name__ == "__main__":
    main()
