from trading212_py.t212 import T212
import trading212_py
import trading212_py.t212

def main():

    t212 = trading212_py.t212.T212()
    print(t212.get_account_details())

if __name__ == '__main__':
    main()