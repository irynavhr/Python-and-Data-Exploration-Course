# developed by Iryna Hrytsenko

import requests
from bs4 import BeautifulSoup

# get page
url = "https://www.imdb.com/title/tt6084202/"
headers = {'Accept-Language': 'en-US,en;q=0.8'}  
response = requests.get(url, headers=headers)

# check
if response.status_code != 200:
    print("Failed to retrieve page.")
    quit()

# parse
soup = BeautifulSoup(response.text, 'html.parser')

# extract....
print("\nMovie Info")

credit_blocks = soup.find_all("li", class_="ipc-metadata-list__item")
for block in credit_blocks:
    label = block.find("span", class_="ipc-metadata-list-item__label")
    if not label:
        continue
    text = label.text.strip()
    if text in ["Director", "Directors", "Writer", "Writers", "Stars"]:
        value_tags = block.find_all("a")
        people = [a.text.strip() for a in value_tags]
        print(f"{text}: {', '.join(people)}")

# awards
print("\nAwards")
awards_section = soup.find('li', attrs={'data-testid': 'award_information'})
if awards_section:
    awards_text = awards_section.text.strip()
    print(f"Awards Summary: {awards_text}")
else:
    print("No awards information found.")

# table
print("\nTop Cast")
cast_url = url + "fullcredits"  
cast_response = requests.get(cast_url, headers=headers)
cast_soup = BeautifulSoup(cast_response.text, 'html.parser')

cast_table = cast_soup.find_all("table", class_="cast_list")
if cast_table:
    cast_rows = cast_table[0].find_all("tr")[1:]  
    count = 1
    for row in cast_rows:
        columns = row.find_all('td')
        if len(columns) < 2:
            continue
        actor_tag = columns[1].find('a')
        role_tag = columns[3] if len(columns) > 3 else None
        actor = actor_tag.text.strip() if actor_tag else "Unknown"
        role = role_tag.text.strip() if role_tag else "Unknown"
        print(f"{count}. {actor} as {role}")
        count += 1
else:
    print("Top cast not found.")