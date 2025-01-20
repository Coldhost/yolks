#!/bin/bash

#
# Copyright (c) 2021 Matthew Penner
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Clear so it shows nicer
clear

#echo -e "\033[1;39;44m __    .  ..  .       , "
#echo -e '\033[1;39;44m/  ` _ | _||__| _  __-+-'
#echo -e "\033[1;39;44m\__.(_)|(_]|  |(_)_)  | "
#echo -e "\033[1;39;44m                        "

echo -e "\033[1;39;44m   ___      _     _                 _                "
echo -e "\033[1;39;44m  / __\___ | | __| | /\  /\___  ___| |_   ___ _   _  "
echo -e '\033[1;39;44m / /  / _ \| |/ _` |/ /_/ / _ \/ __| __| / _ \ | | | '
echo -e '\033[1;39;44m/ /__| (_) | | (_| / __  / (_) \__ \ |_ |  __/ |_| | '
echo -e '\033[1;39;44m\____/\___/|_|\__,_\/ /_/ \___/|___/\__(_)___|\__,_| '
echo -e "\033[1;39;44m                                                     "

echo -e ""
echo -e "Server is starting... "

# Default the TZ environment variable to UTC.
TZ=${TZ:-UTC}
export TZ

# Set environment variable that holds the Internal Docker IP
INTERNAL_IP=$(ip route get 1 | awk '{print $(NF-2);exit}')
export INTERNAL_IP

# Switch to the container's working directory
cd /home/container || exit 1

# Update ClamAV definitions (optional but recommended at runtime)
if [ "$ENABLE_AV" = 1 ]; then
	if find /home/container/clamav/quarantine -type f | grep -q .; then
		printf "\033[1m\033[33mcontainer@coldhost.eu~ \033[1;39;41mQuarantined files are in /clamav/quarantine, Please delete them to remove this warning\033[0m\n"
		exit
	fi
	echo -e "\033[1m\033[33mcontainer@coldhost.eu~ \033[1;39;44mUpdating Virus Databases...\033[0m"
	mkdir -p /home/container/clamav/logs /home/container/clamav/quarantine
	cp /freshclam.conf /home/container/clamav
	freshclam --config-file=/home/container/clamav/freshclam.conf
	echo -e "\033[1m\033[33mcontainer@coldhost.eu~ \033[1;39;44mScanning the home directory with ClamAV AntiVirus...\033[0m"
	if [ "$ONLY_PLUGINS" = 1 ]; then
		clamscan -r --move=/home/container/clamav/quarantine --log=/home/container/clamav/logs/clamscan.txt --database=/home/container/clamav/ --infected --include="^[^\.]+$" --include="\.jar$" --exclude-dir="\.cache" --exclude="\.paper-remapped$" /home/container/plugins
	else
		echo -e "THIS MAY TAKE UNDER 10 MINUTES"
		clamscan -r --move=/home/container/clamav/quarantine --log=/home/container/clamav/logs/clamscan.txt --database=/home/container/clamav/ --infected --include="^[^\.]+$" --include="\.jar$" --exclude-dir="\.cache" --exclude="\.paper-remapped$" /home/container
	fi
	if find /home/container/clamav/quarantine -type f | grep -q .; then
		printf "\033[1m\033[33mcontainer@coldhost.eu~ \033[1;39;41mQuarantined files are in /clamav/quarantine, Please delete them to remove this warning\033[0m\n"
		exit
	fi
else
    printf "\033[1m\033[33mcontainer@coldhost.eu~ \033[1;39;44mWARNING: Antivirus scanning is disabled.\n"
fi

# Scan the home directory

# Print Java version
printf "\033[1m\033[33mcontainer@coldhost.eu~ \033[1;39;44mjava -version\n"
java -version

# Convert all of the "{{VARIABLE}}" parts of the command into the expected shell
# variable format of "${VARIABLE}" before evaluating the string and automatically
# replacing the values.
PARSED=$(echo "${STARTUP}" | sed -e 's/{{/${/g' -e 's/}}/}/g' | eval echo "$(cat -)")

# Display the command we're running in the output, and then execute it with the env
# from the container itself.
printf "\033[1m\033[33mcontainer@coldhost.eu~ \033[1;39;44m%s\n" "$PARSED"
# shellcheck disable=SC2086
exec env ${PARSED}
