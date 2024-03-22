import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from repository import Repository


def main():
    repo = Repository()

    # get data -> repository
    portfolio = pd.read_csv(
        r"input\crisis_portfolio.csv",
        delimiter=",",
        index_col="Date",
        parse_dates=["Date"],
    )

    # Select portfolio asset prices for the middle of the crisis, 2008-2009

    # loc -> model
    # 1 dates -> begin_date = get_begin_date
    #            end_date = get_end_date => repository
    # dates dans fichier de config
    asset_prices = portfolio.loc["2008-01-01":"2009-12-31"]

    # Plot portfolio's asset prices during this time
    # plot => view
    asset_prices.plot().set_ylabel("Closing Prices, USD")
    plt.show()

    # Compute the portfolio's daily returns
    # compute => model
    asset_returns = asset_prices.pct_change()

    # get_weights => repository
    weights = [0.25, 0.25, 0.25, 0.25]

    # compute => model
    portfolio_returns = asset_returns.dot(weights)

    # Plot portfolio returns =>
    portfolio_returns.plot().set_ylabel("Daily Return, %")
    plt.show()

    # Generate the covariance matrix from portfolio asset's returns
    Covariance = asset_returns.cov()

    # Annualize the covariance using 252 trading days per year
    Covariance = Covariance * 252

    # Display the covariance matrix => view
    print(f"Covariance={Covariance}")

    portfolio_variance = np.transpose(weights) @ Covariance @ weights
    portfolio_volatility = np.sqrt(portfolio_variance)

    # display => view
    print(f"Portfolio volatility={portfolio_volatility}")

    # model
    # Calculate the 30-day rolling window of portfolio returns
    returns_windowed = portfolio_returns.rolling(30)

    # model
    # Compute the annualized volatility series
    volatility_series = returns_windowed.std() * np.sqrt(252)

    # view
    # Plot the portfolio volatility => view
    volatility_series.plot().set_ylabel("Annualized Volatility, 30-day Window")
    plt.show()


if __name__ == "__main__":
    main()
