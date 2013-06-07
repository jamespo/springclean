springclean
===========

Intro
-----

A log / file cleanup and processing commandline tool.

Written in Python 2. Tested in Python 2.6 on Redhat / Centos 6 and Python 2.7 on Ubuntu 12.10.

It should also work on Python 2.6/2.7 on Windows and MacOS X but is untested.

Usage
-----

springclean.py [options]

Options:

	Match options - can choose a file match and time option

	-f MATCH, --filematch=MATCH
		                  shell-style wildcard to match logfiles to process
    -x MATCHRE, --matchre=MATCHRE
                          regex to match logfiles to process
    -n MTIME_NEWER, --newer=MTIME_NEWER
                          match files newer than x units (d|h|m|s), eg 3d
    -o MTIME_OLDER, --older=MTIME_OLDER
                          match files older than x units (d|h|m|s), eg 3d

	Actions - choose one (defaults to list)

	--rm                  removed matched files
	-l, --list            list matched files (default action)
    -g, --gzip            gzip matched files
    --mv                  move matched files to --destdir
    --destdir=DESTDIR     directory to move files to (with --mv)

	Switches - optional

    -h, --help            show this help message and exit
    --dir=DIR             directory to match from (default $PWD)
    -v, --verbose         verbose output
    -c, --confirm         confirm each individual operation (rm|gzip|mv)
    -s, --syslog          log successful actions to syslog

Examples
--------

List all files that match regex .*\.log$ :

	springclean -x ".*\.log$"
	
Remove all files that match mail.log

	springclean -f mail.log --rm
	
Gzip all files older than 7 days with confirmation

	springclean --gzip --older 7d --confirm
	
Move all files newer than 2 weeks to directory /tmp

	springclean --newer 2w --mv --destdir /tmp

List all files newer than 3 days in /tmp directory

	springclean --dir /tmp --newer 3d --list

Move all files older than 2 hours matching "*.log" to /tmp

	springclean --mv -f "*.log" --older 2h --destdir /tmp

Other
-----

What springclean does not do:
+ recurse into subdirectories (yet)
+ remove directories

