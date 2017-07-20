from argparse import ArgumentParser, RawDescriptionHelpFormatter
from logging import getLogger, StreamHandler, Formatter, DEBUG, INFO

import sys
import time

__version__ = '0.0.1'


def prepare_parser():
    parser = ArgumentParser(description=(__doc__),
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('-d', '--debug', action='store_true',
                        help='Show debug log')
    # parser.add_argument('-v', '--version', action='version',
    #                     version=__version__,
    #                     help='Show version and exit')
    return parser


def main():
    parser = prepare_parser()
    args = parser.parse_args()

    logger = getLogger(__name__)
    handler = StreamHandler()
    logger.addHandler(handler)
    if args.debug:
        logger.setLevel(DEBUG)
        handler.setLevel(DEBUG)
    else:
        logger.setLevel(INFO)
        handler.setLevel(INFO)
    handler.setFormatter(Formatter('%(asctime)s %(levelname)7s %(message)s'))
    logger.info('Start Running (version: {})'.format(__version__))
    logger.debug('Sleeping 1 sec')
    time.sleep(1)
    logger.info('Finished Running')
    return 0


if __name__ == '__main__':
    sys.exit(main())
