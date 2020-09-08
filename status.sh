for entry in `ls ./systemd`; do
  echo "Status" $entry;
  if systemctl status $entry | grep "Process: *" > /dev/null; then
    if systemctl status $entry | grep "status=0" > /dev/null; then
      tput sgr0;
      systemctl status $entry | grep "Process: *";
      systemctl status $entry | grep "Active: *";
    else
      tput setaf 1;
      systemctl status $entry | grep "Process: *";
      systemctl status $entry | grep "Active: *";
    fi
  else
    tput setaf 2;
    systemctl status $entry | grep "Active: *";
  fi
  echo "";
  tput sgr0;
done