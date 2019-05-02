from django.core.management import call_command as A
from calaccess_campaign_browser.management.commands import CalAccessCommand as B
class C(B):
	help='Transforms and loads refined data from raw CAL-ACCESS source files'
	def handle(B,*C,**D):A('flushcalaccesscampaignbrowser');A('loadcalaccesscampaignfilers');A('loadcalaccesscampaignfilings');A('loadcalaccesscampaignsummaries');A('loadcalaccesscampaigncontributions');A('loadcalaccesscampaignexpenditures');A('scrapecalaccesscampaigncandidates');A('scrapecalaccesscampaignpropositions');B.success('Done!')