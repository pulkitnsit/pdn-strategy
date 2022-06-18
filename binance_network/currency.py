from abstract_classes.abstract_currency import AbstractCurrency


class BUSD(AbstractCurrency):
    ADDRESS = "0xe9e7cea3dedca5984780bafc599bd69add087d56"


class WBNB(AbstractCurrency):
    ADDRESS = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"


class BETH(AbstractCurrency):
    ADDRESS = "0x2170Ed0880ac9A755fd29B2688956BD959F933F8"


class Helena(AbstractCurrency):
    DECIMAL = 10 ** 5
    ADDRESS = "0xE350b08079f9523B24029B838184f177baF961Ff"
