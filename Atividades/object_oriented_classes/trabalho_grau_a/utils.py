from datetime import datetime
class Utils:
    @staticmethod
    def check_date_overlap(reserved_dates, test_date):
        reserved_start_date, reserved_end_date = map(
            lambda x: datetime.strptime(x, "%Y-%m-%d"), reserved_dates
        )
        test_date = datetime.strptime(test_date, "%Y-%m-%d")

        if reserved_start_date <= test_date <= reserved_end_date:
            return True
        else:
            return False
    @staticmethod
    def is_valid_date_format(date_string):
        try:
            datetime.strptime(date_string, "%Y-%m-%d")
            return True
        except ValueError:
            return False
    @staticmethod
    def is_valid_room_number(room_number):
        try:
            room_number = int(room_number)
            return room_number > 0
        except ValueError:
            return False
    @staticmethod
    def is_valid_product_code(product_code):
        try:
            product_code = int(product_code)
            return product_code > 0
        except ValueError:
            return False
    @staticmethod
    def count_days(date_range):
        start_date, end_date = date_range
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        delta = end_date - start_date
        return delta.days