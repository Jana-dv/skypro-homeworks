from Address import Address
from Mailing import Mailing

address1 = Address("111111", "Moscow", "Moskovskaya", "11a", 111)
address2 = Address("222222", "Samara", "Samarskaya", "22b", 222)
package1 = Mailing(address1, address2, 1000, "12345")
print("Отправление", package1.track, "из", package1.from_address.to_string(), "в", package1.to_address.to_string() + ".", "Стоимость", package1.cost, "рублей.")