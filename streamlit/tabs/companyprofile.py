# ==============================================================================
# Initiating
# ==============================================================================
import streamlit as st
from tabs import helper


def getCompanyProfile(ticker):
    """
    Will create Company Profile Tab for the given stock ticker
            Parameters:
                    ticker (str): Stock ticker for which Company Profile tab will be created
    """
    # Add dashboard title and description
    st.title("Company Profile")
    st.write("Data source: Yahoo Finance")

    info = helper.GetCompanyInfo(ticker)
    html_code = helper.createContainer(info, False)
    html_code = html_code + """</table>"""
    st.markdown(html_code, unsafe_allow_html=True)


###############################################################################
# END
###############################################################################
