for entry in `ls ./systemd`; do
  sudo systemctl stop $entry;
  rm /etc/systemd/system/$entry;
  echo 'Deleted' $entry
done