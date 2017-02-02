#!/bin/bash
if [ ! -d unzipped ]; then
	mkdir unzipped
fi
for zipped in zipped/*.Z; do
	7z e $zipped -ounzipped/
done
