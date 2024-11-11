from .models import Order
from datetime import datetime

# добавление начальных данных
if Order.objects.count() == 0:
    Order.objects.create(datetime=datetime(2021, 12, 26, 11, 25, 34))
    Order.objects.create(datetime=datetime(2022, 5, 12, 12, 25, 34))
    Order.objects.create(datetime=datetime(2022, 5, 22, 13, 25, 34))
    Order.objects.create(datetime=datetime(2022, 8, 19, 14, 25, 34))

# получаем заказы, сделанные в 5-м месяце
orders = Order.objects.filter(datetime__month=5)
for order in orders:
    print(order.datetime)

# получаем заказы, сделанные после 5-го месяца
orders = Order.objects.filter(datetime__month__gt=5)
for order in orders:
    print(order.datetime)
