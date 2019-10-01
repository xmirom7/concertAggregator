#!/bin/sh

cd "$(dirname $0)" &&\
    sh ./build &&\
    docker run --rm -it --mount source="$(pwd)/../src/",target="$(pwd)/../src/",type=bind,readonly \
	   --mount source="$(pwd)/../",target="$(pwd)/../",type=bind \
	   concert-aggregator:stretch /bin/sh -c "cd $(realpath --canonicalize-existing $(pwd)/../src/) && python3 main.py"
