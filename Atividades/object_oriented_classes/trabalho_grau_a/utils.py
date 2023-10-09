from datetime import datetime
class Utils:
    @staticmethod
    def check_date_overlap(reserved_dates, test_date):
        reserved_start_date, reserved_end_date = map(
            lambda x: datetime.strptime(x, "%d-%m-%Y"), reserved_dates
        )
        test_date = datetime.strptime(test_date, "%d-%m-%Y")

        if reserved_start_date <= test_date <= reserved_end_date:
            return True
        else:
            return False
    @staticmethod
    def is_valid_date_format(date_string):
        try:
            datetime.strptime(date_string, "%d-%m-%Y")
            return True
        except ValueError:
            return False
    @staticmethod
    def is_valid_room_number(room_number, rooms):
        try:
            room_number = int(room_number)
            for i in rooms:
                if int(i.get_numero()) == room_number:
                    return True
            return False
        except ValueError:
            return False
    @staticmethod
    def is_valid_number_format(room_number):
        try:
            room_number = int(room_number)
            return room_number > 0
        except ValueError:
            return False
    @staticmethod
    def is_valid_code_format(room_number):
        try:
            room_number = int(room_number)
            return room_number > 0
        except ValueError:
            return False
    staticmethod
    def is_valid_product_code(product_code, products):
        try:
            product_code = int(product_code)
            for i in products:
                if int(i.get_codigo()) == product_code:
                    return True
            return False
        except ValueError:
            return False
    @staticmethod
    def is_valid_category(category):
        if category in ["S","M","P"]:
            return True
        else:
            return False
    @staticmethod
    def is_valid_price(price):
        try:
            price = int(price)
            return price > 0
        except ValueError:
            return False
    
    @staticmethod
    def convert_string_to_date(date_string):
        try:
            date = datetime.strptime(date_string, "%d-%m-%Y")
            return date
        except ValueError:
            return False
    @staticmethod
    def count_days(date_range):
        start_date, end_date = date_range
        start_date = datetime.strptime(start_date, "%d-%m-%Y")
        end_date = datetime.strptime(end_date, "%d-%m-%Y")
        delta = end_date - start_date
        return delta.days