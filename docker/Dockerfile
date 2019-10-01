FROM debian:stretch
MAINTAINER Miroslav Nagy <miroslav.nagy@centrum.sk>

ENV DEBIAN_FRONTEND=noninteractive

# Set /bin/sh to bash instead of dash.
RUN echo "dash dash/sh boolean false" | debconf-set-selections &&\
    dpkg-reconfigure dash &&\
    apt-get -qq update &&\
    apt-get --yes -qq --no-install-recommends dist-upgrade &&\
    # apt-utils are needed for a warning to go away. \
    apt-get install --yes -qq --no-install-recommends apt-utils &&\
    # Install favorite editor. \
    apt-get install --yes -qq --no-install-recommends emacs-nox &&\
    apt-get install --yes -qq --no-install-recommends python3 python3-pip &&\
    pip3 install -qqq beautifulsoup4 