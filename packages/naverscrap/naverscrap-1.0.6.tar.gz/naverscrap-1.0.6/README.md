## Introduction
Naver News scraping library


## Installation 
```
pip install naverscrap
```

## Usage

### Single Query
```
from naverscrap import NaverScrap

ns = NaverScrap
df = ns.obtain_results("Tesla", "2020.03.04", "2020.04.04", 10, False) 
                        #query(s), start_date, end_date, no. of results for each query, ascending (false by default)
```

### Multiple Queries
```
from naverscrap import NaverScrap

ns = NaverScrap
queries = ["Tesla", "Facebook", "카카오"] # list of query
df = ns.obtain_results(queries, "2020.03.04", "2020.04.04", 10, False) 
                        #query(s), start_date, end_date, no. of results for each query, ascending (false by default)
```

The output dataframe will be in:

Column | Description
------------ | -------------
_Item_ | Search Query
_Date_ | Date of News Article
_Newspaper_ | News Publication Company
_Title of news_ | Title of news article
_Link_ | Link to news article
_Summary_ | Summary of the news article


## License
© 2021 Brendon Lim.

This repository is licensed under the MIT license.

See LICENSE for details.

[![Downloads](https://static.pepy.tech/personalized-badge/naverscrap?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Total%20Downloads)](https://pepy.tech/project/naverscrap)
