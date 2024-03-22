from model import Model
from repository import Repository
from view import View


def main():
    repo = Repository()
    repo.get_data()
    model = Model(repo)
    view = View(repo, model)

    view.plot_asset_prices()
    view.plot_portfolio_returns()
    view.display_covariance()
    view.display_portfolio_volatility()
    view.plot_portfolio_volatility()


if __name__ == "__main__":
    main()
