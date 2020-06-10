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


class BackupHadler:
    @staticmethod
    def get_current_date():
        current_day = datetime.now().day
        current_month = datetime.now().month
        current_year = datetime.now().year

        return f'{current_day}-{current_month}-{current_year}'

    def create_snap_dir(self):
        current_date = BackupHadler.get_current_date()
        snap_path = f'{backup_path}/{current_date}'

        if os.path.exists(snap_path):
            shutil.rmtree(snap_path)

        os.mkdir(snap_path)

    def make(self):
        current_date = BackupHadler.get_current_date()
        snap_path = f'{backup_path}/{current_date}'

        self.create_snap_dir()

        subprocess.run([
            as_root,
            rsync_cmd,
            options,
            f"--exclude-from={pwd}/exclude_dirs.txt",
            root_path,
            snap_path,
        ])


backup_handler = BackupHadler()

backup_handler.make()
