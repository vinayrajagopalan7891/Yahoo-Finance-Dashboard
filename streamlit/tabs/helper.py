# ==============================================================================
# Initiating
# ==============================================================================
import streamlit as st
import pandas as pd
import yahoo_fin.stock_info as si

# Add table to show stock data
@st.cache
def GetStockData(tickers, start_date, end_date):
    return pd.concat([si.get_data(tick, start_date, end_date) for tick in tickers])


# Add table to show stock data
@st.cache
def GetCompanyInfo(ticker):
    return si.get_company_info(ticker)


@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")


def showData(df):
    """
    Will  data in dataframe using streamlits dataframe
            Parameters:
                    df (dataframe): DataFrame for the stock with relevant info
    """
    show_data = st.checkbox(label="Show data")
    if show_data:
        st.dataframe(df)


def addDownloadButton(df):
    """
    Will create download button and data in dataframe will be downloaded
            Parameters:
                    df (dataframe): DataFrame for the stock with relevant info
    """
    st.download_button(
        label="Download data as CSV",
        data=convert_df(df),
        file_name="large_df.csv",
        mime="text/csv",
    )


def plotrows(df, col):
    """
    Will encapsulate the given dataframe in HTML table tags and display
            Parameters:
                    df (dataframe): DataFrame for the stock with relevant info
                    col (column): Column to which markdown will be added
    """
    df["Attribute"] = df["Attribute"].astype(str)
    df["Value"] = df["Value"].astype(str)
    df["Attribute"] = df["Attribute"].str.replace(r"\d+$", "", regex=True)
    html_code = """<table style="margin-top: 0em;">"""
    for row in df.itertuples():
        html_code = html_code + """<tr style="border: 1px solid #888;">"""
        html_code = (
            html_code
            + """<td style="padding: 0 0.5em 0 0.5em; text-align: left;border: 1px solid #888;font_strength:"">"""
        )
        html_code = html_code + row.Attribute
        html_code = html_code + """ </td>"""
        html_code = (
            html_code
            + """<td style="padding: 0 0.5em 0 0.5em; text-align: left;border: 1px solid #888;"">"""
        )
        html_code = html_code + row.Value
        html_code = html_code + """ </td>"""
        html_code = html_code + """ </tr> """
    html_code = html_code + """</table>"""
    col.markdown(html_code, unsafe_allow_html=True)


def createSubColumn(name, df, col):
    """
    Will encapsulate the given dataframe in HTML table tags and display
            Parameters:
                    name (str) : For the header of the column
                    df (dataframe): DataFrame for the stock with relevant info
                    col (column): Column to which markdown will be added
    """
    col.subheader(name)
    plotrows(df, col)


def createheaders(df, isTitle):
    """
    Will encapsulate the header in dataframe in HTML table tags and display
            Parameters:
                    df (dataframe): DataFrame for the stock with relevant info
                    isTitle (boolean): To indicate title
    """
    html_code = """<table style="margin-top: 0em;width: 100%;">"""
    columns = list(df.columns)

    html_code = html_code + """<tr style="border: 1px solid #888;">"""
    i = 0
    html_code = (
        html_code
        + """<th style="padding: 0 0.5em 0 0.5em; text-align: left;width: 20em; height: 2em;border: 1px solid #888;"">"""
        + """ </th>"""
    )
    for column in columns:
        column = str(column)
        if i == 0 and isTitle:
            st.header(column)
            i += 1
        else:
            html_code = (
                html_code
                + """<th style="padding: 0 0.5em 0 0.5em; text-align: left;width: 20em; height: 2em;border: 1px solid #888;"">"""
            )
            html_code = html_code + column
            html_code = html_code + """ </th>"""
            i += 1

    html_code = html_code + """ </tr>"""
    return html_code


def createContainer(df, header=True, row_num=0, html_code="", isTitle=False):
    """
    Will encapsulate the given dataframe in HTML table tags and display
            Parameters:
                    df (dataframe): DataFrame for the stock with relevant info
                    header (boolean): To indicate header. Default is True
                    row_num (int): To indicate row number from where to print.
                                   Default is 0
                    html_code (str): String containing HTML tags appended.
                                     Default is empty string
                    isTitle (boolean): To indicate title

            Returns:
                    html_code (str): With tha table tags
    """
    # If header is true create a row for headers
    if header:
        html_code = createheaders(df, isTitle)

    # If empty append table tags
    if len(html_code) == 0:
        html_code = """<table style="margin-top: 0em;width: 100%;">"""

    # Iterate rows in dataframe for each tr tag
    for row in df.itertuples():
        html_code = html_code + """<tr style="border: 1px solid #888;">"""
        i = 0
        # Iterate columns in dataframe for each td tag
        for column in row[row_num:]:
            column = str(column)
            if i == 0:
                html_code = (
                    html_code
                    + """<th style="padding: 0 0.5em 0 0.5em; text-align: left; width: 20em;height: 1em;border: 1px solid #888;"">"""
                )
                html_code = html_code + column
                html_code = html_code + """ </th>"""
                i += 1
            else:
                html_code = (
                    html_code
                    + """<td style="padding: 0 0.5em 0 0.5em; text-align: left; width: 20em;height: 1em;border: 1px solid #888;"">"""
                )
                html_code = html_code + column
                html_code = html_code + """ </td>"""
                i += 1

        html_code = html_code + """ </tr> """
        i = 0

    return html_code


###############################################################################
# END
###############################################################################
