#!/usr/bin/python3


from argparse import ArgumentParser
from utils.downloader import Downloader
from domainparsers.reddit import Reddit


__author__ = 'petarGitNik'
__copyright__ = 'Copyright (c) 2017 petarGitNik petargitnik@gmail.com'
__version__ = 'v0.1.0'
__license__ = 'MIT'
__email__ = 'petargitnik@gmail.com'
__status__ = 'Development'


def parse_arguments():
    """
    Parse input arguments of the program. Two positional arguments are
    mandatory: 'URL' and destination 'directory'. 'verbose' is optional.
    Example:

    crawlddit.py -v https://www.reddit.com/r/MemeEconomy/ ./memes

    For more information type:

    crawlddit.py --help
    """
    parser = ArgumentParser(description='reddit /r downloader')

    parser.add_argument('-v', '--verbose',
                        help='display download progress and information',
                        action='store_true')
    parser.add_argument('-p', help='crawl P number of pages', type=int)
    parser.add_argument('URL', help='source link')
    parser.add_argument('directory', help='destination directory')

    args = parser.parse_args()

    return (args.verbose, args.p, args.URL, args.directory)


if __name__ == '__main__':
    verbose, pages, url, destination = parse_arguments()

    if verbose: print('Fetching available links...')
    reddit = Reddit(url, pages)
    reddit.get_all_posts()
    images = reddit.images

    if verbose: print(
        '{}/{} images available for download.'.format(
            reddit.count_downloadable_images() , len(images)
        )
    )

    downloader = Downloader(reddit, destination, verbose)
    downloader.download_files()
