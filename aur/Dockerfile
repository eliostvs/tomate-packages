FROM archlinux

ARG HOME=/home/pkg
ARG USER=pkg
ARG UID=999
ARG GID=999

RUN groupadd -g ${GID} pkg && useradd -u ${UID} -r -g ${GID} -G wheel -m ${USER}

RUN echo "${USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

RUN echo $'\n\
[archlinuxfr]\n\
SigLevel = Never\n\
Server = http://repo.archlinux.fr/$arch\n\
' >> /etc/pacmand.conf

RUN pacman -Sy --noconfirm binutils fakeroot make pacman-contrib sudo wget git

USER ${UID}:${GID}

WORKDIR ${HOME}
