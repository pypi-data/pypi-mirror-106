from optparse import OptionParser
from sys import exit, stderr
from typing import Optional

import typer

from exclock import __VERSION__
from exclock.mains.play_clock_main import main as play_clock_main
from exclock.mains.show_list_main import main as show_list_main
from exclock.mains.specified_time_main import main as specified_time_main
from exclock.util import executable


def get_option_parser():
    usage = 'exclock [options] {clock-filename}'
    parser = OptionParser(usage=usage, version=__VERSION__)
    parser.add_option(
        '-l',
        '--list',
        action='store_true',
        default=False,
        dest='show_list',
        help='show clock names in your PC and exit',
    )
    parser.add_option(
        '-t',
        '--time',
        dest='time',
        action='store',
        help='Time which spends until or to specified',
    )
    parser.add_option(
        '-r',
        '--ring-filename',
        dest='ring_filename',
        action='store',
        help='filename which is used for alarm',
    )
    parser.add_option(
        '--trace',
        '--traceback',
        default=False,
        action='store_true',
        dest='with_traceback',
        help='show traceback',
    )

    return parser


def main(clock_filename_mock=None, show_list_mock=False, time_mock=None) -> None:
    if not executable('xmessage') and not executable('terminal-notifier'):
        print('both xmessage and terminal-notifier not found.', file=stderr)
        exit(1)

    if not executable('mplayer'):
        print('mplayer not found.', file=stderr)
        exit(1)

    def _main(
            show_version: bool = typer.Option(False, '-v', '--version', help='show version'),
            clock_filename: Optional[str] = typer.Option(None, '-c', '--clock-name', help=''),
            show_list: bool = typer.Option(
                False, '-l', '--list', help='show clock names in your PC and exit'),
            time_: Optional[str] = typer.Option(
                None, '-t', '--time', help='Time which spends until or to specified'),
            ring_filename: Optional[str] = typer.Option(
                None, '-r', '--ring-filename', help='filename which is used for alarm'),
            traceback: bool = typer.Option(False, '--trace', '--traceback', help='show traceback'),
    ):
        if clock_filename_mock:
            clock_filename = clock_filename_mock
        if show_list_mock:
            show_list = show_list_mock
        if time_mock:
            time_ = time_mock

        if show_version:
            print(__VERSION__)
        elif show_list:
            show_list_main()
        elif time_ is not None:
            specified_time_main(time_, ring_filename)
        else:
            play_clock_main(clock_filename)

    typer.run(_main)


if __name__ == '__main__':
    main()
