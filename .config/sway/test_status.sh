#!/bin/sh

layouts=("us" "ru" "fr" "de")

layout_index=$(
	swaymsg -r -t get_inputs \
		| jq -r '.[] | select(.type=="keyboard") | .xkb_active_layout_index' \
		| head -n 1
)
layout="${layouts[$layout_index]}"

datetime=$(date +'%Y-%m-%d %T')

echo "$layout | $datetime"
sleep 1
