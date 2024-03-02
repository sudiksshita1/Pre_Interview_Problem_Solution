class Integer:
    _instance = None  # Class variable to hold the single instance

    def __new__(cls, value):
        if cls._instance is None:
            cls._instance = super(Integer, cls).__new__(cls)
            cls._instance.value = value
        return cls._instance

    def __init__(self, value):
        self.value = value

    def is_palindrome(self):
        # Convert integer to string and check if it's a palindrome
        str_value = str(self.value)
        return str_value == str_value[::-1]
