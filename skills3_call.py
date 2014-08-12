"""
call.py - Telemarketing script that displays the next name 
          and phone number of a Customer to call.

          This script is used to drive promotions for 
          specific customers based on their order history.
          We only want to call customers that have placed
          an order of over 20 Watermelons.

"""

# To add a column to a table:
# request = """ALTER TABLE [tablename] ADD [value1] [type];"""
# db.execute(request);

# To print column names:
# [result[0] for result in db.description]
# NOTE: For this to work, you have to execute a query first.


# I added the column last_called with type text.
# Default value is None.

# customers table - list of columns
#['id', 'email', 'givenname', 'surname', 'password', 'telephone', 
# 'tos_agree', 'gender', 'dob', 'billto_address1', 'billto_address2', 
# 'billto_city', 'billto_state', 'billto_postalcode', 'shipto_address1', 
# 'shipto_address2', 'shipto_city', 'shipto_state', 'shipto_postalcode', 
# 'region', 'last_called']

# orders table - list of colums
# ['id', 'customer_id', 'status', 'created_at', 'salesperson_id', 
# 'shipto_address1', 'shipto_address2', 'shipto_city', 'shipto_state', 
# 'shipto_postalcode', 'subtotal', 'tax', 'delivery_method', 'delivery_amount',
# 'order_total', 'delivered_at']

# order_items table - list of columns
# ['id', 'order_id', 'melon_id', 'quantity', 'unit_price', 'total_price']

#melons
#['id', 'melon_type', 'common_name', 'price', 'imgurl', 'flesh_color', 'rind_color', 
# 'seedless']

import sqlite3
import datetime

DB = None
CONN = None

# Class definition to store our customer data
class Customer(object):
	def __init__(self, c_id=None, first=None, last=None, telephone=None, last_called=None):
		self.id = c_id
		self.first = first
		self.last = last
		self.telephone = telephone
		self.last_called = last_called

	def __str__(self):
		output = " Name: %s, %s\n" % (self.last, self.first)
		output += "Phone: %s" % self.telephone

		return output

# Connect to the Database
def connect_to_db():
	global DB, CONN
	CONN = sqlite3.connect('skills3_melons.db')

	DB = CONN.cursor()


# Retrieve the next uncontacted customer record from the database.
# Return the data in a Customer class object.
#
# Remember: Our telemarketers should only be calling customers
#           who have placed orders of 20 (water)melons or more.
def get_next_customer():

# all uncalled customers who ordered greater than 20 watermelons.
	query = """SELECT c.id, c.givenname, c.surname, c.telephone, c.last_called 
			FROM customers c
			JOIN orders o ON(c.id = o.customer_id)
			JOIN order_items i ON(o.id = i.order_id)
			JOIN melons m ON(i.melon_id = m.id)
			WHERE m.melon_type = "Watermelon"
			AND c.last_called IS NOT ?
			GROUP BY c.id HAVING SUM(i.quantity) > 20;"""

	today = datetime.date.today()
	date_text = today.strftime('%Y%m%d')

	DB.execute(query, (date_text,))
	next =  DB.fetchone()
	c_id = next[0]
	first = next[1]
	last = next[2]
	telephone = next[3]
	last_called = next[4]
	c = Customer(c_id, first, last, telephone, last_called)
	return c

def display_next_to_call(customer):
	print "---------------------"
	print "Next Customer to call"
	print "---------------------\n"
	print customer
	print "\n"
	print customer.id


# Update the "last called" column for the customer
#   in the database.
def update_customer_called(customer):
	query = """UPDATE customers 
			SET last_called=?
			WHERE id=?;"""
	today = datetime.date.today()
	date_text = today.strftime('%Y%m%d')
	DB.execute(query, (date_text, customer.id))
	print "executed"

def main():
	connect_to_db()

	done = False

	while not done:
		customer = get_next_customer()
		display_next_to_call(customer)

		print "Mark this customer as called?"
		user_answer = raw_input('(y/n) > ')

		if user_answer.lower() == 'y':
			update_customer_called(customer)
			CONN.commit()
		else:
			done = True


if __name__ == '__main__':
	main()