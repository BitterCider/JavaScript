import requests
import sys

try:
    amount = float(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    neat = response.json()
    rate = neat["bpi"]["USD"]["rate_float"]
    value = "{:,.4f}".format(rate * amount)
    print(f"${value}")

except requests.RequestException:
    sys.exit("Something went wrong")

except ValueError:
    sys.exit("Argument is not a number")

except IndexError:
    sys.exit("Missing argument")
