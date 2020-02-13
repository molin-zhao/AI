import json
import urllib
from util.url import get_url
from util.spider import generate_statistics

f = open('site-url.json', encoding = 'utf-8')
res = f.read()
urls = json.loads(res)

coutry_url = urls['country']
municipality_directly_under_the_central_government_urls = urls['mducg']
province_urls = urls['province']
autonomous_region_urls = urls['ar']

if __name__ == '__main__':
    # apply different strategies 
    strategy_link = lambda e: e.name == 'a' and ('疫情' and "日" and "月" in e.text)
    strategy_content = lambda e: e.name == 'div' and ('累计' and '例' in e.text)
    file_path = './data'
    generate_statistics(coutry_url, strategy_link, strategy_content, file_path)
    generate_statistics(municipality_directly_under_the_central_government_urls, strategy_link, strategy_content, file_path)
    generate_statistics(province_urls, strategy_link, strategy_content, file_path)
    generate_statistics(autonomous_region_urls, strategy_link, strategy_content, file_path)
    print("all finished")

