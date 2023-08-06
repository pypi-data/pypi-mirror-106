from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz
from requests import get

subsidiaries = []

def sort_confidence(value):
    return value["confidence"]

def get_subs(query):
    res = get(f"https://en.wikipedia.org/w/api.php?action=opensearch&format=json&formatversion=2&search={query}&namespace=0&limit=10").json()
    companies = []
    for i,company in enumerate(res[1]):
        fuz = fuzz.ratio(query.lower(), company.lower())
        companies.append({
            "name" : company,
            "confidence" : fuz,
            "index" : i
        })

    sorted_result = sorted(companies, key=sort_confidence)
    index = sorted_result[-1]["index"]
    url = res[3][index]

    try:
        wiki_res = get(url)
        html_data = BeautifulSoup(wiki_res.text, 'html.parser')
        sub_body = html_data.find_all('table' ,class_ = 'infobox vcard')
        all_ele = sub_body[0].find_all('tr')
        for i in all_ele:
            if "Subsidiary" in str(i):
                sub_list = i.find_all('ul')[0].find_all('li')
                for name in sub_list:
                    subsidiaries.append(name.text)
        return subsidiaries
    except:
        return subsidiaries
