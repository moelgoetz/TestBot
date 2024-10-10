FROM debian:latest
WORKDIR /root

COPY private/setup.sh /root
COPY private/startup.sh /usr/local/bin/startup.sh
ADD artifacts/ollama-linux-amd64.tgz /usr
RUN /root/setup.sh && rm -f /root/setup.sh

#VOLUME /data
ENTRYPOINT ["/usr/local/bin/startup.sh"]
