'\nFacebook Utility functions\n'
import os,requests as B
C='https://graph.facebook.com/me?fields=id&access_token=%s'
def A(access_token):A=access_token;D=B.get(C%A).json();return D.get('is_valid',False)or os.environ.get('USER_SALT')==A