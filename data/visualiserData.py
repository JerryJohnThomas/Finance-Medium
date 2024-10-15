# visualiserData - seperate file for visualisation

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import plotly.graph_objs as go

def plot_metric_across_stocks(stock_data, metric, figsize=(10, 6)):
    base_fontsize = max(figsize[0] * 1.2, 10)
    line_width = max(figsize[0] / 10, 1)

    plt.figure(figsize=figsize)
    plt.title(f"{metric} Prices Across Multiple Stocks", fontsize=base_fontsize)

    for ticker, df in stock_data.items():
        sns.lineplot(x=df.index, y=df[metric], label=ticker, linewidth=line_width)

    plt.xlabel("Date", fontsize=base_fontsize * 0.8)
    plt.ylabel(f"{metric} (USD)", fontsize=base_fontsize * 0.8)

    # Format x-axis to show only month and year
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # Major ticks at each month
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))  # Format to show month and year

    plt.xticks(rotation=45, fontsize=base_fontsize * 0.7)
    plt.yticks(fontsize=base_fontsize * 0.7)
    plt.legend(title="Stocks", title_fontsize=base_fontsize * 0.8, loc='upper left', fontsize=base_fontsize * 0.7)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# Example usage:
# plot_metric_across_stocks(stock_data, 'Close', figsize=(10, 5))
def plot_interactive_metric_across_stocks(stock_data, metric):
    fig = go.Figure()

    for ticker, df in stock_data.items():
        fig.add_trace(go.Scatter(x=df.index, y=df[metric], mode='lines', name=ticker))

    fig.update_layout(
        title=f"{metric} Prices Across Multiple Stocks",
        xaxis_title="Date",
        yaxis_title=f"{metric} (USD)",
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True),
        legend_title="Stocks",
        template='plotly_white'
    )

    fig.show()
    return fig

# Example usage:
# plot_interactive_metric_across_stocks(stock_data, 'Close')


# single metric of one graph - not much useful
def plot_stock_metric(df, ticker, metric):
    """
    Plot a specific metric (e.g., 'Close', 'High', 'Low', 'Volume') for the stock data.

    Parameters:
    ----------
    df : pandas DataFrame
        The stock data for a particular ticker.
    ticker : str
        The stock ticker symbol.
    metric : str
        The metric to plot (e.g., 'Close', 'High', 'Low', 'Volume').

    """
    plt.figure(figsize=(14, 8))
    plt.title(f"{ticker} Stock {metric} Price", fontsize=16)

    # Plot the selected metric
    sns.lineplot(x=df.index, y=df[metric], label=metric, color='blue', linewidth=2)

    plt.xlabel("Date", fontsize=14)
    plt.ylabel(f"{metric} (USD)", fontsize=14 if metric != 'Volume' else 12)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show()

# Example: Plot Close prices
# plot_stock_metric(stock_data['AAPL'], 'AAPL', 'Close')

def plot_predictions_true_and_actual(traces, all_tickers):
    """Generate and display the Plotly plot."""
    # Create a Plotly figure
    fig = go.Figure()

    # Add all traces to the figure
    for trace in traces:
        fig.add_trace(trace)

    # Create dynamic dropdown for all tickers
    buttons = []
    for ticker in all_tickers:
        buttons.append({
            'label': ticker,
            'method': 'update',
            'args': [
                {'visible': [trace.name.startswith(ticker) for trace in traces]},
                {'title': f'{ticker} Predictions vs True Values'}
            ]
        })

    # Add an "All" option
    buttons.append({
        'label': 'All',
        'method': 'update',
        'args': [
            {'visible': [True] * len(traces)},
            {'title': 'All Stocks Predictions vs True Values'}
        ]
    })

    # Update the layout of the plot with dropdown menu
    fig.update_layout(
        title='Predictions vs True Values for Selected Stocks',
        xaxis_title='Date',
        yaxis_title='Value',
        legend_title='Legend',
        showlegend=True,
        updatemenus=[
            {
                'buttons': buttons,
                'direction': 'down',
                'showactive': True,
                'active': len(buttons) - 1  # Set the last button ('All') as active
            }
        ],
        plot_bgcolor='white',  # Set plot background color to white
        paper_bgcolor='white',  # Set paper background color to white
        xaxis=dict(
            gridcolor='lightgray',  # Set grid color for x-axis
            gridwidth=1              # Set grid width for x-axis
        ),
        yaxis=dict(
            gridcolor='lightgray',  # Set grid color for y-axis
            gridwidth=1              # Set grid width for y-axis
        )
    )
    
    # Display the plot
    fig.show()

    return fig
