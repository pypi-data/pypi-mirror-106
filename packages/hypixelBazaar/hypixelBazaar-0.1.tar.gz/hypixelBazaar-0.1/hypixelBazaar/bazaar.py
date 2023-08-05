import json
import requests
from datetime import datetime


class Bazaar:

    api_url = "https://api.hypixel.net/skyblock/bazaar"

    def __init__(self):
        self.api_url = self.api_url
        self.__cache = None
        self.__cacheTime = None
        self.__makingRequest = False

    def __autoUpdate(self):
        if (
            self.__cacheTime == None
            or (datetime.now() - self.__cacheTime).total_seconds() > 20
        ):

            try:
                self.__response = requests.get(
                    "https://api.hypixel.net/skyblock/bazaar"
                )

                self.__cache = json.loads(self.__response.text)
                self.__cacheTime = datetime.fromtimestamp(
                    int(self.__cache["lastUpdated"] / 1000)
                )

            except requests.exceptions.RequestException as e:
                return None

    """
    Get basic product information

    """

    def get_buy_price(self, productName):
        self.__autoUpdate()
        return round(
            self.__cache["products"][productName]["quick_status"]["buyPrice"], 2
        )

    def get_sell_price(self, productName):
        self.__autoUpdate()
        return round(
            self.__cache["products"][productName]["quick_status"]["sellPrice"], 2
        )

    def get_product_id(self, productName):
        self.__autoUpdate()
        return self.__cache["products"][productName]["quick_status"][
            "productId"
        ].replace(":", "__")

    def get_sell_volume(self, productName):
        self.__autoUpdate()
        return self.__cache["products"][productName]["quick_status"]["sellVolume"]

    def get_buy_volume(self, productName):
        self.__autoUpdate()
        return self.__cache["products"][productName]["quick_status"]["buyVolume"]

    def get_sell_moving_week(self, productName):
        self.__autoUpdate()
        return self.__cache["products"][productName]["quick_status"]["sellMovingWeek"]

    def get_buy_moving_week(self, productName):
        self.__autoUpdate()
        return self.__cache["products"][productName]["quick_status"]["buyMovingWeek"]

    def get_buy_order_count(self, productName):
        self.__autoUpdate()
        return self.__cache["products"][productName]["quick_status"]["buyOrders"]

    def get_sell_order_count(self, productName):
        self.__autoUpdate()
        return self.__cache["products"][productName]["quick_status"]["sellOrders"]

    def get_product_list(self):
        self.__autoUpdate()
        products = []
        for name in self.__cache["products"]:
            products.append(name)

        return products
