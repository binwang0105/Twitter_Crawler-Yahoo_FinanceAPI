import time
from yahoo_finance import Share

# Download price of a company
price = Share("YHOO")

# New a file to record its current price
f = open("COMPANY_NAME" + "_STOCKPRICE.txt", "wb")

f.write(str(price.get_info()) + "\n")

# Get open stock value
f.write(str(price.get_open()) + "\n")

# Get next price
f.write(str(price.get_price()) + " at " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "\n")

for i in range(0, 28):
	# Sleep one min
	time.sleep(1)
	# Get next price
	f.write(str(price.get_price()) + " at " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "\n")

f.write("Complete!")

f.close()
