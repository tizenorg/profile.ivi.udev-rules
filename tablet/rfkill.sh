#!/bin/sh
#
# rfkill.sh	Used to enable/disable all the rfkill devices on Oaktrail
#
# Authors:	Yin Kangkai <kangkai.yin@intel.com>

# check if we already have rfkill, otherwise have to program into /sys directly
RFKILL=""
if [ -x /sbin/rfkill ]; then
	RFKILL="/sbin/rfkill"
fi


enable() {
	if [ x$RFKILL != x ]; then
		$RFKILL unblock all
		return
	else
		# program directly into /sys, not implement yet
		echo "please install package rfkill"
		return
	fi
}

disable() {
	if [ x$RFKILL != x ]; then
		$RFKILL block all
		return
	else
		# program directly into /sys, not implement yet
		echo "please install package rfkill"
		return
	fi
}


case "$1" in
  enable|add)
	enable
	exit 0
	;;
  disable|remove)
	disable
	exit 0
	;;
  *)
        echo $"Usage: $0 {enable|add|disable|remove}"
        exit 1
esac
exit 0

