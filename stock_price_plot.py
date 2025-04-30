import matplotlib.pyplot as plt
import yfinance as yf

ticker = 'AAPL'
data = yf.download(ticker, period='1mo')

plt.plot(data.index, data['Close'])
plt.title(f"{ticker} Stock Price - Last 30 Days")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
