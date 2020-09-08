#!/bin/bash
cp -t /etc/systemd/system/ ./systemd/*.service;
echo 'Services created';
systemctl daemon-reload;

for entry in `ls ./systemd`; do
  echo 'Starting' $entry;
  sudo systemctl start $entry
done