FROM debian:stretch
MAINTAINER Miroslav Nagy <miroslav.nagy@centrum.sk>

ARG DEBIAN_FRONTEND=noninteractive

# Set /bin/sh to bash instead of dash.
RUN echo "dash dash/sh boolean false" | debconf-set-selections &&\
    dpkg-reconfigure dash &&\
    apt-get -qq update &&\
    apt-get -yqq --no-install-recommends dist-upgrade &&\
    # apt-utils are needed for a warning to go away. \
    apt-get install -yqq apt-utils &&\
    # Install favorite editor. \
    apt-get install -yqq emacs-nox &&\
    apt-get install -yqq --no-install-recommends python3 python3-pip &&\
    pip3 install beautifulsoup4 