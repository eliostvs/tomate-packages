FROM archlinux

ENV HOME=/home/pkg

ARG UID=1000
ARG GID=1000

RUN pacman -Sy --noconfirm binutils fakeroot make pacman-contrib sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
RUN groupadd -g $GID pkg && useradd -u $UID -r -g pkg -G wheel -m pkg

USER pkg:pkg

WORKDIR $HOME