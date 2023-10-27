class Review:
    def __init__(self, name, review, date, rating):
        self.name = name
        self.review = review
        self.date = date
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, Review):
            return (self.name, self.review, self.date, self.rating) == (
                other.name,
                other.review,
                other.date,
                other.rating,
            )
        return False

    def __hash__(self):
        return hash((self.name, self.review, self.date, self.rating))
