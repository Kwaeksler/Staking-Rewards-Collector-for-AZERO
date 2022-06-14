# |--------------------------------------------------------------------------------------
# | Repository: Staking-Rewards-Collector-for-AZERO
# | Description: Create a JSON-Report with Staking-Reward-Informations for Aleph Zero
# | Version: 1.0
# | Author: Daniel H.
# | Author URI: https://github.com/Kwaeksler
# | License: GNU General Public License v3.0
# |--------------------------------------------------------------------------------------

import requests
import time

# Dezimalstelle je nach Länge der Zahl hinzufügen
def checkAmount(amount):
    digits = []
    # Ziffern des übergebenen Wertes in eine Liste schreiben
    while amount > 0:
        digits.insert(0, amount % 10)
        amount = (amount - amount % 10) // 10

    # Länge überprüfen und Trennzeichen in die Liste einfügen
    if len(digits) == 12:
        digits.insert(0, "0"+".")
    elif len(digits) == 13:
        digits.insert(1, ".")
    elif len(digits) == 14:
        digits.insert(2, ".")
    elif len(digits) == 15:
        digits.insert(3, ".")
    elif len(digits) == 16:
        digits.insert(4, ".")
    elif len(digits) == 17:
        digits.insert(5, ".")
    else:
        print("Ungültiges Zahlenformat!")

    # String aus Array zusammensetzen und Wert zurückgeben
    newAmount = ''.join(str(e) for e in digits)
    newAmount = float(newAmount)
    return newAmount;


# Historischen Preis von CoinGecko auslesen
def getSimpleHistoryPrice(CoinID, Date, targetCurrency):
    req = requests.get(f"https://api.coingecko.com/api/v3/coins/{CoinID}/history?date={Date}", headers={'User-agent':'CGBot'})

    if req.status_code == 429:
        print("-------------------------------------------------------------------------------")
        print(f"\nStatus: Zu viele API-Anfragen bei CoinGecko.com - Skript wird für {req.headers['Retry-After']} Sekunden pausiert und anschließend fortgesetzt ...")
        print(f"\nInfo: Falls keine historischen Preise benötigt werden:\nBitte den Wert der Variable 'Prices' auf 'No' setzen, das beschleunigt die Skript-Laufzeit\n")
        print("-------------------------------------------------------------------------------")
        time.sleep(int(req.headers["Retry-After"]))

        print("\nStatus: Das Skript wird fortgesetzt ...\n")
        req = requests.get(f"https://api.coingecko.com/api/v3/coins/{CoinID}/history?date={Date}", headers={'User-agent':'CGBot'})

    cgData = req.json()
    price = cgData['market_data']['current_price'][targetCurrency]

    return price

def getAccurateHistoryPrice(CoinID, Date_Unix, targetCurrency):
    date_from = Date_Unix-3600
    date_to = Date_Unix+3600

    req = requests.get(f"https://api.coingecko.com/api/v3/coins/{CoinID}/market_chart/range?vs_currency={targetCurrency}&from={date_from}&to={date_to}", headers={'User-agent':'CGBot'})

    if req.status_code == 429:
        print("-------------------------------------------------------------------------------")
        print(f"\nStatus: Zu viele API-Anfragen bei CoinGecko.com - Skript wird für {req.headers['Retry-After']} Sekunden pausiert und anschließend fortgesetzt ...")
        print(f"\nInfo: Falls keine oder nur ungenauere Tagespreise benötigt werden:\nBitte den Wert der Variable 'Prices' auf 'Fast' oder 'No' setzen, das beschleunigt die Skript-Laufzeit\n")
        print("-------------------------------------------------------------------------------")
        time.sleep(int(req.headers["Retry-After"]))

        print("\nStatus: Das Skript wird fortgesetzt ...\n")
        req = requests.get(f"https://api.coingecko.com/api/v3/coins/{CoinID}/market_chart/range?vs_currency={targetCurrency}&from={date_from}&to={date_to}", headers={'User-agent':'CGBot'})

    cgData = req.json()
    count_prices = len(cgData['prices'])

    i = 0
    price = 0

    while i < count_prices:
        price = price + cgData['prices'][i][1]
        i = i + 1

    price = price / i
    return price