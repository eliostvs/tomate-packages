FROM archlinux

ENV HOME=/home/pkg
ARG UID=1000
ARG GID=1000

RUN groupadd -g $GID pkg && useradd -u $UID -r -g $GID -G wheel -m pkg

RUN echo '%wheel ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

RUN echo $'\n\
[archlinuxfr]\n\
SigLevel = Never\n\
Server = http://repo.archlinux.fr/$arch\n\
' >> /etc/pacmand.conf

RUN pacman -Sy --noconfirm binutils fakeroot make pacman-contrib sudo wget git

USER $UID:$GID

WORKDIR $HOME
