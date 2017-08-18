# stop script on error
set -e

# Install instapush
pathcrontab="/var/spool/cron/crontabs/pi"
pathapache="/var/www"
printf "\Download instapush...\n"
pip install instapush

# install projectKunayWow if not already installed
if [ ! -d ./projectKunayWow ]; then
  printf "\nInstalling projectKunayWow...\n"
  git clone https://github.com/freddybarco/projectKunayWow.git
  pushd projectKunayWow
  SCRIPT_PATH=$PWD
  echo -e "@reboot $PWD/ngrokBash.sh" >> $pathcrontab
  echo -e "@reboot $PWD/pythonBash.sh" >> $pathcrontab
  popd
fi

# Permisos
SCRIPT_PATH=$PWD
chmod -R 755 ./projectKunayWow