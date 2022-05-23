#!/bin/env sh

# INIT
touch /tmp/sbar
kill -9 $(cat /tmp/sbar)
echo "$$" > /tmp/sbar

# MODULES
update_cpu () { 
	# sketchy way to calculate actual percent usage 
	cpu_idle=`top -b -n 1 | grep Cpu | awk '{print $8}'|cut -f 1 -d "."`
	# when 0% usage
	if [[ $cpu_idle = "id," ]]; then
		cpu_idle=100
	fi
	cpu=`expr 100 - $cpu_idle`
}

update_memory () { 
	mem="$(free | head -n 2 | tail -n 1 | awk '{printf "%.0fM/%2.2f%%\n", $3/1000, $3/$2*100}')"
}

update_time () { 
	time="$(date "+%a %b %d %H:%M")" 
}

update_weather () { 
	weather_api="$(curl -s "wttr.in?format=1"| sed -E "s/^(.).*\+/\1/")" 
	if [[ ${#weather_api} -gt 1 && ${#weather_api} -lt 10 ]]; then 
		weather="$weather_api | "
	else
		weather=""
	fi
}

update_vol () { 
	vol="$(pactl list sinks | grep '^[[:space:]]Volume:' | \
	head -n $(( $SINK + 1 )) | tail -n 1 | sed -e 's,.* \([0-9][0-9]*\)%.*,\1,')"
}

update_btc () {
	btc_api="$(curl -s http://api.coindesk.com/v1/bpi/currentprice.json | jq -r .bpi.USD.rate)"
	if [[ ${#btc_api} -gt 0 ]]; then
		btc="₿ $btc_api |"
	else 
		btc=""
	fi
}
# set initial value 
update_vol

display () { 
  #printf "%s\n" " $event [$weather] [$memory $cpu] [$bat] [$backlight] [$vol] $time "
	xsetroot -name "$btc $weather⌨ $cpu% | ⚠ $mem | ^ $vol% | $time"
}

update_btc
update_weather

iter=0
while true
do
	sleep 3 & wait && { 
		iter=$((iter + 1))
		if [[ $(($iter % 20)) -eq 0 ]]; then
			update_btc
			update_weather
		fi
		if [[ $(($iter % 2)) -eq 0 ]]; then 
			update_vol
		fi
		if [[ $((iter)) -gt 1000 ]]; then
			iter=0
		fi
		update_time
		update_cpu
		update_memory
		display
	}
done 
