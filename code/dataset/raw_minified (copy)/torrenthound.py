import re
from trackers.base_tracker import BaseTracker as A
class B(A):
	def __init__(A):super(B,A).__init__();A.name='TorrentHound'
	def extract_download_url(D,url):B=re.compile('/hash/');A=B.sub('/torrent/',url,1);C=A[:A.index('/torrent-info')];return C