from distutils.core import setup
setup(
  name = 'naverscrap',
  packages = ['naverscrap'],
  version = '1.0.1',      
  license='MIT',    
  description = 'A Naver News Scraping tool',
  author = 'Brendon Lim',  
  author_email = 'brendonlim96@hotmail.com',   
  url = 'https://github.com/brendonlch/naverscrap',   
  download_url = 'https://github.com/brendonlch/naverscrap/archive/refs/tags/1.0.0.tar.gz',
  
  keywords = ['naver', 'korea', 'news', 'article', 'newspaper', 'web scrapping'],
  install_requires=[
          'datetime',
          'beautifulsoup4',
          'pandas',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',   
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)