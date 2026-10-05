REVENUE_TARGET = 10000


# Блок 1
def read_sales_data(file_path):
    sales = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            sales.append({
                "item": parts[0],
                "price": float(parts[1]),
                "status": parts[2]
            })
    return sales


# Блок 2
def filter_valid_sales(sales):
    valid_sales = []
    for sale in sales:
        if sale["status"] == "completed" and sale["price"] > 0:
            valid_sales.append(sale)
    return valid_sales


# Блок 3
def calculate_total_revenue(valid_sales, discount_rate):
    total_revenue = 0
    for sale in valid_sales:
        discounted_price = sale["price"] * (1 - discount_rate)
        total_revenue += discounted_price
    return total_revenue


# Блок 4
def save_sales_report(total_revenue, valid_sales, report_path="report.txt"):
    report = f"Total Revenue: ${total_revenue:.2f}\nValid Transactions: {len(valid_sales)}"
    with open(report_path, "w") as file:
        file.write(report)


# Блок 5
def notify_stakeholders(total_revenue):
    if total_revenue > REVENUE_TARGET:
        print("Sending email to CEO: Target reached!")
    else:
        print("Sending email to Manager: Target not reached.")


def main(file_path, discount_rate):
    sales = read_sales_data(file_path)
    valid_sales = filter_valid_sales(sales)
    total_revenue = calculate_total_revenue(valid_sales, discount_rate)
    save_sales_report(total_revenue, valid_sales)
    notify_stakeholders(total_revenue)


if __name__ == "__main__":
    main("sales.csv", discount_rate=0.1)