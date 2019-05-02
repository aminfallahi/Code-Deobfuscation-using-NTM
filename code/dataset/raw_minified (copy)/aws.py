'\nAmazon AWS-related utils.\n'
import boto
from django.conf import settings as B
def A():'\n    Returns an S3Connection object. Uses values from fabfile.env for creds.\n    ';A=B.S3_DB_BACKUP;return boto.connect_s3(A['AWS_ACCESS_KEY_ID'],A['AWS_SECRET_ACCESS_KEY'])