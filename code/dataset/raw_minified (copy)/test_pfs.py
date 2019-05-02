from pyquery import PyQuery as A
from olympia.amo.tests import TestCase as B
from services.pfs import get_output as C
class D(B):
	def test_xss(E):
		for B in ['name','mimetype','guid','version','iconUrl','InstallerLocation','InstallerHash','XPILocation','InstallerShowsUI','manualInstallationURL','licenseURL','needsRestart']:D=C({B:'fooo<script>alert("foo")</script>;'});assert not A(D)('script')