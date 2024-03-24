import logging

import streamlit as st
from matplotlib import pyplot as plt

from constants import LOGGER_NAME
from model import Model
from repository import Repository

logger = logging.getLogger(LOGGER_NAME)


class View:
    def __init__(self):
        logger.info("Initializing View")
        self.repository = None
        self.model = None

    def init_streamlit(self):
        st.set_page_config(
            page_title=self.repository.streamlit_page_title,
            layout=self.repository.streamlit_layout,
            initial_sidebar_state=self.repository.streamlit_sidebar_state,
        )

    def set_repository(self, repository: Repository):
        self.repository = repository

    def set_model(self, model: Model):
        self.model = model

    def plot_asset_prices(self):
        plt.clf()
        logger.info("Plot asset prices")
        st.markdown(self.repository.caption_plot_asset_prices)
        st.pyplot(
            self.model.asset_prices.plot()
            .set_ylabel(self.repository.asset_prices_ylabel)
            .figure
        )

    def plot_portfolio_returns(self):
        plt.clf()
        logger.info("Plot portfolio returns")
        st.markdown(self.repository.caption_plot_portfolio_returns)
        st.pyplot(
            self.model.portfolio_returns.plot()
            .set_ylabel(self.repository.portfolio_returns_ylabel)
            .figure
        )

    def display_covariance(self):
        logger.info("Display covariance")
        st.markdown(self.repository.caption_covariance)
        st.dataframe(self.model.covariance)

    def display_portfolio_volatility(self):
        logger.info("Display portfolio volatility")
        logger.info(f"{self.model.portfolio_volatility:.2f}")
        st.metric(
            label=self.repository.caption_portfolio_volatility,
            value=f"{self.model.portfolio_volatility:.2f}",
        )

    def plot_portfolio_volatility(self):
        plt.clf()
        logger.info("Plot portfolio volatility")

        st.markdown(self.repository.caption_plot_portfolio_volatility)
        st.pyplot(
            self.model.volatility_series.plot()
            .set_ylabel(self.repository.portfolio_volatility_ylabel)
            .figure
        )
