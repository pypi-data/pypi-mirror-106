#!/usr/bin/python3
# -*- coding: utf-8 -*-

#  pypgexec. Script to execute queries in postgres database
#  Copyright (C) 2021  Alexis Torres Valdes
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#  USA
#
#  Contact: alexis89.dev@gmail.com

import os
import argparse
import logging
import psycopg2
from configparser import ConfigParser

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(BASE_DIR, '__version__.py')) as f:
    exec(f.read(), about)

logging.basicConfig(filename='pypgexec.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def parse_args():
    __version__ = about['__version__']

    parser = argparse.ArgumentParser(prog=about['__title__'], description=about['__description__'])

    parser.add_argument('-v',
                        '--version',
                        action='version',
                        version=f'%(prog)s {__version__}',)
    parser.add_argument('-a',
                        '--author',
                        action='version',
                        version='%(prog)s was created by software developer Alexis Torres Valdes <alexis89.dev@gmail.com>',
                        help="show program's author and exit")

    parser.add_argument('--config',
                        required=True,
                        help='Database configuration file')
    parser.add_argument('--script',
                        required=True,
                        help='Script to execute')

    return parser.parse_args()


def config(filename, section):
    if not os.path.exists(filename):
        raise ValueError('File does not exist')

    parser = ConfigParser()
    parser.read(filename)

    if not parser.has_section(section):
        raise Exception(f'Section {section} not found in file {filename}')

    cfg = {}
    params = parser.items(section)
    for param in params:
        cfg[param[0]] = param[1]

    return cfg


def pg_exec(params: dict, queries: tuple):
    conn = None
    try:
        conn = psycopg2.connect(**params)
        logger.info('Connection created')

        with conn:
            with conn.cursor() as cur:
                for query in queries:
                    try:
                        cur.execute(query)
                        logger.info(f'{query} OK')
                    except (Exception, psycopg2.DatabaseError) as err:
                        logger.error(f'{query} - {err}')
                        continue
    except (Exception, psycopg2.DatabaseError) as err:
        logger.error(err)
    finally:
        if conn is not None:
            conn.close()
            logger.info('Connection closed')


def main():
    args = parse_args()
    config_arg = args.config
    script_arg = args.script

    params = config(config_arg, 'postgresql')
    with open(script_arg) as fr:
        uncomment = filter(lambda ln: not ln.startswith('#'), fr.readlines())
        no_line_breaks = map(lambda ln: ln.replace('\n', ''), uncomment)
        queries = tuple(no_line_breaks)

    pg_exec(params, queries)


if __name__ == '__main__':
    main()
