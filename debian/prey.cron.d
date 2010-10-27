# /etc/cron.d/prey: crontab entries for the prey package

*/20 * * * * root /usr/lib/prey/prey.sh >/var/log/prey.log
