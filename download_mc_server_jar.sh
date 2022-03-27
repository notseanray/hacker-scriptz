#!/bin/bash
if [ $1 == "1.12.2" ]; then
	wget https://launcher.mojang.com/mc/game/1.12.2/server/886945bfb2b978778c3a0288fd7fab09d315b25f/server.jar
fi
if [ $1 == "1.16.5" ]; then
	wget https://launcher.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar
fi
if [ $1 == "1.18.2" ]; then
	wget https://launcher.mojang.com/v1/objects/c8f83c5655308435b3dcf03c06d9fe8740a77469/server.jar
fi
