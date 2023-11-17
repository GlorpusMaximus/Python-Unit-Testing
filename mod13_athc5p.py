import unittest

def get_symbol():
    symbol = input("\nEnter stock symbol: ")
    return symbol

def get_chart_type():
    chartType = input("\nEnter the chart type you want (1, 2): ")
    return chartType

def get_time_series():
    timeSeries = input("\nEnter the time series option (1, 2, 3, 4): ")
    return timeSeries

def get_start_date():
    startDate = input("\nEnter the start Date (YYYY-MM-DD): ")
    return startDate

def get_end_date():
    endDate = input("\nEnter the end Date (YYYY-MM-DD): ")
    return endDate

class InputTests(unittest.TestCase):

    def test_valid_symbol(self):
        symbol = get_symbol()
        self.assertTrue(symbol.isalpha())
        self.assertTrue(symbol.isupper())
        self.assertTrue(1 <= len(symbol) <= 7)
        
    def test_chart_type(self):
        chartType = get_chart_type()
        self.assertTrue(chartType in ['1', '2'])

    def test_time_series(self):
        timeSeries = get_time_series()
        self.assertTrue(timeSeries in ['1', '2', '3', '4'])

    def test_start_date(self):
        startDate = get_start_date()
        start_year = int(startDate[:4])
        start_month = int(startDate[5:7])
        start_day = int(startDate[8:10])
        self.assertTrue(len(startDate) == 10)
        self.assertTrue(1000 <= start_year <= 9999)
        self.assertTrue(1 <= start_month <= 12)
        self.assertTrue(1 <= start_day <= 31)

    def test_end_date(self):
        endDate = get_end_date()
        end_year = int(endDate[:4])
        end_month = int(endDate[5:7])
        end_day = int(endDate[8:10])
        self.assertTrue(len(endDate) == 10)
        self.assertTrue(1000 <= end_year <= 9999)
        self.assertTrue(1 <= end_month <= 12)
        self.assertTrue(1 <= end_day <= 31)

if __name__ == '__main__':
    unittest.main()