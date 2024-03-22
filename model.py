import numpy as np

from constants import TRADING_DAYS_PER_YEAR


class Model:
    def __init__(self, repository):
        self.repository = repository

        self.asset_returns = self.repository.asset_prices.pct_change()
        self.portfolio_returns = self.asset_returns.dot(self.repository.weights)
        self.covariance = self.asset_returns.cov() * TRADING_DAYS_PER_YEAR
        self.portfolio_variance = np.transpose(self.repository.weights) @ self.covariance @ self.repository.weights
        self.portfolio_volatility = np.sqrt(self.portfolio_variance)
        self.returns_windowed = self.portfolio_returns.rolling(self.repository.rolling_window)
        self.volatility_series = self.returns_windowed.std() * np.sqrt(TRADING_DAYS_PER_YEAR)