## Define oauth application id and secret.
## FB_CLIENT_ID='xxx'
## FB_CLIENT_SECRET="yyyy"

## import required modules
## try:
##     import json
## except ImportError:
##     from gluon.contrib import simplejson as json
## from facebook import GraphAPI, GraphAPIError
## from gluon.contrib.login_methods.oauth20_account import OAuthAccount


## extend the OAUthAccount class
##class FaceBookAccount(OAuthAccount):
##    """OAuth impl for FaceBook"""
##    AUTH_URL="https://graph.facebook.com/oauth/authorize"
##    TOKEN_URL="https://graph.facebook.com/oauth/access_token"
##
##    def __init__(self):
##        OAuthAccount.__init__(self, None, FB_CLIENT_ID, FB_CLIENT_SECRET,
##                              self.AUTH_URL, self.TOKEN_URL,
##                              scope='email,user_about_me,user_activities, user_birthday, user_education_history, user_groups, user_hometown, user_interests, user_likes, user_location, user_relationships, user_relationship_details, user_religion_politics, user_subscriptions, user_work_history, user_photos, user_status, user_videos, publish_actions, friends_hometown, friends_location,friends_photos',
##                              state="auth_provider=facebook",
##                              display='popup')
##        self.graph = None
##
##    def get_user(self):
##        '''Returns the user using the Graph API.
##'''
##        if not self.accessToken():
##            return None
##
##        if not self.graph:
##            self.graph = GraphAPI((self.accessToken()))
##
##        user = None
##        try:
##            user = self.graph.get_object("me")
##        except GraphAPIError, e:
##            session.token = None
##            self.graph = None
##
##        if user:
##            if not user.has_key('username'):
##                username = user['id']
##            else:
##                username = user['username']
##
##            if not user.has_key('email'):
##                email = '%s.fakemail' %(user['id'])
##            else:
##                email = user['email']
##
##            return dict(first_name = user['first_name'],
##                        last_name = user['last_name'],
##                        username = username,
##                        email = '%s' %(email) )

## use the above class to build a new login form
## auth.settings.login_form=FaceBookAccount()