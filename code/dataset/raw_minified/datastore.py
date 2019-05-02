from gcloud import datastore as A
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='/home/carlo/gcloud-vimhelp-hrd.json'
B=A.Client(dataset_id='vimhelp-hrd')