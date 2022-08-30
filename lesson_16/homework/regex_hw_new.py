import re


def remove_url_anchor(url):
    """ Returns a URL with any after removing the connection (#)."""
    new_url = re.split(r'#', url, 1)
    return new_url[0]


assert remove_url_anchor("lms.ithillel.ua#about") == "lms.ithillel.ua"
assert remove_url_anchor("lms.ithillel.ua/groups/?page=1#example") == "lms.ithillel.ua/groups/?page=1"
assert remove_url_anchor("lms.ithillel.ua/groups/") == "lms.ithillel.ua/groups/"
