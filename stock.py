from tkinter import *
import yfinance as yf
import matplotlib.pyplot as plt
import os



root = Tk()

HEIGHT = 400
WIDTH = 750


canvas1 = Canvas(root, width=WIDTH, height=HEIGHT)
canvas1.pack()

background_image = PhotoImage(file=os.getcwd()+'\\landscape.png')
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

pre_entry1 = StringVar(root, value='Enter a valid Stock Ticker')
entry1 = Entry(root, bg="#6c9fce", relief=FLAT, font=('calibri', 12), textvariable=pre_entry1)
canvas1.create_window(400, 178, window=entry1)


entry2 = Entry(root, bg="#6c9fce", relief=FLAT, font=('calibri', 12))
canvas1.create_window(400, 238, window=entry2)


def getStockPrice():
    stockprice = entry1.get()
    stock = yf.Ticker(stockprice)
    label = Label(root, bg='#42c2f4', relief=FLAT, text=stock.info.get('regularMarketPrice'))
    canvas1.create_window(600, 204, window=label)


button1 = Button(text='Get the Stock Price', font=('calibri', 12), relief=FLAT,  bg="#ff8967", activebackground="#ff8967", command=getStockPrice)
canvas1.create_window(200, 180, window=button1)


def getStock():
    stockprice = entry1.get()
    stock = yf.Ticker(stockprice)
    label = Label(root, relief=FLAT, font=('calibri', 12), text=stock.recommendations)
    canvas1.create_window(200, 460, window=label)


def getStockGraph():
    stockprice = entry1.get()
    stock = yf.Ticker(stockprice)
    TIME = entry2.get()
    fig = plt.figure()
    fig.patch.set_facecolor('#919191')
    ax = plt.gca(facecolor = "#919191")
    stock_hist = stock.history(period=TIME)
    stock_hist.plot(y="Close", ax=ax, color="#FFAD00")
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title("Closing price of " + stockprice)
    plt.show()

button = Button(text='Get the Stock Graph', font=('calibri', 12), relief=FLAT,  bg="#ff8967", activebackground="#ff8967", command=getStockGraph)
canvas1.create_window(200, 240, window=button)

root.resizable(height = 0, width = 0)
root.title("Stocks")

root.mainloop()
