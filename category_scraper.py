from basic_methods import DEFAULT_KEYWORD_INPUT, DEFAULT_NUMBER_OF_PAGES


def user_category_choose(category=None):
    CATEGORY_CHOOSE = int(input('Enter a number:\n1.startups\n2.venture\n3.security\n4.artificial-intelligence\n5.cryptocurrency\n6.apps\n7.space\n8.social\n9.biotech-health\n10.enterprise\n11.hardware\n12.transportation\n13.fintech\n14.robotics\n15.commerce\n16.climate\n17.transportation\n18.government-policy:---> '))
    category = CATEGORY_CHOOSE
    if CATEGORY_CHOOSE == 1:
        category = 'Startups'
    elif CATEGORY_CHOOSE == 2:
        category = 'Venture'
    elif CATEGORY_CHOOSE == 3:
        category = 'Security'
    elif CATEGORY_CHOOSE == 4:
        category = 'artificial-intelligence'
    elif CATEGORY_CHOOSE == 5:
        category = 'cryptocurrency'
    elif CATEGORY_CHOOSE == 6:
        category = 'Apps'
    elif CATEGORY_CHOOSE == 7:
        category = 'Space'
    elif CATEGORY_CHOOSE == 8:
        category = 'Social'
    elif CATEGORY_CHOOSE == 9:
        category = 'Biotech-health'
    elif CATEGORY_CHOOSE == 10:
        category = 'Enterprise'
    elif CATEGORY_CHOOSE == 11:
        category = 'Hardware'
    elif CATEGORY_CHOOSE == 12:
        category = 'Transportation'
    elif CATEGORY_CHOOSE == 13:
        category = 'Fintech'
    elif CATEGORY_CHOOSE == 14:
        category = 'Robotics'
    elif CATEGORY_CHOOSE == 15:
        category = 'Commerce'
    elif CATEGORY_CHOOSE == 16:
        category = 'Climate'
    elif CATEGORY_CHOOSE == 17:
        category = 'Transportation'
    elif CATEGORY_CHOOSE == 18:
        category = 'Government-policy'
    else:
        print('Wrong input')
    return category


page = list()


def user_pages_input(pages=None):
    pages = int(input('Enter a number for pages:---> ')
                or DEFAULT_NUMBER_OF_PAGES)
    page.append(pages)


def user_page_number_input(search_page=None):
    pages = int(''.join(map(str, page)))
    search_page = pages * 10
    return search_page


def user_keyword_input(keyword=None):
    keyword = input(
        'Enter your keyword for search:---> ') or DEFAULT_KEYWORD_INPUT
    return (keyword)
