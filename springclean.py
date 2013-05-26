#!/usr/bin/env python

# springclean - process and cleanup (log) files
# Copyright James Powell jamespo [at] gmail [dot] com - 2013

import sys, re, os
import fnmatch
import time
from operator import lt, gt
from optparse import OptionParser

class SpringClean(object):
    def __init__(self, options):
        self.options = options
        self.status = None

    def run(self):
        if self.find_matches():
            self.perform_action()

    def find_matches(self):
        '''find filename matches based on conditions passed'''
        try:
            os.chdir(self.options.dir)
        except OSError, excep:
            self.status = excep[1] + ' ' + self.options.dir
            return False
        # get all files, then filter
        files = [file for file in os.listdir(".")]
        if self.options.matchre is not None:
            files = self.matchre_files(files)
        if self.options.mtime_older is not None:
            files = self.match_mtime_files(files, lt, self.calc_time(self.options.mtime_older))
        elif self.options.mtime_newer is not None:
            files = self.match_mtime_files(files, gt, self.calc_time(self.options.mtime_newer))
        self.files = files
        return True

    def matchre_files(self, files):
        '''match files against regex'''
        mre = re.compile(self.options.matchre)
        refiles = [file for file in files if re.search(mre, file) is not None]
        return refiles

    def match_mtime_files(self, files, oper, threshold):
        '''match files mtime against now - delta'''
        # oper is either lt or gt
        mt_files = [file for file in files if oper(os.stat(file).st_mtime, threshold)]
        return mt_files

    @staticmethod
    def calc_time(timediff, unit = 'days'):
        secs_to_unit = { 'days' : 86400 }
        time_threshold = int(time.mktime(time.localtime())) - int(timediff * secs_to_unit['days'])
        return time_threshold

    def perform_action(self):
        action = None
        if self.options.action == 'list':
            print '%s matched files: ' % len(self.files)
            self.process_files(self.list_file)
        elif self.options.action == 'rm':
            self.process_files(self.remove_file)
            print "Removed %s files" % len(self.files)

    def process_files(self, action):
        for file in self.files:
            action(file)


    def list_file(self, file):
        print self.options.dir + '/' + file

    def remove_file(self, file):
        os.remove(self.options.dir + '/' + file)


def bombout(reason):
    '''quit with error message'''
    print "Error: " + reason
    sys.exit(0)

def checkopts(options):
    '''validate passed options'''
    if options.match is None and options.matchre is None and options.mtime_older is None\
        and options.mtime_newer is None:
        bombout("No file matching arguments specified")
    elif options.match is not None and options.matchre is not None:
        bombout("Choose one of match and matchre arguments")
    elif options.mtime_older is not None and options.mtime_newer is not None:
        bombout("Choose one of older or newer conditions")

def main():
    parser = OptionParser()
    parser.add_option("--dir", dest="dir", help="directory to match from (default $PWD)",
                      default=os.getcwd())
    parser.add_option("--match", dest="match",
                      help="shell-style wildcard to match logfiles to process")
    parser.add_option("--matchre", dest="matchre",
                      help="regex to match logfiles to process")
    parser.add_option("--newer", dest="mtime_newer",
                      help="match files newer than x days")
    parser.add_option("--older", dest="mtime_older",
                      help="match files older than x days")
    parser.add_option("--action", dest="action", default="list",
                      help="action on matched files (rm|list|gzip|mv) default - list")
    (options, args) = parser.parse_args()
    checkopts(options)
    sc = SpringClean(options)
    rc = sc.run()
    #print sc.status

if __name__ == '__main__':
    main()
