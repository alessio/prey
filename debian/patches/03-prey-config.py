Description: Adjust prey-config.py according to the Debian customization.
 Application modules are installed in /usr/lib/prey/.
 Configuration is stored in /etc/prey/config.
---
 platform/linux/prey-config.py |    6 +++---
 1 file changed, 3 insertions(+), 3 deletions(-)

--- prey.orig/platform/linux/prey-config.py
+++ prey/platform/linux/prey-config.py
@@ -41,8 +41,8 @@ _ = gettext.gettext
 # vars and such
 ################################################
 
-PREY_PATH = '/usr/share/prey'
-CONFIG_FILE = PREY_PATH + '/config'
+PREY_PATH = '/usr/lib/prey'
+CONFIG_FILE = '/etc/prey/config'
 CONTROL_PANEL_URL = 'http://control.preyproject.com'
 CONTROL_PANEL_URL_SSL = 'https://control.preyproject.com'
 GUEST_ACCOUNT_NAME = 'guest_account'
@@ -293,7 +293,7 @@ class PreyConfigurator(object):
 			return True
 
 	def is_config_writable(self):
-		command = 'if [ ! -w "'+PREY_PATH+'/config" ]; then echo 1; fi'
+		command = 'if [ ! -w "%s" ]; then echo 1; fi' % CONFIG_FILE
 		no_access = os.popen(command).read().strip()
 		if no_access == '1':
 			self.show_alert(_("Unauthorized"), _("You don't have access to manage Prey's configuration. Sorry."), True)
