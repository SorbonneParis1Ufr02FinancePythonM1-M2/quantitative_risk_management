import logging

import numpy as np

from constants import TRADING_DAYS_PER_YEAR, LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class Model:
    """
    This class is responsible for all computations.
    """
    def __init__(self, repository):
        logger.info("Initializing Model")
        self.repository = repository

        self.asset_prices = self.repository.portfolio.loc[self.repository.begin_date: self.repository.end_date].copy(
            deep=True
        )
        logger.info(f"asset_prices shape={self.asset_prices.shape}")

        self.asset_returns = self.asset_prices.pct_change()
        logger.debug(f"Asset returns shape={self.asset_returns.shape}")
        self.portfolio_returns = self.asset_returns.dot(self.repository.weights)
        logger.debug(f"Portfolio returns shape={self.portfolio_returns.shape}")
        self.covariance = self.asset_returns.cov() * TRADING_DAYS_PER_YEAR
        logger.debug(f"covariance shape={self.covariance.shape}")
        self.portfolio_variance = (
            np.transpose(self.repository.weights)
            @ self.covariance
            @ self.repository.weights
        )
        logger.debug(f"portfolio variance={self.portfolio_variance}")
        self.portfolio_volatility = np.sqrt(self.portfolio_variance)
        logger.debug(f"portfolio_volatility={self.portfolio_volatility}")
        self.returns_windowed = self.portfolio_returns.rolling(
            self.repository.rolling_window
        )
        self.volatility_series = self.returns_windowed.std() * np.sqrt(
            TRADING_DAYS_PER_YEAR
        )
        logger.debug(f"volatility series shape={self.volatility_series.shape}")
