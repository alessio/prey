Description: Adjust prey-config.py according to the Debian customization.
 Application modules are installed in /usr/lib/prey/.
 Configuration is stored in /etc/prey/config.
---
 platform/linux/prey-config.py |    4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)

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
