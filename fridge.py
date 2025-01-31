import datetime
from decimal import Decimal

goods = {
        'Яблоко':[{'amount': Decimal(1.5), 'expiration_date': datetime.date(2023,10,14)}],
         'Яйца':[{'amount': Decimal(10), 'expiration_date': datetime.date(2026,6,14)},
            {'amount': Decimal(10), 'expiration_date': datetime.date(2026,6,14)}],
         'Морковь':[{'amount': Decimal(1.5), 'expiration_date': datetime.date(2025,2,14)}]}

def get_expired(items, in_advance_days=0):
    dates = []
    for products in items.values():
        for product in products:
            if product['expiration_date'] - datetime.date.today() <= in_advance_days:
                dates.append(product['expiration_date'])
    return dates

print(get_expired(goods, 17))
        #dates.append(product['expiration_date'])
#print(dates)


        
        
