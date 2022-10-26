#!/bin/sh
# Filter out stable releases (which go to wesnoth)
git ls-remote --tags https://github.com/wesnoth/wesnoth 2>/dev/null|awk '{ print $2; }' |sed -e 's,refs/tags/,,;s,_,.,g' |grep -v '\^{}' |grep '1\.1[79]' |sort -V |tail -n1
