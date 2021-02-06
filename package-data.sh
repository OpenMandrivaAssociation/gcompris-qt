#!/bin/sh
# Make sure we have all the (not all common) deps of
# generate_all_rcc.sh
sudo dnf install id3v2 ffmpeg
git clone --depth 1 https://github.com/gcompris/GCompris-data
cd GCompris-data
./generate_all_rcc.sh
mkdir -p data2/backgroundMusic
cp -a voices/ogg/.rcc/voices-ogg data2/
cp -a background-music/.rcc/* data2/backgroundMusic/
cp -a voices/ogg/.rcc/words data2/
tar cf ../gcompris-qt-voices.tar data2
