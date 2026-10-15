import requests
from bs4 import BeautifulSoup


def print_grid_from_google_doc(url):
    # Get the published Google Doc
    response = requests.get(url)
    response.raise_for_status()

    # Parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the table
    table = soup.find("table")

    if table is None:
        raise ValueError("Could not find the data table in the document.")

    points = []
    max_x = 0
    max_y = 0

    # Read every row except the header
    rows = table.find_all("tr")[1:]

    for row in rows:
        cells = row.find_all(["td", "th"])

        if len(cells) < 3:
            continue

        x = int(cells[0].get_text(strip=True))
        char = cells[1].get_text()
        y = int(cells[2].get_text(strip=True))

        points.append((x, y, char))

        max_x = max(max_x, x)
        max_y = max(max_y, y)

    # Create an empty grid
    grid = [[" " for _ in range(max_x + 1)]
            for _ in range(max_y + 1)]

    # Put characters into their coordinates
    for x, y, char in points:
        grid[y][x] = char

    # y increases upward, so print from max_y down to 0
    for y in range(max_y, -1, -1):
        print("".join(grid[y]))
url= https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub