from matplotlib import pyplot as plt


class View:
    def __init__(self, repository, model):
        print("Initializing View")
        self.repository = repository
        self.model = model

    def plot_asset_prices(self):
        print("Plot asset prices")
        self.repository.asset_prices.plot().set_ylabel(
            self.repository.asset_prices_ylabel
        )
        plt.show()

    def plot_portfolio_returns(self):
        print("Plot portfolio returns")
        self.model.portfolio_returns.plot().set_ylabel(
            self.repository.portfolio_returns_ylabel
        )
        plt.show()

    def display_covariance(self):
        print("Display covariance")
        print(f"Covariance={self.model.covariance}")

    def display_portfolio_volatility(self):
        print("Display portfolio volatility")
        print(f"Portfolio volatility={self.model.portfolio_volatility}")

    def plot_portfolio_volatility(self):
        print("Plot portfolio volatility")
        self.model.volatility_series.plot().set_ylabel(
            self.repository.portfolio_volatility_ylabel
        )
        plt.show()
