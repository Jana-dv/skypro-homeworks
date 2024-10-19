from smartphone import Smartphone


catalog = [Smartphone("Samsung", "111", "+79111111111"), 
Smartphone("Huawei", "222", "+79222222222"), 
Smartphone("Sony", "333", "+79333333333"), 
Smartphone("OnePlus", "444", "+79444444444"), 
Smartphone("Nokia", "555", "+79555555555")]
for i in catalog:
    print(catalog.phone_brand)
    print(catalog.phone_model)
    print(catalog.phone_number)