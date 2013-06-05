springclean
===========

a log / file cleanup and processing commandline tool

Usage:
------

springclean.py [options]

Options:

      -h, --help            show this help message and exit
      --dir=DIR             directory to match from (default $PWD)
      -v, --verbose         verbose output
      -c, --confirm         confirm each individual operatio (rm|gzip|mv)
      -s, --syslog          log actions to syslog
      -f MATCH, --filematch=MATCH
                            shell-style wildcard to match logfiles to process
      -x MATCHRE, --matchre=MATCHRE
                            regex to match logfiles to process
      -n MTIME_NEWER, --newer=MTIME_NEWER
                            match files newer than x units (d|h|m|s), eg 3d
      -o MTIME_OLDER, --older=MTIME_OLDER
                            match files older than x units (d|h|m|s), eg 3d
      --rm                  removed matched files
      -l, --list            list matched files
      -g, --gzip            gzip matched files
      --mv                  move matched files to --destdir
      --destdir=DESTDIR     directory to move files to (with --action mv)
    						 list
