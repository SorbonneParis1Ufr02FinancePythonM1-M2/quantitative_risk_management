import os

import pandas as pd

from constants import CONFIG_FILE
from helpers.helpers_serialize import get_serialized_data


class Repository:
    def __init__(self):
        print("Initializing repository")
        self._repository_full_path = os.path.dirname(__file__)
        config_full_path = os.path.join(os.path.dirname(__file__), CONFIG_FILE)
        print(f"config_full_path={config_full_path}")
        self.config = get_serialized_data(config_full_path)

        self.portfolio_file_path = os.path.join(
            self._repository_full_path,
            self.config["input"]["input_folder"],
            self.config["input"]["input_file"],
        )
        print(f"portfolio_file_path={self.portfolio_file_path}")

        self.file_delimiter = self.config["input"]["delimiter"]
        self.file_index_col = self.config["input"]["index_col"]
        self.file_parse_dates = self.config["input"]["parse_dates"]

        self.begin_date = self.config["begin_date"]
        self.end_date = self.config["end_date"]
        print(f"begin_date={self.begin_date}")
        print(f"end_date={self.end_date}")

        self.weights = self.config["weights"]
        print(f"weights={self.weights}")
        self.rolling_window = self.config["rolling_window_of_portfolio_returns"]

        self.asset_prices_ylabel = self.config["view"]["asset_prices_ylabel"]
        self.portfolio_returns_ylabel = self.config["view"]["portfolio_returns_ylabel"]
        self.portfolio_volatility_ylabel = self.config["view"][
            "portfolio_volatility_ylabel"
        ]

        self.portfolio = None
        self.asset_prices = None

    def get_data(self):
        print("Getting portfolio")
        self.portfolio = pd.read_csv(
            self.portfolio_file_path,
            delimiter=self.file_delimiter,
            index_col=self.file_index_col,
            parse_dates=self.file_parse_dates,
            dayfirst=True,
        )
        print(f"portfolio shape={self.portfolio.shape}")
        self.asset_prices = self.portfolio.loc[self.begin_date : self.end_date]
        print(f"asset_prices shape={self.asset_prices.shape}")
