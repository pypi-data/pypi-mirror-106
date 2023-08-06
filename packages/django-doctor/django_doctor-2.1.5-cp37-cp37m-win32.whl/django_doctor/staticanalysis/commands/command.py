import argparse
import pathlib
import sys

from django_doctor.staticanalysis.commands import fix, check, helpers


ignore_help = 'Add <file or directory> to the black list. It should be a base name, not a path.'

SUPPORT_MESSAGE = 'Please support Django Doctor by buying a licence for commercial use. https://django.doctor/price\n\n'


def resolve_directory(raw):
    return str(pathlib.Path(raw).resolve())


parser = argparse.ArgumentParser(prog='Django Doctor')

subparsers = parser.add_subparsers()

check_parser = subparsers.add_parser('check')
check_parser.add_argument('-d', '--directory', default='.', type=resolve_directory)
check_parser.add_argument('-i', '--ignore', nargs='*', help=ignore_help)

check_parser.set_defaults(command='check')

fix_parser = subparsers.add_parser('fix')
fix_parser.add_argument('-d', '--directory', default='.', type=resolve_directory)
fix_parser.add_argument('-i', '--ignore', nargs='*', help=ignore_help)
fix_parser.add_argument('-a', '--address', default='localhost', type=str)
fix_parser.add_argument('-p', '--port', default=9000, type=int)
fix_parser.set_defaults(command='fix')


def handle(output=sys.stdout, argv=sys.argv[1:]):
    output.write(helpers.blue(SUPPORT_MESSAGE))

    options = parser.parse_args(argv)

    if options.command == 'check':
        check.handle(
            project_root=options.directory,
            ignore=options.ignore or [],
            output=output
        )
    elif options.command == 'fix':
        fix.handle(
            project_root=options.directory,
            output=output,
            address=options.address,
            port=options.port,
            ignore=options.ignore or [], 
        )


def main():
    try:
        handle()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
