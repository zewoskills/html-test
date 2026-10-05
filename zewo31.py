class DataManager:
    def __init__(self, data):
        self.data = data

    def filter_by_status_and_value(self, status, value_limit):
        filtered_data = []
        for item in self.data:
            if item['a'] > value_limit and item['s'] == status:
                filtered_data.append(item)
        return filtered_data

    def calculate_total(self, items, apply_discount):
        total = 0
        for item in items:
            total += item['v']
        if apply_discount:
            total = total * 0.9
        return total