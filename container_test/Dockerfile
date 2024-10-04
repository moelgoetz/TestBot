#FROM opensuse/tumbleweed
#WORKDIR /root
#
#COPY private/setup.sh /root
#RUN /root/setup.sh && rm -f /root/setup.sh
#
#VOLUME /data

FROM debian:latest
WORKDIR /root

COPY private/setup.sh /root
RUN /root/setup.sh && rm -f /root/setup.sh

VOLUME /data
