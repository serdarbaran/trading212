from trading212py import T212,Dividend
def main():

    t212 = T212()
    print(t212.account_metadata())
    print(t212.account_cash())
    print(t212.pie_list())

    dividend = Dividend()
    

if __name__ == '__main__':
    main()