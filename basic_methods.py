BASE_URL = 'https://search.techcrunch.com/search?p={keyword}&b={output}'

    
DEFAULT_NUMBER_OF_PAGES = 5
DEFAULT_KEYWORD_INPUT = 'games'

NUMBER_OF_PAGES = int(input('Enter a number for pages:---> ') or DEFAULT_NUMBER_OF_PAGES)
TOTAL_SEARCH_ITEMS = NUMBER_OF_PAGES * 10
KEYWORD_INPUT = input('Enter your keyword for search:---> ') or DEFAULT_KEYWORD_INPUT

