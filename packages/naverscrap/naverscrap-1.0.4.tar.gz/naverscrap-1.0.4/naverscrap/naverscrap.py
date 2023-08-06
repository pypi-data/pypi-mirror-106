import requests
from bs4 import BeautifulSoup
from datetime import datetime  
from datetime import timedelta
import pandas as pd

class NaverScrap:
    def obtain_results(queries, date_start, date_end, num_of_queries, ascending=False):
        if isinstance(queries, str):
            queries = [queries]
        arr = []
        for query in queries:
            i = 1
            tmp = []
            while i < num_of_queries:
                r = requests.get(f'https://search.naver.com/search.naver?where=news&query={query}&ds={date_start}&de={date_end}&sort={int(ascending)+1}&start={i}&nso=so%3Ar%2Cp%3Afrom{date_start.replace(".","")}to{date_end.replace(".", "")}')
                scrap = BeautifulSoup(r.text, 'lxml')
                results = scrap.find_all('li', class_='bx')
                for result in results:
                    article = result.find('a', class_='news_tit')
                    desc = result.find('div', class_='dsc_wrap')
                    news_source = result.find('a', class_='info press')
                    if article == None:
                        continue
                    date = result.find_all('span', class_='info')[-1]
                    date = date.text
                    if '일 전' in date:
                        day = int(date[0])
                        date = str(datetime.now() - timedelta(days=day))
                        date = date.replace('-','.')
                    elif '시간 전' in date:
                        hour = int(date[:len(date)-4])
                        date = str(datetime.now() - timedelta(hours=hour))
                        date = date.replace('-', '.')
                    elif '분 전' in date:
                        minute = int(date[:len(date)-4])
                        date = str(datetime.now() - timedelta(minutes=minute))
                        date = date.replace('-', '.')

                    date = date[:10]
                    title = article['title']
                    link = article['href']
                    desc = desc.text
                    news_source = news_source.text
                    tmp.append([query, date, news_source, title, link, desc])
                i += 10
            arr += tmp[:num_of_queries]
        df = pd.DataFrame(arr, columns=['Item', 'Date', 'Newspaper', 'Title of news', 'Link', 'Summary'])
        return df