# -*- coding: utf-8 -*-
import os

from django.conf import settings


def regex_string_to_png(regex_string):
    filename = os.path.join(settings.GRAPHS_PATH, 'output.png')

    os.system('python -m automaton -o {} "{}"'.format(filename, regex_string))
