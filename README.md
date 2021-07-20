@see @credits https://alexbloggt.com/lueftersteuerung/

* git clone project to /opt/pifancontrol
* create symlink for systemd: ln -s /opt/pifancontrol/fan_control.service /etc/systemd/system/
* reload deamon: systemctl daemon-reload
* start: systemctl start fan_control.service
* enable autostart: systemctl enable fan_control.service
* check status: systemctl status fan_control.service
* stress test: sudo apt-get update && sudo apt-get install -y stress && stress -t 30 -c 4