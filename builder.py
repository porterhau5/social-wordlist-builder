#!/usr/bin/python
# -*- coding: utf-8 -*-

import ConfigParser
import optparse
import os
import string
import twitter

wordlist = []

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
                                   ' [-c <status count> -o <output file>]')

    parser.add_option('-c', dest='count', type='int',\
      help='specify number of statuses to pull (max 200)')
    parser.add_option('-o', dest='outfile', type='string',\
      help='specify output file name for wordlist')
    parser.add_option('-u', dest='username', type='string',\
      help='specify Twitter username')

    (options, args) = parser.parse_args()

    count = options.count
    outfile = options.outfile
    username = options.username

    if count > 200:
        print "Count must be less than or equal to 200"
        print parser.usage
        exit(0)

    # default to 20
    if count == None:
        count = 20

    # default to username.txt
    if outfile == None:
        outfile = str(username) + ".txt"

    if username == None:
        print parser.usage
        exit(0)

    return count, outfile, username


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


# print all possible fields for twitter.Status object
# mostly for reference
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


# print all possible fields for twitter.User object
# mostly for reference
def print_user(user):
    print "ID: "
    print user.id
    print "--------------------------------"
    print "NAME: "
    print user.name
    print "--------------------------------"
    print "SCREEN_NAME: "
    print user.screen_name
    print "--------------------------------"
    print "LOCATION: "
    print user.location
    print "--------------------------------"
    print "DESCRIPTION: "
    print user.description
    print "--------------------------------"
    print "PROFILE_IMAGE_URL: "
    print user.profile_image_url
    print "--------------------------------"
    print "PROFILE_BACKGROUND_TILE: "
    print user.profile_background_tile
    print "--------------------------------"
    print "PROFILE_BACKGROUND_IMAGE_URL: "
    print user.profile_background_image_url
    print "--------------------------------"
    print "PROFILE_SIDEBAR_FILL_COLOR: "
    print user.profile_sidebar_fill_color
    print "--------------------------------"
    print "PROFILE_BACKGROUND_COLOR: "
    print user.profile_background_color
    print "--------------------------------"
    print "PROFILE_LINK_COLOR: "
    print user.profile_link_color
    print "--------------------------------"
    print "PROFILE_TEXT_COLOR: "
    print user.profile_text_color
    print "--------------------------------"
    print "PROTECTED: "
    print user.protected
    print "--------------------------------"
    print "UTC_OFFSET: "
    print user.utc_offset
    print "--------------------------------"
    print "TIME_ZONE: "
    print user.time_zone
    print "--------------------------------"
    print "URL: "
    print user.url
    print "--------------------------------"
    print "STATUS: "
    print user.status
    print "--------------------------------"
    print "STATUSES_COUNT: "
    print user.statuses_count
    print "--------------------------------"
    print "FOLLOWERS_COUNT: "
    print user.followers_count
    print "--------------------------------"
    print "FRIENDS_COUNT: "
    print user.friends_count
    print "--------------------------------"
    print "FAVOURITES_COUNT: "
    print user.favourites_count
    print "--------------------------------"
    print "GEO_ENABLED: "
    print user.geo_enabled
    print "--------------------------------"
    print "VERIFIED: "
    print user.verified
    print "--------------------------------"
    print "LANG: "
    print user.lang
    print "--------------------------------"
    print "NOTIFICATIONS: "
    print user.notifications
    print "--------------------------------"
    print "CONTRIBUTORS_ENABLED: "
    print user.contributors_enabled
    print "--------------------------------"
    print "CREATED_AT: "
    print user.created_at
    print "--------------------------------"
    print "LISTED_COUNT: "
    print user.listed_count
    print "--------------------------------"


# parse the TEXT from each status, extracting each word
def parse_statuses(statuses):

    print "[*] Fetching user statuses..."

    status_count = 0
    for s in statuses:
        status_count += 1
        for word in s.text.split():
            word = word.encode('ascii', 'ignore')
            wordlist.append(word)
            # remove punctuation from word
            word = word.translate(string.maketrans("",""), string.punctuation)
            wordlist.append(word)

    print "        Found " + str(status_count) + " statuses"

def parse_user(user):

    print "[*] Fetching user information..."

    print "        Fetching user description"
    # get words from User's description
    for word in user.description.split():
        word = word.encode('ascii', 'ignore')
        wordlist.append(word)
        # remove punctuation from word
        word = word.translate(string.maketrans("",""), string.punctuation)
        wordlist.append(word)

    print "        Fetching user name"
    # get words from User's name
    for word in user.name.split():
        word = word.encode('ascii', 'ignore')
        wordlist.append(word)
        # remove punctuation from word
        word = word.translate(string.maketrans("",""), string.punctuation)
        wordlist.append(word)

    print "        Fetching user screenname"
    # get words from User's screen_name
    for word in user.screen_name.split():
        word = word.encode('ascii', 'ignore')
        wordlist.append(word)
        # remove punctuation from word
        word = word.translate(string.maketrans("",""), string.punctuation)
        wordlist.append(word)

    print "        Fetching user location"
    # get words from User's location
    for word in user.location.split():
        word = word.encode('ascii', 'ignore')
        wordlist.append(word)
        # remove punctuation from word
        word = word.translate(string.maketrans("",""), string.punctuation)
        wordlist.append(word)


# write the wordlist out to a file
def write_wordlist(wordlist, outfile):

    # remove duplicates and sort
    wordlist = list(set(wordlist))
    wordlist.sort()

    # remove URLs (of the form http://t.co)
    wordlist[:] = [word for word in wordlist if not ("http://t.co" in word
                   or "httptco" in word)]

    f = open_file(outfile, "a+")
    for element in wordlist:
        f.write("%s\n" % element)
    print "[+] Writing " + str(len(wordlist)) + " words to: " + outfile
    f.close()

    # convert words to lowercase
    wordlist_lower = [word.lower() for word in wordlist]
    # remove duplicates and sort
    wordlist_lower = list(set(wordlist_lower))
    wordlist_lower.sort()

    f = open_file("lower_" + outfile, "a+")
    for element in wordlist_lower:
        f.write("%s\n" % element)
    print "[+] Writing " + str(len(wordlist_lower)) + " words to: lower_" +\
          outfile
    f.close()


def main():
    count,outfile,username = get_options()
    api = authenticate()

    print "[*] Twitter username: " + username

    user = api.GetUser(screen_name=username)
    parse_user(user)

    statuses = api.GetUserTimeline(screen_name=username,
                                   count=count,
                                   include_rts=True)
    parse_statuses(statuses)

    write_wordlist(wordlist, outfile)


if __name__ == '__main__':
    main()


#TODO:
# add other authentication methods
# find more sources for words: friends, follow URLs?, etc.
# update README
