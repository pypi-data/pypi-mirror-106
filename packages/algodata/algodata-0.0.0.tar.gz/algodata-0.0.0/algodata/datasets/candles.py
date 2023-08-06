import copy

import pandas as pd
from attrdict import AttrDict as Sample
from jupyter_dash import JupyterDash
from dash import Dash
from dash.dependencies import Output, Input, State
import dash_core_components as dcc
import dash_html_components as html

from ..vis import plot_candles


class CandleDataset:
    """[summary]"""

    def __init__(self, data, lookback=10, lookahead=10, transform=None, start=None, end=None):
        super().__init__()
        self.lookback = lookback
        self.lookahead = lookahead
        self.transform = transform
        self.start = start
        self.end = end

        self.data = data
        assert len(self.data) > 0, f"no data found."

        if start:
            self.query(f"sample_time >= '{start}'")
        if end:
            self.query(f"sample_time <= '{end}'")
        assert len(self.data) > 0, f"no data found in period from {start} to {end}."

    def __len__(self):
        return len(self.data) - self.lookback - self.lookahead

    def __getitem__(self, i):
        x, y = self.get_context(i)

        if self.transform is not None:
            x, y = self.transform((x, y))

        return x, y

    def _validate_index(self, i):
        if i < 0:
            i = len(self) + i + 1
        assert i < len(self), "index out of range"
        return i

    def get_context(self, i):
        i = self._validate_index(i)
        index = i + self.lookback

        x = self.data.iloc[index - self.lookback : index]
        y = self.data.iloc[index : index + self.lookahead]

        # Intersection of x and y should be empty
        assert x.index.intersection(y.index).empty, "Subsetting is not causal."

        return Sample(data=x, index=i), Sample(data=y, index=i)

    def get_candle(self, i):
        i = self._validate_index(i)
        index = i + self.lookback

        return self.data.iloc[index]

    def get_candles(self, start_i, end_i):
        start_i = self._validate_index(start_i)
        end_i = self._validate_index(end_i - 1) + 1
        start_i += self.lookback
        end_i += self.lookback

        return self.data.iloc[start_i:end_i]

    def query(self, *args, **kwargs):
        self.data = self.data.query(*args, **kwargs)

    def plot(self, jupyter=False, **kwargs):
        if jupyter and "mode" not in kwargs:
            kwargs["mode"] = "inline"

        fig = plot_candles(self.data)

        if jupyter:
            app = JupyterDash()
        else:
            app = Dash()

        app.layout = html.Div(
            [
                dcc.Graph(figure=fig, id="candlestick"),
            ]
        )

        app.run_server(**kwargs)


class MT4CSVDataset(CandleDataset):
    """[summary]"""

    def __init__(self, path, *args, **kwargs):
        data = pd.read_csv(
            path,
            names=["date", "time", "open", "high", "low", "close", "volume_tick"],
            parse_dates={"sample_time": [0, 1]},
            index_col="sample_time",
        )
        assert len(data) > 0, f"no data found in {path}."
        super().__init__(data, *args, **kwargs)
