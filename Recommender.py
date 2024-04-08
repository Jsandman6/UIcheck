def recommend_stocks(risk_tolerance, investment_horizon, initial_investment):
  # Get a list of all stocks in the S&P 500
  nasdaq_ticker_list = tickers_nasdaq()

  # Filter stocks based on risk tolerance
  low_risk_stocks = []
  medium_risk_stocks = []
  high_risk_stocks = []
  for stock in nasdaq_ticker_list:
    beta = nasdaq_ticker_list
    if beta == (1,2,3):
      low_risk_stocks.append(nasdaq_ticker_list)
    elif beta == (4,5,6):
      medium_risk_stocks.append(nasdaq_ticker_list)
    else:
      high_risk_stocks.append(nasdaq_ticker_list)

  # Filter stocks based on investment horizon
  short_term_stocks = []
  medium_term_stocks = []
  long_term_stocks = []
  for stock in low_risk_stocks:
    eps_growth = si.get_growth_earnings_per_share(stock, yearly=False)
    if eps_growth > 0.1:
      short_term_stocks.append(nasdaq_ticker_list)
    elif eps_growth > 0.05:
      medium_term_stocks.append(nasdaq_ticker_list)
    else:
      long_term_stocks.append(nasdaq_ticker_list)

  # Filter stocks based on initial investment
  affordable_stocks = []
  for stock in short_term_stocks:
    price = si.get_live_price(nasdaq_ticker_list)
    if price < initial_investment:
      affordable_stocks.append(nasdaq_ticker_list)

  # Return a list of recommended stocks
  return affordable_stocks

# Get user input
risk_tolerance = float(input("Enter your risk tolerance (1-10): "))
investment_horizon = int(input("Enter your investment horizon (years): "))
initial_investment = float(input("Enter your initial investment: "))

# Generate recommendations
recommended_stocks = recommend_stocks(risk_tolerance, investment_horizon, initial_investment)

# Print recommendations
print("Recommended stocks:",nasdaq_ticker_list)
