#!/bin/env sh

# INIT
touch /tmp/sbar
kill -9 $(cat /tmp/sbar)
echo "$$" > /tmp/sbar

# MODULES
update_cpu () { 
	# sketchy way to calculate actual percent usage 
	cpu_idle=`top -b -n 1 | grep Cpu | awk '{print $8}'|cut -f 1 -d "."`
	cpu=`expr 100 - $cpu_idle`
}

update_memory () { 
	mem="$(free | head -n 2 | tail -n 1 | awk '{printf "%.0fM/%2.2f%%\n", $3/1000, $3/$2*100}')"
}

update_time () { 
	time="$(date "+%a %b %d %H:%M")" 
}

update_weather () { 
	weather="$(curl -s "wttr.in?format=1"| sed -E "s/^(.).*\+/\1/")" 
	#weather="$(curl -s "wttr.in?format="%t"")"
}

update_vol () { 
	vol="$([ "$(pamixer --get-mute)" = "false" ] && printf '' || printf '')$(pamixer --get-volume)%"
	vol="$(pactl list sinks | grep '^[[:space:]]Volume:' | \
	head -n $(( $SINK + 1 )) | tail -n 1 | sed -e 's,.* \([0-9][0-9]*\)%.*,\1,')"
}

btc () {
  btc="$(curl -s http://api.coindesk.com/v1/bpi/currentprice.json | jq -r .bpi.USD.rate)"
}
# set initial value 
update_vol

display () { 
  #printf "%s\n" " $event [$weather] [$memory $cpu] [$bat] [$backlight] [$vol] $time "
	xsetroot -name "₿ $btc | $weather | ⌨ $cpu% | ⚠ $mem | ^ $vol% | $time"
}
while true
do
	sleep 5 & wait && { 
		btc
		update_time
		update_cpu
		update_memory
		update_vol
		update_weather
		display
	}
done 
