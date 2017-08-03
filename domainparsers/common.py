#!/usr/bin/python3


"""
Constants shared between parsers. These constants could be turned into classes.
For example:

class Domain(object):
    REDDIT = 'reddit'
    GFYCAT = 'gfycat'
    ...

So later in the program they could be used as Domain.REDDIT.
"""


FILE_FORMATS = ['.jpg', '.jpeg', '.png', '.gif', '.webm']
DOMAINS = ['reddit', 'imgur', 'gfycat', 'tumblr', 'blogspot']


class DomainMissingException(Exception):
    pass


if __name__ == '__main__':
    print(__doc__)
