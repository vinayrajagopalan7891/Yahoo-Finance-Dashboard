# ==============================================================================
# Initiating
# ==============================================================================
import yahoo_fin.stock_info as si
import streamlit as st
from tabs import helper


def getAnalysis(ticker):
    """
    Will create Analysis Tab for the given stock ticker
            Parameters:
                    ticker (str): Stock ticker for which analysis tab will be created
    """
    st.title("Analysis")
    st.write("Data source: Yahoo Finance")

    earnings_dict = si.get_analysts_info(ticker)
    headers = [
        "Earnings Estimate",
        "Revenue Estimate",
        "Earnings History",
        "EPS Trend",
        "EPS Revisions",
        "Growth Estimates",
    ]

    # Iterate through the headers and create HTML table for each header
    for header in headers:
        df = earnings_dict[header]
        df = df.astype(str)
        html_code = helper.createContainer(df, True, 1, "", True)
        html_code = html_code + """</table>"""
        st.markdown(html_code, unsafe_allow_html=True)


###############################################################################
# END
###############################################################################
