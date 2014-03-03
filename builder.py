#!/usr/bin/python
# -*- coding: utf-8 -*-

import ConfigParser
import optparse
import os
import twitter

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

def get_options():
    parser = optparse.OptionParser('usage:\r\n builder.py -u <username>')

    parser.add_option('-u', dest='username', type='string',\
      help='specify Twitter username')

    (options, args) = parser.parse_args()

    username = options.username

    if username == None:
        print parser.usage
        exit(0)

    return username

def main():
    username = get_options()
    api = authenticate()

    print api.VerifyCredentials()

    print "[+] Fetching statuses for user: " + username
    statuses = api.GetUserTimeline(screen_name=username)

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
'''
     status.contributors
     status.coordinates
     status.created_at
     status.created_at_in_seconds # read only
     status.favorited
     status.favorite_count
     status.geo
     status.id
     status.in_reply_to_screen_name
     status.in_reply_to_user_id
     status.in_reply_to_status_id
     status.lang
     status.place
     status.retweet_count
     status.relative_created_at # read only
     status.source
     status.text
     status.truncated
     status.location
     status.user
     status.urls
     status.user_mentions
     status.hashtags
'''

if __name__ == '__main__':
    main()


#TODO:
# add other authentication methods
