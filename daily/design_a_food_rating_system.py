from typing import *


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):


    def changeRating(self, food: str, newRating: int) -> None:

    def highestRated(self, cuisine: str) -> str:


if __name__ == '__main__':
    foodRatings = FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
                              ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
                              [9, 12, 8, 15, 14, 7]
                              )
    foodRatings.highestRated("korean")  # return "kimchi"
    # "kimchi" is the highest rated korean food with a rating of 9.
    foodRatings.highestRated("japanese")  # return "ramen"
    # "ramen" is the highest rated japanese food with a rating of 14.
    foodRatings.changeRating("sushi", 16)  # "sushi" now has a rating of 16.
    foodRatings.highestRated("japanese")  # return "sushi"
    # "sushi" is the highest rated japanese food with a rating of 16.
    foodRatings.changeRating("ramen", 16)  # "ramen" now has a rating of 16.
    foodRatings.highestRated("japanese")  # return "ramen"
    # Both "sushi" and "ramen" have a rating of 16.
    # However, "ramen" is lexicographically smaller than "sushi".
