from bs4 import BeautifulSoup
import requests
import csv
def scrape_wiki_table(url, table_position):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup= BeautifulSoup(response.content,'html.parser')
        tables = soup.find_all('table')
        
        if 0 <= table_position < len(tables):
            table = tables[table_position]
        else:
            raise ValueError(f"Invalid table position: {table_position}")
        headers= [th.text.strip() for th in table.find('tr').find_all('th')]

        data= []
        for row in table.find_all('tr')[1:]:
            row_data={}
            cells= row.find_all('td')
            for i, cell in enumerate(cells):
                row_data[headers[i]]=cell.text.strip()
            data.append(row_data)
        with open('wiki_table_data.csv', 'w', newline='') as csvfile:
            fieldnames=headers
            writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
    except ValueError as e:
        print(f"Error: {e}")
url='https://meta.wikimedia.org/wiki/Wikipedia_article_depth/Table'
table_position = 0
scrape_wiki_table(url, table_position)
print(f"Data saved to 'wikipedia_table_data.csv'")