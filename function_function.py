def get_converter(conversion_rates, currency):
    rate = conversion_rates[currency]
    def conv_mult(value):
        return value * rate
    return conv_mult

def main():
    exch_rate = {'USD': 80.23, 'CNY': 50.30, 'GBP': 100.0}
    exchange_multipliers = dict([(key, get_converter(exch_rate, key))
                                 for key, value in exch_rate.items()])
    sales_list = {'USD': [100, 200, 300], 'GBP': [250,500,30]}
    converted_list = [(key, list(map(exchange_multipliers[key], value)))
                           for key, value in sales_list.items()]
    for elem in converted_list:
        print(elem)


    # converted_list = dict([(key, list(map(exchange_multipliers[key], value)))
    #                        for key, value in sales_list.items()])
    # print(converted_list)

main()


