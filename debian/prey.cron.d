# /etc/cron.d/prey: crontab entries for the prey package

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
SHELL=/bin/bash

*/20 * * * * root /usr/lib/prey/prey.sh >/var/log/prey.log
