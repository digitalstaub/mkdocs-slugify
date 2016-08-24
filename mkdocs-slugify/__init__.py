import re
import unicodedata

def slugify(value, separator):

    """ Slugify a string, to make it URL friendly. """
    normalized = unicodedata.normalize('NFKD', value)
    v = normalized.strip().lower()
    # remove toc numbers
    v = re.sub('^[\d\.]+\s?\-?\s?', '', v)
    # print re.sub('[%s\s]+' % separator, separator, v)

    return re.sub('[%s\s]+' % separator, separator, v)
