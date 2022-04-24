# ==============================================================================
# Initiating
# ==============================================================================
import yahoo_fin.stock_info as si
import streamlit as st
from tabs import helper


def getStats(ticker):
    """
    Will create Statistics Tab for the given stock ticker
            Parameters:
                    ticker (str): Stock ticker for which Statistics tab will be created
    """
    st.title("Stats")
    st.write("Data source: Yahoo Finance")

    # Get the stock data
    tick_info = si.get_stats(ticker)
    tick_valuation = si.get_stats_valuation(ticker)
    col1, col2 = st.columns([2, 2])

    valuation_measures = tick_valuation.rename(columns={0: "Attribute", 1: "Value"})

    # Create sub section and display data in table format
    helper.createSubColumn("Valuation Measures", valuation_measures, col1)

    col1.subheader("Financial Highlights")

    helper.createSubColumn(
        "Fiscal Year", tick_info.loc[29:30, ["Attribute", "Value"]], col1
    )

    helper.createSubColumn(
        "Profitability", tick_info.loc[31:32, ["Attribute", "Value"]], col1
    )

    helper.createSubColumn(
        "Management Effectiveness", tick_info.loc[33:34, ["Attribute", "Value"]], col1
    )

    helper.createSubColumn(
        "Income Statement", tick_info.loc[35:42, ["Attribute", "Value"]], col1
    )

    helper.createSubColumn(
        "Balance Sheet", tick_info.loc[43:48, ["Attribute", "Value"]], col1
    )

    helper.createSubColumn(
        "Cash Flow Statement", tick_info.loc[49:50, ["Attribute", "Value"]], col1
    )

    col2.subheader("Trading Information")
    helper.createSubColumn(
        "Stock Price History", tick_info.loc[:6, ["Attribute", "Value"]], col2
    )

    helper.createSubColumn(
        "Share Statistics", tick_info.loc[7:18, ["Attribute", "Value"]], col2
    )

    helper.createSubColumn(
        "Dividends & Splits", tick_info.loc[19:27, ["Attribute", "Value"]], col2
    )


###############################################################################
# END
###############################################################################
