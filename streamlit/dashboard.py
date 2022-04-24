# -*- coding: utf-8 -*-
###############################################################################
# FINANCIAL DASHBOARD
###############################################################################

# ==============================================================================
# Initiating
# ==============================================================================

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import yahoo_fin.stock_info as si
import streamlit as st
from tabs import analysis, chart, montecarlo, stats, summary, financials, companyprofile
from tabs.helper import GetStockData, GetCompanyInfo
import yfinance as yfin

# ==============================================================================
# Main body
# ==============================================================================
def run():

    try:

        # Add selection box
        global ticker, form, counter

        form = st.sidebar.form(key="my_form")
        counter = 1

        # Add the ticker selection on the sidebar
        # Get the list of stock tickers from S&P500
        ticker_list = si.tickers_sp500()

        ticker = form.selectbox("Select a ticker", ticker_list)

        # Add select begin-end date
        global start_date, end_date
        col1, col2 = form.columns(2)
        start_date = col1.date_input(
            "Start date", datetime.today().date() - timedelta(days=30)
        )
        end_date = col2.date_input("End date", datetime.today().date())

        # Add a radio box
        select_tab = st.sidebar.radio(
            "Select tab",
            [
                "Summary",
                "Chart",
                "Stats",
                "Financials",
                "Analysis",
                "Monte Carlo",
                "Company profile",
            ],
        )

        df = pd.DataFrame()
        # Show the selected tab
        if select_tab == "Company profile":
            companyprofile.getCompanyProfile(ticker)
        elif select_tab == "Chart":
            df = yfin.download([ticker], start_date, end_date)
            chart.getChart(df, ticker)
        elif select_tab == "Summary":
            df = GetStockData([ticker], start_date, end_date)
            summary.getSummary(df, ticker)
        elif select_tab == "Stats":
            stats.getStats(ticker)
        elif select_tab == "Financials":
            financials.getFinancials(ticker)
        elif select_tab == "Analysis":
            analysis.getAnalysis(ticker)
        elif select_tab == "Monte Carlo":
            df = GetStockData([ticker], start_date, end_date)
            montecarlo.getMonteCarlo(df, ticker)

        # Show the submit button
        submit = form.form_submit_button(label="Update")

    except Exception as e:
        st.error("There was an error.Please restart the application")


if __name__ == "__main__":
    run()

###############################################################################
# END
###############################################################################
