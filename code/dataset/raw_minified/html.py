from markupsafe import Markup as A
def B(url):return A('<div data-html-include="{}"></div>'.format(url))