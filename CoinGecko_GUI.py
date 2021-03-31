from tkinter import *
from pycoingecko import CoinGeckoAPI

def quote_refresh():

    cg = CoinGeckoAPI()
    tokens = cg.get_price(ids='bitcoin,basic-attention-token,pooltogether,compound-governance-token,ethereum,uniswap',
                          vs_currencies='usd')
    price_dict = {}

    for token_id, token_info in tokens.items():
        if token_id == 'ethereum':
            price_dict['ETH'] = token_info['usd']
        elif token_id == 'bitcoin':
            price_dict['BTC'] = token_info['usd']
        elif token_id == 'compound-governance-token':
            price_dict['COMP'] = token_info['usd']
        elif token_id == 'basic-attention-token':
            price_dict['BAT'] = token_info['usd']
        elif token_id == 'uniswap':
            price_dict['UNI'] = token_info['usd']
        elif token_id == 'pooltogether':
            price_dict['POOL'] = token_info['usd']

    return price_dict

def main():

    quotes = quote_refresh()

    root = Tk()
    root.geometry('350x200')
    root.title("CoinGecko Crypto Quotes")
    a = Label(root, text=quotes)
    a.pack()


    root.mainloop()

    # print(quotes)

if __name__ == "__main__": main()