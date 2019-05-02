import sys
sys.path.append('../API')
import solr
A=solr.SolrConnection('http://localhost:8502/solr/fp')
A.delete_query('track_id:[* TO *]')
A.commit()