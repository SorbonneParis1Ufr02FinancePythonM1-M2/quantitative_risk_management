import logging
import os

import pandas as pd
import streamlit as st

from constants import CONFIG_FILE, LOGGER_NAME
from helpers.helpers_serialize import get_serialized_data

logger = logging.getLogger(LOGGER_NAME)


@st.cache_data
def _get_data(portfolio_file_path, delimiter, index_col, parse_dates):
    logger.info("get data uncached")
    return pd.read_csv(
        portfolio_file_path,
        delimiter=delimiter,
        index_col=index_col,
        parse_dates=parse_dates,
        dayfirst=True,
    )


class Repository:
    """
    This class is responsible for all data acquisition.
    """

    def __init__(self):
        """
        self.config will contain all data from the config file.
        self.weights will contain all portfolio weights.
        self.portfolio will contain all market data.
        """
        logger.info("Initializing repository")
        self._repository_full_path = os.path.dirname(__file__)
        _config_full_path = os.path.join(os.path.dirname(__file__), CONFIG_FILE)
        logger.info(f"config_full_path={_config_full_path}")
        self.config = get_serialized_data(_config_full_path)

        # CSV file parameters
        self.portfolio_file_path = os.path.join(
            self._repository_full_path,
            self.config["input"]["input_folder"],
            self.config["input"]["input_file"],
        )
        logger.info(f"portfolio_file_path={self.portfolio_file_path}")

        self._file_delimiter = self.config["input"]["delimiter"]
        self._file_index_col = self.config["input"]["index_col"]
        self._file_parse_dates = self.config["input"]["parse_dates"]

        # date parameters
        self.begin_date = self.config["begin_date"]
        self.end_date = self.config["end_date"]
        logger.info(f"begin_date={self.begin_date}")
        logger.info(f"end_date={self.end_date}")

        # Portfolio weights data
        self.weights = self.config["weights"]
        logger.info(f"weights={self.weights}")
        self.rolling_window = self.config["rolling_window_of_portfolio_returns"]

        # Plot parameters
        self.asset_prices_ylabel = self.config["view"]["asset_prices_ylabel"]
        self.portfolio_returns_ylabel = self.config["view"]["portfolio_returns_ylabel"]
        self.portfolio_volatility_ylabel = self.config["view"][
            "portfolio_volatility_ylabel"
        ]

        # Streamlit configuration data
        self.streamlit_page_title = self.config["streamlit"]["page_title"]
        self.streamlit_layout = self.config["streamlit"]["layout"]
        self.streamlit_sidebar_state = self.config["streamlit"]["sidebar_state"]
        self.caption_plot_asset_prices = self.config["streamlit"][
            "caption_plot_asset_prices"
        ]
        self.caption_plot_portfolio_returns = self.config["streamlit"][
            "caption_plot_portfolio_returns"
        ]
        self.caption_covariance = self.config["streamlit"]["caption_covariance"]
        self.caption_portfolio_volatility = self.config["streamlit"][
            "caption_portfolio_volatility"
        ]
        self.caption_plot_portfolio_volatility = self.config["streamlit"][
            "caption_plot_portfolio_volatility"
        ]

        # Portfolio data
        self.portfolio = pd.DataFrame()

    def get_data(self):
        """
        This method is in charge of getting portfolio data from the csv file
        :return: None
        """
        logger.info("Getting portfolio")

        self.portfolio = _get_data(
            self.portfolio_file_path,
            self._file_delimiter,
            self._file_index_col,
            self._file_parse_dates,
        )

        logger.info(f"portfolio shape={self.portfolio.shape}")

