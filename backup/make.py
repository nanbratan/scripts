#!/usr/bin/env python3

import os
import shutil
import subprocess
from datetime import datetime

pwd = os.path.dirname(os.path.realpath(__file__))

root_path = '/'
backup_path = '/backup'
options = '-aAXv'
as_root = 'pkexec'
rsync_cmd = 'rsync'
exclude_dirs = f'--exclude-from={pwd}/exclude_dirs.txt'


def get_snap_path():
    current_day = datetime.now().day
    current_month = datetime.now().month
    current_year = datetime.now().year

    current_date = f'{current_day}-{current_month}-{current_year}'

    return f'{backup_path}/{current_date}'


def create_snap_dir():
    snap_path = get_snap_path

    if os.path.exists(snap_path):
        shutil.rmtree(snap_path)

    os.mkdir(snap_path)


def make_backup():
    snap_path = get_snap_path()

    create_snap_dir()

    subprocess.run([
        as_root,
        rsync_cmd,
        options,
        exclude_dirs,
        root_path,
        snap_path,
    ])


make_backup()
