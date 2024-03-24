

class Controller:
    def __init__(self, repo, model, view):
        self._repo = repo
        self._model = model
        self._view = view

    def run(self):
        self._repo.get_data()
        self._model.compute()

        self._view.plot_asset_prices()
        self._view.plot_portfolio_returns()
        self._view.display_covariance()
        self._view.display_portfolio_volatility()
        self._view.plot_portfolio_volatility()
