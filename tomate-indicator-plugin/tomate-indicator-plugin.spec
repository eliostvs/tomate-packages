#
# spec file for package tomate-indicator-plugin
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

%define real_name tomate
%define module_name %{real_name}_indicator_plugin

Name: %{real_name}-indicator-plugin
Version: 0.0.0
Release: 0
License: GPL-3.0+
Summary: Tomate indicator plugin
Source: %{name}-%{version}.tar.gz
Url: https://github.com/eliostvs/tomate-indicator-plugin

BuildRoot: %{_tmppath}/%{name}-%{version}-build

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: hicolor-icon-theme

Requires: hicolor-icon-theme

%if 0%{?fedora}
BuildArch: noarch
Requires: libappindicator-gtk3
%endif

%if 0%{?suse_version}
BuildArchitectures: noarch
Requires: typelib-1_0-AppIndicator3-0_1
%endif

%description
Tomate plugin that shows the session progress in indicator.

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

%post
%if 0%{?suse_version}
%icon_theme_cache_post
%endif
%if 0%{?fedora}
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%postun
%if 0%{?suse_version}
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
%{python3_sitelib}/*.egg-info
%dir %{_datadir}/%{real_name}/
%{_datadir}/%{real_name}/plugins/
%{_datadir}/icons/hicolor/*/*/*.*
%{_datadir}/icons/ubuntu-mono-light/
%{_datadir}/icons/ubuntu-mono-dark/
%doc AUTHORS COPYING README.md

%changelog
