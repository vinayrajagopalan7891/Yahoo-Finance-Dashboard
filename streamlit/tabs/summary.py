# ==============================================================================
# Initiating
# ==============================================================================
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import yahoo_fin.stock_info as si
import streamlit as st
from datetime import datetime, timedelta
from tabs import helper
import datetime as dt


def getSummary(df, ticker):
    """
    Will create monte Carlo Simulation for the stock price
            Parameters:
                    df (dataframe): DataFrame for the stock with relevant info
                    ticker (str): Stock ticker
    """
    st.title("Summary")
    st.write("Data source: Yahoo Finance")

    # Get the stock data
    tick_info = si.get_quote_table(ticker, dict_result=False)
    html_code = helper.createContainer(tick_info, False, 1)
    html_code = html_code + """</table>"""
    st.markdown(html_code, unsafe_allow_html=True)

    # Select the duration
    duration = st.selectbox("Select Duration", ["-", "1M", "6M", "YTD", "1Y", "5Y"])
    today = datetime.today().date()
    if duration == "1M":
        df = helper.GetStockData(
            ticker,
            today - timedelta(days=30),
            today,
        )
    elif duration == "6M":
        df = helper.GetStockData(
            ticker,
            today - timedelta(days=180),
            today,
        )
    elif duration == "YTD":
        date_time = dt.datetime(today.year, 1, 1)
        days = today - date_time.date()
        df = helper.GetStockData(
            ticker,
            today - timedelta(days=days.days),
            today,
        )
    elif duration == "1Y":
        df = helper.GetStockData(
            ticker,
            today - timedelta(days=365),
            today,
        )
    elif duration == "5Y":
        df = helper.GetStockData(
            ticker,
            today - timedelta(days=365 * 5),
            today,
        )

    tick_info = tick_info.set_index("attribute")
    close_price = tick_info.loc["Previous Close", "value"]
    open = tick_info.loc["Open", "value"]

    # Check if stock is in profit or loss
    if open > close_price:
        format = "green"
    else:
        format = "red"

    # Plot the graph
    fig, ax = plt.subplots(figsize=(10, 5))
    x = list(df.index)
    y1 = df["close"]
    ymin, ymax = min(y1), max(y1)
    xmin, xmax = min(x), max(x)
    ax.fill_between(x, y1, facecolor=format, alpha=0.5)
    plt.xlim([xmin, xmax])
    plt.ylim([ymin - 10, 1.02 * ymax])
    ax.set_xlabel("Date")
    ax.set_ylabel("Close_Price")
    st.pyplot(fig)

    helper.showData(df)
    helper.addDownloadButton(df)


###############################################################################
# END
###############################################################################
