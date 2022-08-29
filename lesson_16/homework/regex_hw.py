import re


def remove_url_anchor(url):
    """ Returns a URL with any after removing the connection (#)."""
    if re.search(r'#', url):
        new_url = re.split(r'#', url, 1)
        print(new_url[0])
        return new_url[0]
    else:
        print(url)
        return url


assert remove_url_anchor("lms.ithillel.ua#about") == "lms.ithillel.ua"
assert remove_url_anchor("lms.ithillel.ua/groups/?page=1#example") == "lms.ithillel.ua/groups/?page=1"
assert remove_url_anchor("lms.ithillel.ua/groups/") == "lms.ithillel.ua/groups/"
