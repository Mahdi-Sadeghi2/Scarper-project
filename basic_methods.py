

BASE_URL = 'https://search.techcrunch.com/search?p={keyword}&b={output}'
BASE_CATEGORY_URL = 'https://techcrunch.com/category/{categories}/'


DEFAULT_NUMBER_OF_PAGES = 5
DEFAULT_KEYWORD_INPUT = 'games'



task = int(input('Please choose one task:\n1.scarp based on search\n2.scrap based on category---> '))
if task == 1:
    NUMBER_OF_PAGES = int(input('Enter a number for pages:---> ') or DEFAULT_NUMBER_OF_PAGES)
    TOTAL_SEARCH_ITEMS = NUMBER_OF_PAGES * 10
    KEYWORD_INPUT = input('Enter your keyword for search:---> ') or DEFAULT_KEYWORD_INPUT
elif task == 2:
    CATEGORY_CHOOSE = int(input('Enter a number:\n1.startups\n2.venture\n3.security\n4.artificial-intelligence\n5.cryptocurrency\n6.apps\n7.space\n8.social\n9.biotech-health\n10.enterprise\n11.hardware\n12.transportation\n13.fintech\n14.robotics\n15.commerce\n16.climate\n17.transportation\n18.government-policy:---> '))
    CATEGORIES = CATEGORY_CHOOSE

    if CATEGORY_CHOOSE == 1:
        CATEGORIES = 'Startups'
    elif CATEGORY_CHOOSE == 2:
        CATEGORIES = 'Venture'
    elif CATEGORY_CHOOSE == 3:
        CATEGORIES = 'Security'
    elif CATEGORY_CHOOSE == 4:
        CATEGORIES = 'artificial-intelligence'
    elif CATEGORY_CHOOSE == 5:
        CATEGORIES = 'cryptocurrency'
    elif CATEGORY_CHOOSE == 6:
        CATEGORIES = 'Apps'   
    elif CATEGORY_CHOOSE == 7:
        CATEGORIES = 'Space'   
    elif CATEGORY_CHOOSE == 8:
        CATEGORIES = 'Social'   
    elif CATEGORY_CHOOSE == 9:
        CATEGORIES = 'Biotech-health'
    elif CATEGORY_CHOOSE == 10:
        CATEGORIES = 'Enterprise'
    elif CATEGORY_CHOOSE == 11:
        CATEGORIES = 'Hardware'
    elif CATEGORY_CHOOSE == 12:
        CATEGORIES = 'Transportation'
    elif CATEGORY_CHOOSE == 13:
        CATEGORIES = 'Fintech'
    elif CATEGORY_CHOOSE == 14:
        CATEGORIES = 'Robotics'
    elif CATEGORY_CHOOSE == 15:
        CATEGORIES = 'Commerce'
    elif CATEGORY_CHOOSE == 16:
        CATEGORIES = 'Climate'
    elif CATEGORY_CHOOSE == 17:
        CATEGORIES = 'Transportation'
    elif CATEGORY_CHOOSE == 18:
        CATEGORIES = 'Government-policy'
    else:
        print('Wrong input')
else:
    print('Sorry, wrong input, try again')