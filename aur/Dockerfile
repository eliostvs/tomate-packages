FROM archlinux

ENV HOME=/home/pkg
ARG UID=1000
ARG GID=1000

RUN groupadd -g $GID pkg && \
    useradd -u $UID -r -g $GID -G wheel -m pkg

RUN pacman -Sy --noconfirm binutils fakeroot make pacman-contrib sudo

RUN echo '%wheel ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER $UID:$GID

WORKDIR $HOME