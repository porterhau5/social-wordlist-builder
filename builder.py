#!/usr/bin/python
# -*- coding: utf-8 -*-

import ConfigParser
import optparse
import os
import twitter

# class for parsing and returning config values from .tweetrc
class TweetRc(object):
    def __init__(self):
        self._config = None

    def GetConsumerKey(self):
        return self._GetOption('consumer_key')

    def GetConsumerSecret(self):
        return self._GetOption('consumer_secret')

    def GetAccessTokenKey(self):
        return self._GetOption('access_token_key')

    def GetAccessTokenSecret(self):
        return self._GetOption('access_token_secret')

    def _GetOption(self, option):
        try:
            return self._GetConfig().get('Tweet', option)
        except:
            return None

    def _GetConfig(self):
        if not self._config:
            self._config = ConfigParser.ConfigParser()
            self._config.read(os.path.expanduser('~/.tweetrc'))
        return self._config

# authenticate to the Twitter API using appropriate tokens
def authenticate():
    rc = TweetRc()
    consumer_key = rc.GetConsumerKey()
    consumer_secret = rc.GetConsumerSecret()
    access_token_key = rc.GetAccessTokenKey()
    access_token_secret = rc.GetAccessTokenSecret()
    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token_key,
                      access_token_secret=access_token_secret)
    return api

# get the user-supplied arguments
def get_options():
    parser = optparse.OptionParser('usage:\r\n builder.py -u <username> '\
                                   ' [-o <output file>]')

    parser.add_option('-u', dest='username', type='string',\
      help='specify Twitter username')
    parser.add_option('-o', dest='outfile', type='string',\
      help='specify output file name for wordlist')

    (options, args) = parser.parse_args()

    username = options.username
    outfile = options.outfile

    if username == None:
        print parser.usage
        exit(0)

    if outfile == None:
        outfile = "wordlist.txt"

    return username, outfile

# Try to open file_name in mode
# If successful, return the opened file descriptor
def open_file(file_name, mode):
    try:
        the_file = open(file_name, mode)
    except IOError, e:
        print "Unable to open the file", file_name, "Exiting.\n", e
        exit(0)
    else:
        return the_file

# print all possible fields from statuses
def print_statuses(statuses):
    print "CONTRIBUTORS: "
    print [s.contributors for s in statuses]
    print "--------------------------------"
    print "COORDINATES: "
    print [s.coordinates for s in statuses]
    print "--------------------------------"
    print "CREATED_AT: "
    print [s.created_at for s in statuses]
    print "--------------------------------"
    print "CREATED_AT_IN_SECONDS: "
    print [s.created_at_in_seconds for s in statuses]
    print "--------------------------------"
    print "FAVORITED: "
    print [s.favorited for s in statuses]
    print "--------------------------------"
    print "FAVORITE_COUNTS: "
    print [s.favorite_count for s in statuses]
    print "--------------------------------"
    print "GEO: "
    print [s.geo for s in statuses]
    print "--------------------------------"
    print "ID: "
    print [s.id for s in statuses]
    print "--------------------------------"
    print "IN_REPLY_TO_SCREEN_NAME: "
    print [s.in_reply_to_screen_name for s in statuses]
    print "--------------------------------"
    print "IN_REPLY_TO_USER_ID: "
    print [s.in_reply_to_user_id for s in statuses]
    print "--------------------------------"
    print "IN_REPLY_TO_STATUS_ID: "
    print [s.in_reply_to_status_id for s in statuses]
    print "--------------------------------"
    print "LANG: "
    print [s.lang for s in statuses]
    print "--------------------------------"
    print "PLACE: "
    print [s.place for s in statuses]
    print "--------------------------------"
    print "RETWEET_COUNT: "
    print [s.retweet_count for s in statuses]
    print "--------------------------------"
    print "RELATIVE_CREATED_AT: "
    print [s.relative_created_at for s in statuses]
    print "--------------------------------"
    print "SOURCE: "
    print [s.source for s in statuses]
    print "--------------------------------"
    print "TEXT: "
    print [s.text for s in statuses]
    print "--------------------------------"
    print "TRUNCATED: "
    print [s.truncated for s in statuses]
    print "--------------------------------"
    print "LOCATION: "
    print [s.location for s in statuses]
    print "--------------------------------"
    print "USER: "
    print [s.user for s in statuses]
    print "--------------------------------"
    print "URLS: "
    print [s.urls for s in statuses]
    print "--------------------------------"
    print "USER_MENTIONS: "
    print [s.user_mentions for s in statuses]
    print "--------------------------------"
    print "HASHTAGS: "
    print [s.hashtags for s in statuses]
    print "--------------------------------"

# parse the TEXT from each status, extracting each word and removing duplicates
def parse_statuses(statuses):
    wordlist = []

    for s in statuses:
        for word in s.text.split():
            wordlist.append(word.encode('ascii', 'ignore'))

    wordlist = list(set(wordlist))
    wordlist.sort()
    print "[+] Found " + str(len(wordlist)) + " new words"
    return wordlist

# write the wordlist out to a file
def write_wordlist(wordlist, outfile):
    f = open_file(outfile, "a+")
    for element in wordlist:
        f.write("%s\n" % element)
    print "[+] Writing wordlist to: " + outfile
    f.close()

def main():
    username,outfile = get_options()
    api = authenticate()

    print "[+] Fetching statuses for user: " + username
    statuses = api.GetUserTimeline(screen_name=username)

    write_wordlist(parse_statuses(statuses), outfile)

if __name__ == '__main__':
    main()


#TODO:
# add other authentication methods
