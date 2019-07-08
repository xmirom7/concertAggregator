#!/bin/sh

cd "$(dirname $0)"
docker run --rm -it --mount source="$(pwd)",target="$(pwd)",type=bind concert-aggregator:stretch /bin/sh -c "cd $(pwd) && python3 main.py"
