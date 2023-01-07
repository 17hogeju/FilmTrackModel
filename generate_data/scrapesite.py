from bs4 import BeautifulSoup
import requests
import json

# url = 'https://www.rottentomatoes.com/browse/tv_series_browse/affiliates:hulu~sort:popular?page=5' # hulu shows
# url = 'https://www.rottentomatoes.com/browse/tv_series_browse/affiliates:netflix~sort:popular?page=5' # netflix shows
# url = 'https://www.rottentomatoes.com/browse/tv_series_browse/affiliates:hbo_max~sort:popular?page=5' # hbo max shows
# url = 'https://www.rottentomatoes.com/browse/tv_series_browse/affiliates:amazon_prime~sort:popular?page=5' # amazon prime shows
# url = 'https://www.rottentomatoes.com/browse/tv_series_browse/affiliates:disney_plus~sort:popular?page=5' # disney plus shows



# url = 'https://www.rottentomatoes.com/browse/movies_at_home/affiliates:hulu~sort:popular?page=5' # hulu movies
# url = 'https://www.rottentomatoes.com/browse/movies_at_home/affiliates:netflix~sort:popular?page=5' # netflix movies
# url = 'https://www.rottentomatoes.com/browse/movies_at_home/affiliates:hbo_max~sort:popular?page=5' # hbo max movies
# url = 'https://www.rottentomatoes.com/browse/movies_at_home/affiliates:amazon_prime~sort:popular?page=5' # amazon prime movies
url = 'https://www.rottentomatoes.com/browse/movies_at_home/affiliates:disney_plus~sort:popular?page=5' # disney plus movies

affiliate = "disney"
ttype = "movie"


def get_data(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.text


temp = get_data(url)
soup = BeautifulSoup(temp, 'lxml')

results = soup.find(id="main-page-content")
items = results.find_all("img", alt=True)
titles = []

for item in items:
    titles.append(item['alt'])

res = {
    "affiliate": affiliate,
    "ttype": ttype,
    "titles": titles
}
with open(f'../data/{affiliate}_{ttype}.json', 'w') as f:
    json.dump(res, f)
