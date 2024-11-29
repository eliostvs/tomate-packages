#
# spec file for package tomate-gtk
#
# Copyright (c) 2014 Elio Esteves Duarte <elio.esteves.duarte@gmail.com>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define modname tomate

Name: %{modname}-gtk
Version: 0.5.0
Release: 0
License: GPL-3.0+
Summary: A Pomodoro timer
Source: %{name}-%{version}.tar.gz
Url: https://github.com/eliostvs/tomate-gtk

BuildRoot: %{_tmppath}/%{name}-%{version}-build

BuildRequires: python3-devel
BuildRequires: python3-setuptools

Requires: notification-daemon
Requires: python3-blinker
Requires: python3-gobject
Requires: python3-pyxdg
Requires: python3-setuptools
Requires: python3-venusian
Requires: python3-wiring
Requires: python3-wrapt
Requires: python3-yapsy
Requires: playerctl-libs

%if 0%{?fedora}
BuildArch: noarch
Requires: gstreamer1-plugins-base
Requires: gstreamer1-plugins-good
Requires: gtk3
Requires: libnotify
Requires: python3-dbus
Requires: python3-gstreamer1
Requires: python3-packaging
%endif

%if 0%{?suse_version}
BuildArchitectures: noarch
BuildRequires: desktop-file-utils
BuildRequires: hicolor-icon-theme
Requires: gstreamer-plugins-base
Requires: gstreamer-plugins-good
Requires: python3-dbus-python
Requires: python311-packaging
Requires: typelib-1_0-Gst-1_0
Requires: typelib-1_0-Gtk-3_0
Requires: typelib-1_0-Notify-0_7
%endif

Conflicts: tomate-alarm-plugin
Conflicts: tomate-notify-plugin
Conflicts: tomate-exec-plugin
Conflicts: tomate-breakscreen-plugin
Conflicts: tomate-playerautopause-plugin

%description
A Pomodoro timer written in Gtk3 and Python for Linux desktops.

%prep
%setup -q -n %{name}-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%post
%if 0%{?suse_version}
%desktop_database_post
%icon_theme_cache_post
%endif
%if 0%{?fedora}
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%postun
%if 0%{?suse_version}
%desktop_database_postun
%icon_theme_cache_postun
%endif
%if 0%{?fedora}
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
%endif

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*.*
%dir %{_datadir}/%{modname}
%{_datadir}/%{modname}/media/
%{_datadir}/%{modname}/plugins/
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{modname}

%doc AUTHORS COPYING README.md CHANGELOG.md

%changelog
