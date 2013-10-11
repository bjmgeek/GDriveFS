#!/usr/bin/env python2.7

from os import unlink, environ
from os.path import join

def main():
    sbin_parent = environ.get('PREFIX', '/usr/local')
    sbin_path = join(sbin_parent, 'sbin')

    for tool_name in ('gdfs', 'gdfstool'):
        file_path = join(sbin_path, tool_name)

        print("Unlinking: %s" % (file_path))
        unlink(file_path)

main()

