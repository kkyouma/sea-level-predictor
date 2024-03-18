import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x=df["Year"], y=df["CSIRO Adjusted Sea Level"], label="Data Points", s=5)

    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(
        x=df["Year"], y=df["CSIRO Adjusted Sea Level"]
    )
    x_values1 = range(df["Year"].min(), 2051)
    first_line = slope * x_values1 + intercept
    ax.plot(x_values1, first_line, color="green", label="First Regression Line")

    # Create second line of best fit
    filtered_data = df[(df["Year"] >= 2000)]
    slope2, intercept2, _, _, _ = linregress(
        x=filtered_data["Year"], y=filtered_data["CSIRO Adjusted Sea Level"]
    )
    x_values2 = range(filtered_data["Year"].min(), 2051)
    second_line = slope2 * x_values2 + intercept2
    ax.plot(x_values2, second_line, color="red", label="Second Regression Line")

    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_xlabel("Year")
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
