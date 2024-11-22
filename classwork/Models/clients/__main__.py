from datetime import date
from decimal import Decimal
from Clients import ClientsCollection, Client

monday = ClientsCollection(sort_by='birth_date')

a = Client(iid=14,
           fam_name='Сидорелли',
           birth_date=date(1917,11,7),
           money=Decimal('2096.16'),
           city='Петроград')

b = Client(iid=12,
           fam_name='Пупкин',
           birth_date=date(1792,9,24),
           money=Decimal('1024.32'),
           city='Париж')

c = Client(iid=46,
           fam_name='Иванов',
           birth_date=date(1960,10,12),
           money=Decimal('4096.16'),
           city='Москва')

d = Client(iid=46,
           fam_name='Иванов',
           birth_date=date(1960,10,12),
           money=Decimal('4096.16'),
           city='Москва')

e = Client(iid=46,
           fam_name='Петров',
           birth_date=date(1959,11,9),
           money=Decimal('2.72'),
           city='Рязань')

monday.append(a)
monday.append(b)
monday.append(c)
monday.append(c)
#monday.append(d)
#monday.append(e)

for x in monday:
    print(x)