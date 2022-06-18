from abstract_classes.abstract_currency import AbstractCurrency


class AVAXUSDC(AbstractCurrency):
    ADDRESS = "0xa7d7079b0fead91f3e65f86e8915cb59c1a4c664"
    DECIMAL = 10 ** 6


class THORUS(AbstractCurrency):
    ADDRESS = "0xae4aa155d2987b454c29450ef4f862cf00907b61"


class STHORUS(AbstractCurrency):
    ADDRESS = "0x63468133ed352e602beb61dd254d6060ad2fe419"


class STATIK(AbstractCurrency):
    ADDRESS = "0x97d367A5f900F5c9dB4370D0D801Fc52332244C7"
