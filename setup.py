#!/usr/bin/python3

import os
from setuptools import setup, find_packages

setup(
    name="Optimus-indicator",
    version="3.0",
    description="Manjaro-Optimus Application Indicator",
    url='https://github.com/linesma/manjaroptimus-appindicator',
    author='Mark Lines',
    license='GPLv3',
    packages=["Optimus-indicator", "Optimus-indicator.manjaroptimusindicator", "Optimus-indicator.scripts", "Optimus-indicator.autostart", "Optimus-indicator.bin", "Optimus-indicator.icons", "Optimus-indicator.pkexec"],
    include_package_data=True,
    package_data={
            "Optimus-indicator": [
	      "manjaroptimusindicator/*",
            "icons/*.svg",
            "scripts/*",
            "autostart/*.desktop",
		"pkexec/*",
            "bin/*"
        ]
    },
    scripts=["bin/manjaroptimus-appindicator"],
)

os.chmod ('/etc/xdg/autostart/manjaroptimus-appindicator.desktop', 0o755)
os.chmod ('/usr/bin/manjaroptimus-appindicator', 0o755)
os.chmod ('/usr/share/manjaroptimus-appindicator/scripts/pkexec_nvidia', 0o755)
os.chmod ('/usr/share/manjaroptimus-appindicator/scripts/pkexec_intel', 0o755)
os.chmod ('/usr/share/manjaroptimus-appindicator/scripts/reboot.sh', 0o755)
#os.chmod ('/usr/local/bin/set-intel.sh', 0o755)
#os.chmod ('/usr/local/bin/set-nvidia.sh', 0o755)

