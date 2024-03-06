class User:
    """Class User"""
    main_test_answers = []
    def __init__(self, username, email, password):
        self.email = email
        self.username = username
        self.password = password
        self.reviewed_wines = []
        self.wine_rating = {}