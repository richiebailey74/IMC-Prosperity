import pandas as pd


def round1_data_reader():
    prices_r1_d0 = pd.read_csv('data/prices_round_1_day_0.csv', sep=';')
    prices_r1_d1 = pd.read_csv('data/prices_round_1_day_-1.csv', sep=';')
    prices_r1_d2 = pd.read_csv('data/prices_round_1_day_-2.csv', sep=';')

    trades_r1_d0 = pd.read_csv('data_round1/trades_round_1_day_0_nn.csv', sep=';')
    trades_r1_d1 = pd.read_csv('data_round1/trades_round_1_day_-1nn.csv', sep=';')
    trades_r1_d2 = pd.read_csv('data_round1/trades_round_1_day_-2_nn.csv', sep=';')

    return prices_r1_d0, prices_r1_d1, prices_r1_d2, trades_r1_d0, trades_r1_d1, trades_r1_d2
