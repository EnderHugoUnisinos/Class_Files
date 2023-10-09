from datetime import datetime
class Utils:
    @staticmethod
    def checkDateOverlap(reservedDates, testDate):
        reservedStartDate, reservedEndDate = map(
            lambda x: datetime.strptime(x, "%d-%m-%Y"), reservedDates
        )
        testDate = datetime.strptime(testDate, "%d-%m-%Y")

        if reservedStartDate <= testDate <= reservedEndDate:
            return True
        else:
            return False
    @staticmethod
    def isValidDateFormat(dateString):
        try:
            datetime.strptime(dateString, "%d-%m-%Y")
            return True
        except ValueError:
            return False
    @staticmethod
    def isValidRoomNumber(roomNumber, rooms):
        try:
            roomNumber = int(roomNumber)
            for i in rooms:
                if int(i.getNumero()) == roomNumber:
                    return True
            return False
        except ValueError:
            return False
    @staticmethod
    def isValidNumberFormat(roomNumber):
        try:
            roomNumber = int(roomNumber)
            return roomNumber > 0
        except ValueError:
            return False
    @staticmethod
    def isValidCodeFormat(roomNumber):
        try:
            roomNumber = int(roomNumber)
            return roomNumber > 0
        except ValueError:
            return False
    @staticmethod
    def isValidProductCode(productCode, products):
        try:
            productCode = int(productCode)
            for i in products:
                if int(i.getCodigo()) == productCode:
                    return True
            return False
        except ValueError:
            return False
    @staticmethod
    def isValidCategory(category):
        if category in ["S","M","P"]:
            return True
        else:
            return False
    @staticmethod
    def isValidPrice(price):
        try:
            price = int(price)
            return price > 0
        except ValueError:
            return False  
    @staticmethod
    def convertStringToDate(dateString):
        try:
            date = datetime.strptime(dateString, "%d-%m-%Y")
            return date
        except ValueError:
            return False
    @staticmethod
    def countDays(dateRange):
        startDate, endDate = dateRange
        startDate = datetime.strptime(startDate, "%d-%m-%Y")
        endDate = datetime.strptime(endDate, "%d-%m-%Y")
        delta = endDate - startDate
        return delta.days