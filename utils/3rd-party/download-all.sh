#!/bin/bash
# $File: download-all.sh
# $Date: Wed Feb 15 19:17:26 2012 +0800
# $Author: jiakai <jia.kai66@gmail.com>

grep -v '^#' list | \
	while read addr fname 
	do
		wget "$addr" -c -O "$fname"
	done


# unzip uglifyjs
unzip uglifyjs.zip -d uglifyjs
orig_dir=uglifyjs/$(ls uglifyjs)
mv $orig_dir/* uglifyjs
rm -rf $orig_dir

