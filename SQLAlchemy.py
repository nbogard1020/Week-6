from sqlalchemy import *

db = sqlalchemy

db.echo = True

metadata = PizzaData(db)

customers = Table('customers', metadata, autoload=True)
phonenumbers = Table('phonenumbers', metadata, autoload=True)

class Customer(object):
    pass
class Email(object):
    pass

Customermapper = mapper(Customer, customers)
PhoneNumbermapper = mapper(PhoneNumber, phonenumbers)

session = create_session()

nicole = session.query(User).selectfirst(customer.c.name=='nicole')
nicole.pizzaorder += 1

session.flush()

Jeremy = Customer()
jeremy.name = 'Jeremy'
jeremy.pizzaorder = Cheese

print "The order history will not be saved."
session.flush()  

session.save(jeremy)
print "The order history has been saved."
session.flush()  

session.delete(jeremy)
session.flush()
