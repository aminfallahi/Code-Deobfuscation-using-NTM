'Reindex add-ons to fix stale data left by changes to the post_save\nhandler.'
from addons.cron import reindex_addons as A
A()