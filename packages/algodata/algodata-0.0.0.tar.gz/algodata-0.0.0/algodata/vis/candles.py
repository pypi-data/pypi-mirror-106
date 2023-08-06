import numpy as np
from plotly import express as px, graph_objects as go
from plotly.subplots import make_subplots


def plot_candles(ohlcv):
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(
            x=ohlcv.index,
            y=ohlcv.volume_tick,
            opacity=0.4,
            name="volume",
        )
    )

    fig.add_trace(
        go.Candlestick(
            x=ohlcv.index,
            open=ohlcv["open"],
            high=ohlcv["high"],
            low=ohlcv["low"],
            close=ohlcv["close"],
            name="OHLC",
        ),
        secondary_y=True,
    )

    vol_max = ohlcv.volume_tick.max()
    vol_scale = 10 ** np.floor(np.log10(vol_max))
    max_tick = np.ceil(vol_max / vol_scale) * vol_scale
    ticks = np.arange(0, max_tick + 1, vol_scale)
    fig.add_annotation(
        x=0,
        y=0.12,
        text="Volume",
        showarrow=False,
        textangle=-90,
        xref="paper",
        yref="paper",
        xshift=-50,
    )
    fig.update_yaxes(range=[0, ohlcv.volume_tick.max() * 4], tickvals=ticks, secondary_y=False)
    fig.update_yaxes(title_text="Price", fixedrange=False, secondary_y=True)
    fig.update_layout(
        height=700,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        hovermode="x unified",
    )

    return fig
