# Manjaro-Optimus Indicator
Indicator and GUI switch for Optimus-Switch on Manjaro that works in many Desktop-Environments.

![Manjaro-Optimus Indicator](https://github.com/linesma/manjaroptimus-appindicator/blob/master/screenshots/screenshot.jpg)     

# Acknowledgements
This was inspired by Martin Wimpress' Mate Optimus project at: https://github.com/ubuntu-mate/mate-optimus and is a fork of openSUSE's suseprime-appindicator project at: https://github.com/openSUSE/suseprime-appindicator.

It has been updated to work with the Optimus-Switch program by dglt1, links are in the requirements section, on Manjaro.

Thank you to the authors of the above programs.

Thank you also goes to the members of the Manjaro forums who took the time to help me learn about and troubleshoot python. I truly do appreciate it.

# About

This is an indicator that resides in the system tray. It displays an icon that shows which graphics card, either nVidia or Intel, is in use, and allows the user to switch between the two via a GUI menu. No matter which Desktop-Environment is being used.

# Desktop Environments Supported

This program has been tested on and supports the following Desktop-Environments:
- XFCE
- KDE
- Gnome
- Budgie
- Cinnamon
- Mate
- LXDE

Unfortunately, while the program would run on LXQT, no indicator was displayed. It may work with tiling window managers, such as Bspwn and Awesome, but it has not been tested on them.

# Requirements
- The appropriate version of Optimus-Switch for your desktop envirnoment [Optimus-Switch Repositories] (https://github.com/dglt1).
- libappindicator-gtk3 package from the Manjaro Community Repository.

# Installation

#### Before installation, make a back-up of your system using your favorite back-up tool!!!

1. Install the version of Optimus-Switch for your chosen desktop environment.

2. Install libappindicator-gtk3 from the Manjaro Community Repository.
```
sudo pacman -S libappindicator-gtk3
```
3. Clone this repository to your computer and go to its folder.
```
git clone https://github.com/linesma/manjaroptimus-appindicator.git
cd manjaroptimus-appindicator
```

#### If you are using Gnome continue on, if not go to go to the next section.

Gnome requires slightly modified scripts to switch between the GPU's. While they are the same scripts in dglt's Optimus-Switch GDM repository, I have included them here for ease of installation.

4. Make the install script executable.
```
chmod a+x setupgn.py
```

5. Run the setup script.
```
sudo ./setupgn.py install
```

The setup script will then copy the files to the required directories and adjust their permissions as needed.

6. Once the install script has finished. Reboot the computer. Manjaro-Optimus Indicator is set to autostart when the computer boots.

#### For Desktop Environments other than Gnome.

4. Make the install script executable.
```
chmod a+x setup.py
```

5. Run the setup script.
```
sudo ./setup.py install
```

The setup script will then copy the files to the required directories and adjust their permissions as needed.

6. Once the install script has finished. Reboot the computer. Manjaro-Optimus Indicator is set to autostart when the computer boots.

# Troubleshooting

Q. I am getting an error message saying "Removed /etc/systemd/system/graphical.target.wants/disable-nvidia.service" or "Created symlink...."

A. This is not an error. It is notifying the user that the "set-intel" and the "set-nvidia" scripts are changing a systemd service. The script has still run and changed the graphics card. To stop this notification, run the "setupgn.py" file. It will change the "set-intel" and "set-nvidia" scripts to stop these notifications. 

# Uninstall

This section will be coming soon.

# Fun Stuff

I have included a second set of icons in the "more-icons/set01" folder. If you want to use them instead of the default, just copy them into the '/usr/share/icons/hicolor/symbolic/apps'. Hopefully I will be adding more icon choices in the future.

Enjoy!!!
