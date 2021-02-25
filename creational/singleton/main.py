from creational.singleton.SingletonClass import SingletonClass


def main():
    print("Singleton Design Pattern")

    singleton_1 = SingletonClass.get_instance()
    singleton_1.set_auction_bid(10)
    singleton_1.set_auction_holder("Scrooge McDuck")
    singleton_1.print_current_auction()

    singleton_2 = SingletonClass.get_instance()
    singleton_2.set_auction_bid(1000)
    singleton_2.set_auction_holder("Micky Mouse")
    singleton_2.print_current_auction()


if __name__ == "__main__":
    main()
