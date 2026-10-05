# def check_age(age):
#  result = None
#  if age >= 18:
#  result = True
#  else:
#  result = False
#  return result




def check_age(age):
    return age >= 18

result = check_age(15)
print(result)











# def calculate_order_total(price, quantity):
#  total = price * quantity
#  if total > 1000:
#  total = total * 0.9
#  return total
# def calculate_cart_total(items):
#  total = 0
#  for item in items:
#  total += item.price * item.quantity
#  if total > 1000:
#  total = total * 0.9
#  return total






# DISCOUNT_THRESHOLD = 1000
# DISCOUNT_RATE = 0.9

# def apply_discount(total):
#     if total > DISCOUNT_THRESHOLD:
#         total = total * DISCOUNT_RATE
#     return total

# def calculate_order_total(price, quantity):
#     total = price * quantity
#     return apply_discount(total)


# def calculate_cart_total(items):
#     total = 0
#     for item in items:
#         total += item.price * item.quantity
#     return apply_discount(total)


# total = calculate_order_total(400, 3)
# print(total)























# class NotificationService:
#  def __init__(self):
#  self.channels = {}
#  def register_channel(self, name, handler):
#  self.channels[name] = handler
#  def send(self, channel_name, message):
#  handler = self.channels.get(channel_name)
#  if handler:
#  handler(message)
#  else:
#  raise ValueError("Unknown channel")
# # В проекте используется только email:
# service = NotificationService()
# service.register_channel("email", send_email)
# service.send("email", "Привет!")

 





# def send_email(message):
#     print("Email is sending:", message)

# send_email("Привет!")