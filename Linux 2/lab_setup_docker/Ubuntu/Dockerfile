# syntax=docker/dockerfile:1.2
FROM ubuntu

RUN apt update \
    && apt install -y --no-install-recommends \
    git shadow vim sudo wget openssh-server \
    && rm -rf /var/lib/apt/lists/*

ADD docker-entrypoint.sh /usr/local/bin
ADD users.txt /var

RUN rm -rf /etc/ssh/ssh_host_rsa_key /etc/ssh/ssh_host_dsa_key

ENTRYPOINT [ "docker-entrypoint.sh" ]
CMD [ "/usr/sbin/sshd", "-D" ]
