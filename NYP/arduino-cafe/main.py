#Dependencies
from pyfirmata import SERVO
import pyfirmata
from pyfirmata import Arduino, util

#Initialize Arduino Port
port = 'COM3'

board = Arduino(port)
iter = pyfirmata.util.Iterator(board)
iter.start()

red_led = board.get_pin('d:7:o')   # Red LED pin 7 on Arduino
XMotor = 6                         # Motor pin 6 on Arduino
green_led = board.get_pin('d:5:o') # Green LED pin 5 on Arduino

board.digital[XMotor].mode = SERVO


#Utilities
def getPercent(amount, value):
    return (amount/ 100) * value

def paddedLine(left, right, paddingLength):
	if len(left) > paddingLength:
		raise Exception("Padding length cannot be less than length of left")
	return str(left) + " "*(paddingLength - len(left)) + str(right)

def wrappedMenu(title, data_set: dict, footers: list=[], paddingLength=20, decorator="="):
	result = [None]
	maximum = 0

	for left, right in data_set.items():
		line = paddedLine(left, right, paddingLength)
		result.append(line)
		if len(line) > maximum:
			maximum = len(line)

	for line in footers:
		result.append(line)

	decoratorTopLength = (maximum - len(title)) // 2
	top = decorator*decoratorTopLength + title + decorator*decoratorTopLength
	result[0] = top
	bottom = decorator*maximum
	result.append(bottom)

	return "\n".join(result)


#Constants
filename = "menu.csv"
menu = {}
with open(filename, "r") as f:
  for line in f:
    item,price = line.rstrip("\n").split(",")
    menu.update({item: int(price)})


#Menu
footers = [
	"Purchase $10.00 (excl GST) or more and get 5% discount",
	"Membership discount: 15% (on amount after deducting Purchase discount if any)",
	"GST: 7%"
]
print(wrappedMenu("Café Menu", menu, footers))


#Input
customer_order = ""
while customer_order not in menu.keys():
    customer_order = input(f"Select the drink type: ({', '.join(menu.keys())}): ").strip()

price = menu[customer_order]

quantity = ""
while not quantity.isdigit():
    quantity = input("Select the quantity of drinks: ").strip()
quantity = int(quantity)

if quantity % 2 == 0:
    green_led.write(1)
    board.pass_time(3)
    green_led.write(0)
else:
    red_led.write(1)
    board.pass_time(3)
    red_led.write(0)

membership_values = {"Y": True, "N": False}
membership_input = ""
while membership_input not in membership_values.keys():
    membership_input = input("Are you a member (Y/N): ").strip()
membership = membership_values[membership_input]

#Calculation
initial_amount = price * quantity
purchase_discount = getPercent(initial_amount, 5) * 5 if initial_amount >= 10 else 0
membership_discount = getPercent(initial_amount - purchase_discount, 15) if membership else 0
total_before_gst = initial_amount - purchase_discount - membership_discount
gst = getPercent(total_before_gst, 7)
total_after_gst = total_before_gst - gst


#Convert amount to 2dp
initial_amount = "{:.2f}".format(initial_amount)
purchase_discount = "{:.2f}".format(purchase_discount)
membership_discount = "{:.2f}".format(membership_discount)
total_before_gst = "{:.2f}".format(total_before_gst)
gst = "{:.2f}".format(gst)
total_after_gst = "{:.2f}".format(total_after_gst)


#Receipt
items = {
	"Drink": customer_order,
	"Quantity": quantity,
	"Member": membership_input,
	"Amount": f"${initial_amount}",
	"Purchase Disc.": f"${purchase_discount}",
	"Member Disc.": f"${membership_discount}",
	"Total (bef. GST)": f"${total_before_gst}",
	"GST": f"${gst}",
	"Total (incl. GST)": f"${total_after_gst}",
}
print(wrappedMenu("Receipt", items))


#Servo movement
def setServoAngle(pin, angle):
    board.digital[pin].write(angle)
for i in range(0, 180):
    setServoAngle(XMotor, i)
