# ==============================================================================
# Initiating
# ==============================================================================
import yahoo_fin.stock_info as si
import streamlit as st
from tabs import helper


def getFinancials(ticker):
    """
    Will create Financials Tab for the given stock ticker
            Parameters:
                    ticker (str): Stock ticker for which Financials tab will be created
    """
    st.title("Financials")
    st.write("Data source: Yahoo Finance")

    col1, col2 = st.columns([2, 2])

    # Add a radio box
    select_tab_1 = col1.radio(
        "Select tab", ["Income Statement", "Cash Flow", "Balance Sheet"]
    )

    select_tab_2 = col2.radio("Select tab", ["Yearly", "Quaterly"])

    if select_tab_1 == "Income Statement":
        if select_tab_2 == "Yearly":
            financials = si.get_income_statement(ticker, yearly=True)
        else:
            financials = si.get_income_statement(ticker, yearly=False)
    elif select_tab_1 == "Cash Flow":
        if select_tab_2 == "Yearly":
            financials = si.get_cash_flow(ticker, yearly=True)
        else:
            financials = si.get_cash_flow(ticker, yearly=False)
    elif select_tab_1 == "Balance Sheet":
        if select_tab_2 == "Yearly":
            financials = si.get_balance_sheet(ticker, yearly=True)
        else:
            financials = si.get_balance_sheet(ticker, yearly=False)

    financials = financials.astype(str)
    html_code = helper.createContainer(financials, True, 0, False)
    html_code = html_code + """</table> </br>"""
    st.markdown(html_code, unsafe_allow_html=True)


###############################################################################
# END
###############################################################################
