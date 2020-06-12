#!/usr/bin/env python3

import sys
import os

from datetime import datetime

HOME = os.environ['HOME']
notes_dir = f'{HOME}/notes'


def get_current_date():
    current_day = datetime.now().day
    current_month = datetime.now().month
    current_year = datetime.now().year

    if len(str(current_day)) == 1:
        current_day = f'0{current_day}'
    if len(str(current_month)) == 1:
        current_month = f'0{current_month}'

    return f'{current_day}-{current_month}-{current_year}'


def get_current_time():
    current_hour = datetime.now().hour
    current_minutes = datetime.now().minute

    if len(str(current_minutes)) == 1:
        current_minutes = f'0{current_minutes}'

    return f'{current_hour}:{current_minutes}'


def make_note():
    text_exists = len(sys.argv) > 1

    if not text_exists:
        print("Attention! Write text for note!")
        return

    text = sys.argv[1]
    current_date = get_current_date()
    current_time = get_current_time()

    if not os.path.exists(notes_dir):
        os.mkdir(notes_dir)

    file = open(f'{notes_dir}/{current_date}', 'a+')

    file.write(f'[{current_time}] - {text}\n')


make_note()

