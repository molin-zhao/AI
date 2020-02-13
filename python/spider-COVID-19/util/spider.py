import os
from .url import get_url, get_cookie
from .file import write_to_file

# strategy for parsing COVID-19 statistic links
def strategy_for_href(soup, base_url, strategy):
    href_list = []
    for li in soup.find_all("li"):
        for a in li.find_all(strategy, href = True):
            href = a['href']
            if href.startswith('../'):
                trimmed_href = href.strip('..')
                trimmed_base_url = base_url[:base_url.rfind('/')]
                href_link = trimmed_base_url + trimmed_href
                href_list.append(href_link)
            elif href.startswith('./'):
                trimmed_href = href.strip('.')
                href_link = base_url + trimmed_href
                href_list.append(href_link)
            elif href.startswith('http'):
                href_list.append(href)
            else:
                continue
    return href_list

# strategy for parsing COVID-19 statistical information
def strategy_for_content(soup, base_url, strategy):
    print(base_url)
    content = ""
    for div in soup.find_all(strategy):
        trimmed_text = div.text.replace(' ', '').replace('\r', '').replace('\n', '')
        content += trimmed_text
    return content

# generate statistics and write to file
def generate_statistics(urls, strategy_link, strategy_content, data_path = "../data"):
    if type(urls) == list:
        for i in range(len(urls)):
            for key, value in urls[i].items():
                # headers = {
                #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
                #     'Cookie': get_cookie(urls)
                # }
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
                }
                soup = get_url(value, headers)
                href_list = strategy_for_href(soup, value, strategy_link)
                for j in range(len(href_list)):
                    link = href_list[j]
                    delicious_soup = get_url(link, headers)
                    statistics_content = strategy_for_content(delicious_soup, link, strategy_content)
                    folder_name = data_path + '/' + key
                    if not os.path.exists(folder_name):
                        os.makedirs(folder_name)
                    write_to_file(folder_name + '/' + str(j) + '.txt', statistics_content)
    else:
        return