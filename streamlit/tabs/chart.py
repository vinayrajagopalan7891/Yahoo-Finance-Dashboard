# ==============================================================================
# Initiating
# ==============================================================================
from datetime import datetime, timedelta
import streamlit as st
from datetime import datetime, timedelta
from tabs import helper
import datetime as dt
import yfinance as yfin
import mplfinance as mpf


def getChart(df, ticker):
    """
    Will create candle/line plot for the stock price
            Parameters:
                    df (dataframe): DataFrame for the stock with relevant info
                                    including Open,High,Low,Close and Volume
                    ticker (str): Stock ticker
    """
    st.title("Chart")
    st.write("Data source: Yahoo Finance")

    col1, col2, col3 = st.columns([2, 2, 2])
    type = "candle"
    days = 30

    duration = col1.selectbox("Select Duration", ["-", "1M", "6M", "YTD", "1Y", "5Y"])
    today = datetime.today().date()
    if duration == "1M":
        days = 30
    elif duration == "6M":
        days = 180
    elif duration == "YTD":
        date_time = dt.datetime(today.year, 1, 1)
        days = today - date_time.date()
        days = days.days
    elif duration == "1Y":
        days = 365
    elif duration == "5Y":
        days = 365 * 5

    chartType = col2.selectbox("Select Chart Type", ["Candle", "Line"])
    if chartType == "Line":
        type = "line"
    elif duration == "Candle":
        type = "candle"

    interval = col3.selectbox(
        "Select Interval",
        ["-", "1d", "5d", "1wk", "1mo", "3mo"],
    )

    if interval != "-":
        df = yfin.download(
            ticker, start=today - timedelta(days=days), end=today, interval=interval
        )
        duration = "-"
    elif duration != "-":
        df = yfin.download(
            ticker,
            start=today - timedelta(days=days),
            end=today,
        )

    title = ticker
    # Plot the graph
    fig = mpf.plot(
        df,
        type=type,
        style="charles",
        title=title,
        ylabel="Price ($)",
        volume=True,
        ylabel_lower="Volume",
        mav=(50),
    )

    # Turn off warning for  showPyplotGlobalUse
    st.set_option("deprecation.showPyplotGlobalUse", False)
    st.pyplot(fig)
    helper.showData(df)
    helper.addDownloadButton(df)


###############################################################################
# END
###############################################################################
