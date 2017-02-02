#!/bin/bash
if [ ! -d zipped ]; then
	mkdir zipped
fi
cp gsacwget.sh zipped/
cd zipped/
/bin/bash gsacwget.sh
rm gsacwget.sh
cd ..

