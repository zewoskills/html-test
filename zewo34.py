def process_orders(orders):
    total = 0
    valid_orders = []
    for order in orders:
        if order['status'] == 'completed':
            total += order['price']
            valid_orders.append(order)
            print("Order " + str(order['id']) + " processed, price: " + str(order['price']))
    
    avg = total / len(valid_orders)
    print("Total: " + str(total))
    print("Average: " + str(avg))
    return total, avg