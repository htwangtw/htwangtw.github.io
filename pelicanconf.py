AUTHOR = 'Hao-Ting Wang'
SITENAME = 'Hao-Ting Wang'
SITETITLE = 'Hao-Ting Wang'
SITESUBTITLE = 'Neuroscience, Neuroinformatics'
SITEDESCRIPTION = "Hao-Ting's personal site."

SITEURL = 'https://wanghaoting.com'
SITELOGO = SITEURL + "/images/profile.png"

THEME = "./themes/Flex"

PATH = 'content'
PAGE_PATHS = ['']
ARTICLE_PATHS = ['articles']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

# Blogroll
# LINKS = (
#     ("Archives", "/archives.html"),
#     ("Categories", "/categories.html"),
#     ("Tags", "/tags.html"),
# )

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/HaoTingW713'),
          ('github', 'https://github.com/htwangtw'),
          ('google', 'https://scholar.google.com/citations?user=FrlzI8IAAAAJ&hl=en'))

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
    "icon": True,
    "language": "en_US",
}

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = True
