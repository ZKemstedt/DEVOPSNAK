# syntax=docker/dockerfile:1.2
FROM alpine:3.14

RUN apk add --update --no-cache git shadow vim wget doas sed openssh

RUN groupadd -r zephyro \
	&& useradd --no-log-init -m -g zephyro zephyro \
	&& echo "zephyro:skt" | chpasswd \
	&& echo "permit zephyro as root" >> /etc/doas.conf

COPY ./keys/desktop.pub /home/zephyro/desktop.pub
COPY ./keys/macbook.pub /home/zephyro/macbook.pub

RUN mkdir /home/zephyro/.ssh \
&& cat /home/zephyro/desktop.pub >> /home/zephyro/.ssh/authorized_keys \
&& cat /home/zephyro/macbook.pub >> /home/zephyro/.ssh/authorized_keys \
&& sed -i 's/#PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config

ADD docker-entrypoint.sh /usr/local/bin

RUN rm -rf /etc/ssh/ssh_host_rsa_key /etc/ssh/ssh_host_dsa_key

ENTRYPOINT [ "docker-entrypoint.sh" ]
CMD [ "/usr/sbin/sshd", "-D" ]
