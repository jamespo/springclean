springclean
===========

a log / file cleanup and processing commandline tool

Usage:
------

springclean.py [options]

Options:

    	-h, --help           show this help message and exit
    	--dir=DIR            directory to match from (default $PWD)
    	--match=MATCH        shell-style wildcard to match logfiles to process
    	--matchre=MATCHRE    regex to match logfiles to process
    	--newer=MTIME_NEWER  match files newer than x days
    	--older=MTIME_OLDER  match files older than x days
    	--action=ACTION      action on matched files (rm|list|gzip|mv) default -
    						 list
