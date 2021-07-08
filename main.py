import sqlite3
import tkinter as tk

conn = sqlite3.connect('base.db')
c = conn.cursor()



c.execute("""CREATE TABLE list(
	first_name text,
	last_name text,
	email text,	
	phn integer
)""")




#making user to input data

def show_all():
	c.execute("SELECT * FROM list")
	items = c.fetchall()
	print("NAMES\tLAST NAME\t\tEMAILS")
	print("-----\t--------\t\t-------------")
	for i in items:
		print(i[0] + "\t" + i[1] + "\t\t" + i[2])


	print('Executed successfully')
	# Commiting conn
	conn.commit()

	# Closing conn
	conn.close()




