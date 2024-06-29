# -*- coding: utf-8 -*-
"""."""

import pathlib
import subprocess

BASE_DIR = pathlib.Path(__file__).resolve().parent

INPUT = BASE_DIR.parent / 'resources' / 'ui'
OUTPUT = BASE_DIR.parent / 'app_pyside_ui' / 'uic'


def main() -> None:
    print('[!] Converting *.ui files, please wait... [!]')
    print('Converted Files:')
    for file in INPUT.rglob('*.ui'):
        if file.is_file() and file.suffix == '.ui':
            print(f'- {file.name}.')
            output = OUTPUT / f'Ui_{file.stem}.py'
            output.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run(
                args=['pyside6-uic', '--from-imports', file, '-o', output],
                check=False,
            )
    print('[!] Done [!]')


if __name__ == '__main__':
    main()
