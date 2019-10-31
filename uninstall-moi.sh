#!/bin/sh

#Manjaro-Optimus Indicator uninstall script.

if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

echo 'Removing Manjaro-Optimus Indicator'

rm -rf /usr/share/icons/hicolor/symbolic/apps/manjaroptimus-symbolic.svg
rm -rf /usr/share/icons/hicolor/symbolic/apps/manjaroptimus-intel-symbolic.svg
rm -rf /usr/share/icons/hicolor/symbolic/apps/manjaroptimus-nvidia-symbolic.svg
rm -rf /usr/share/manjaroptimus-appindicator/scripts/pkexec_nvidia
rm -rf /usr/share/manjaroptimus-appindicator/scripts/pkexec_intel
rm -rf /usr/share/polkit-1/actions/org.freedesktop.policykit.set-nvidia.sh.policy
rm -rf /usr/share/polkit-1/actions/org.freedesktop.policykit.set-intel.sh.policy
rm -rf /etc/xdg/autostart/manjaroptimus-appindicator.desktop
rm -rf /usr/bin/manjaroptimus-appindicator

sleep 1
echo 'Manjaro-Optimus Indicator is now uninstalled.'
echo 'To complete the uninstall process, please restart your computer'

rm -rf uninstall-moi.sh
