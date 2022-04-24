# ==============================================================================
# Initiating
# ==============================================================================
import yahoo_fin.stock_info as si
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tabs import helper

simulations = 200
time_horizone = 30


def getMonteCarlo(df, ticker):
    """
    Will create monte Carlo Simulation for the stock price
            Parameters:
                    df (dataframe): DataFrame for the stock with relevant info
                    ticker (str): Stock ticker
    """
    st.title("Monte Carlo")
    st.write("Data source: Yahoo Finance")

    # Take the close price
    close_price = df["close"]
    col1, col2 = st.columns([2, 2])
    daily_return = close_price.pct_change()
    daily_volatility = np.std(daily_return)

    # Add a radio box
    select_tab_1 = col1.radio("Select Number of Simulations", ["200", "500", "1000"])
    select_tab_2 = col2.radio("Select Time Horizon", ["30", "60", "90"])

    if select_tab_1 == "200":
        simulations = 200
    elif select_tab_1 == "500":
        simulations = 500
    elif select_tab_1 == "1000":
        simulations = 1000

    if select_tab_2 == "30":
        time_horizone = 30
    elif select_tab_2 == "60":
        time_horizone = 60
    elif select_tab_2 == "90":
        time_horizone = 90

    # Run the simulation
    simulation_df = pd.DataFrame()

    for i in range(simulations):

        # The list to store the next stock price
        next_price = []

        # Create the next stock price
        last_price = close_price[-1]

        for j in range(time_horizone):
            # Generate the random percentage change around the mean (0) and std (daily_volatility)
            future_return = np.random.normal(0, daily_volatility)

            # Generate the random future price
            future_price = last_price * (1 + future_return)

            # Save the price and go next
            next_price.append(future_price)
            last_price = future_price

        # Store the result of the simulation
        simulation_df[i] = next_price
    # Plot the simulation stock price in the future
    fig, ax = plt.subplots()
    fig.set_size_inches(15, 10, forward=True)

    plt.plot(simulation_df)
    plt.title(
        "Monte Carlo simulation for "
        + ticker
        + " stock price in next "
        + str(time_horizone)
        + " days"
    )
    plt.xlabel("Day")
    plt.ylabel("Price")

    plt.axhline(y=close_price[-1], color="red")
    plt.legend(["Current stock price is: " + str(np.round(close_price[-1], 2))])
    ax.get_legend().legendHandles[0].set_color("red")

    st.pyplot(fig)

    # Get the ending price of the nth day
    ending_price = simulation_df.iloc[-1:, :].values[
        0,
    ]
    # Price at 95% confidence interval
    future_price_95ci = np.percentile(ending_price, 5)

    # Value at Risk
    # 95% of the time, the losses will not be more than 16.35 USD
    VaR = close_price[-1] - future_price_95ci
    st.write("VaR at 95% confidence interval is: " + str(np.round(VaR, 2)) + " USD")


###############################################################################
# END
###############################################################################
