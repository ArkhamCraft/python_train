# 私有属性和私有方法
class bankaccount:
    def __init__(self, name, money):
        self.name = name
        self.__money = money

    def bank_card(self):
        print(f'{self.name}有{self.__money}的存款')

    def cardholder(self):
        self.bank_card()


if __name__ == '__main__':
    xiaoming = bankaccount('xiaoming', 100)
    xiaoming.cardholder()
