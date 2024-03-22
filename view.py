import logging

import streamlit as st
from matplotlib import pyplot as plt

from constants import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class View:
    def __init__(self, repository, model):
        logger.info("Initializing View")
        self.repository = repository
        self.model = model

    def plot_asset_prices(self):
        logger.info("Plot asset prices")
        st.pyplot(self.repository.asset_prices.plot(figsize=(20, 10)).set_ylabel(
            self.repository.asset_prices_ylabel).figure)

    def plot_portfolio_returns(self):
        logger.info("Plot portfolio returns")
        self.model.portfolio_returns.plot().set_ylabel(
            self.repository.portfolio_returns_ylabel
        )
        plt.show()

    def display_covariance(self):
        logger.info("Display covariance")
        print(f"Covariance={self.model.covariance}")

    def display_portfolio_volatility(self):
        logger.info("Display portfolio volatility")
        print(f"Portfolio volatility={self.model.portfolio_volatility}")

    def plot_portfolio_volatility(self):
        logger.info("Plot portfolio volatility")
        self.model.volatility_series.plot().set_ylabel(
            self.repository.portfolio_volatility_ylabel
        )
        plt.show()

    def to_streamlit(self):
        st.set_page_config(page_title=self.repository.streamlit_page_title,
                           layout=self.repository.streamlit_layout,
                           initial_sidebar_state=self.repository.streamlit_sidebar_state)
