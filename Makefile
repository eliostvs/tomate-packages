remote_repo=ssh://aur@aur.archlinux.org/$(pkgname).git
local_repo=/tmp/$(pkgname)
pkgrel=1

ifndef pkgver
$(error pkgver is not set)
endif

ifndef pkgname
$(error pkgname is not set)
endif

aur:
	@echo "Starting release $(pkgversion)"; \
	rm -rf $(local_repo); \
	git clone $(remote_repo) $(local_repo); \
	cp -a $(pkgname)/PKGBUILD $(local_repo)/; \
	cd $(local_repo); \
	sed -i 's/pkgver=0.0.0/pkgver=$(pkgver)/' PKGBUILD; \
	sed -i 's/pkgrel=1/pkgrel=$(pkgrel)/' PKGBUILD; \
	updpkgsums; \
	git clean -f; \
	makepkg --printsrcinfo > .SRCINFO; \
	git commit -am 'Update version to $(pkgver)'; \
	git push;
