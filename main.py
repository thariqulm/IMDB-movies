#Source https://bit.ly/3oiyn4p
import requests
from bs4 import BeautifulSoup
def imdb_top(imdb_top_n):
    year=input("Enter the release year(yyyy): ") 
    rating= input("Enter the minimum IMDB rating (out of 10): ")
    vote= input("Enter the minimum number of votes: ")
    print("\nBelow is the list of top %s movies released in the year %s with IMDB rating: %s+ and no.of votes: %s+"%(imdb_top_n,year,rating,vote))
    base_url = (
        f"https://www.imdb.com/search/title?title_type="
        f"feature&release_date=%s-01-01,%s-12-31&user_rating=%s.0,10.0&num_votes=%s,&sort=year,desc&count={imdb_top_n}"%(year,year,rating,vote)
    )
    source = BeautifulSoup(requests.get(base_url).content, "html.parser")
    index=1
    for m in source.findAll("div", class_="lister-item mode-advanced"):
        print("\n%d."%index + m.h3.a.text +"(%s)"%year)
        print("IMDB Rating: %s"%m.strong.text)
        index=index+1
if __name__ == "__main__":
    imdb_top(input("Enter the number of Movies required: "))