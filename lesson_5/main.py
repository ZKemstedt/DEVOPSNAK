from mora import Mora
from watches import Watches


class WatchRepository():
    def __init__(self):
        self.watches = []
        self.max_value = 1000

    def add_watch(self, watch):
        if(watch.value > self.max_value):
            raise Exception("Go buy a vault.")
        self.watches.append(watch)

    def __str__(self):
        return "\n".join(map(str, self.watches))


def main():
    watchRepository = WatchRepository()
    watchRepository.max_value = 100000

    watchRepository.add_watch(Mora.get_default_watch())
    watchRepository.add_watch(Mora.get_default_watch())

    rolex = Watches("rolex")
    rolex.value = 50000
    watchRepository.add_watch(rolex)
    print(watchRepository)


if __name__ == "__main__":
    main()
