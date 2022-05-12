pip install pyserial
sudo adduser $USER $(stat --format="%G" /dev/ttyACM0 )
sudo cp 70-roboclaw.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules && sudo service udev restart && sudo udevadm trigger