from sys import exit, stderr
from typing import Optional

import typer

from exclock import __VERSION__
from exclock.mains.play_clock_main import main as play_clock_main
from exclock.mains.show_list_main import main as show_list_main
from exclock.mains.specified_time_main import main as specified_time_main
from exclock.util import executable, get_clock_basenames


def main(clock_filename_mock=None, show_list_mock=False, time_mock=None) -> None:
    if not executable('xmessage') and not executable('terminal-notifier'):
        print('both xmessage and terminal-notifier not found.', file=stderr)
        exit(1)

    if not executable('mplayer'):
        print('mplayer not found.', file=stderr)
        exit(1)

    clock_basenames_ = get_clock_basenames()
    clock_basenames = ' [' + '|'.join(get_clock_basenames()) + ']' if clock_basenames_ else ''

    def _main(
        clock_filename_: Optional[str] = typer.Argument(
            None, metavar='CLOCK_FILENAME', help='clock filename' + clock_basenames),
        show_version: bool = typer.Option(False, '-v', '--version', help='show version'),
        clock_filename: Optional[str] = typer.Option(
            None, '-c', '--clock-filename', help='indicate clock filenames' + clock_basenames),
        show_list: bool = typer.Option(
            False, '-l', '--list', help='show clock names in your PC and exit'),
        time_: Optional[str] = typer.Option(
            None, '-t', '--time', help='Time which spends until or to specified'),
        ring_filename: Optional[str] = typer.Option(
            None, '-r', '--ring-filename', help='filename which is used for alarm'),
        traceback: bool = typer.Option(
            False, '--trace', '--traceback', help='show traceback', hidden=True),
    ):
        if clock_filename_mock:
            clock_filename = clock_filename_mock
        if show_list_mock:
            show_list = show_list_mock
        if time_mock:
            time_ = time_mock

        if clock_filename_ is not None and clock_filename is None:
            clock_filename = clock_filename_
        elif clock_filename_ is not None and clock_filename is not None:
            print('clock_filename configuration is duplicate.', file=stderr)
            typer.Exit()

        if show_version:
            print(__VERSION__)
        elif show_list:
            show_list_main()
        elif time_ is not None:
            specified_time_main(time_, ring_filename)
        elif clock_filename is not None:
            play_clock_main(clock_filename)
        else:
            print('clock_filename is not declared.', file=stderr)
            typer.Exit()

    app = typer.Typer(add_completion=False)
    app.command()(_main)
    app()


if __name__ == '__main__':
    main()
