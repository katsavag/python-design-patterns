class SingletonClass:
    __instance = None
    __auction_name = None
    auction_bid = 0.0
    auction_holder = None

    def __init__(self):
        SingletonClass.__instance = self

    @staticmethod
    def get_instance():
        if SingletonClass.__instance is None:
            SingletonClass()
        return SingletonClass.__instance

    def set_auction_bid(self, bid):
        self.auction_bid = bid

    def set_auction_holder(self, holder):
        self.auction_holder = holder

    def print_current_auction(self):
        print("Current instance is: {}".format(self.get_instance()))
        print("Current Bid is: {}".format(self.auction_bid))
        print("Current Holder is: {}".format(self.auction_holder))
