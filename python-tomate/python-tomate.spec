#
# spec file for package python-tomate
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
#

%define real_name tomate

Name: python-%{real_name}
Version: 0.0.0
Release: 0
License: GPL-3.0+
Source0: README.md
Url: https://github.com/eliostvs/tomate
Summary: A pomodoro timer

BuildRoot: %{_tmppath}/%{name}-%{version}-build

%if 0%{?fedora}
BuildArch: noarch
%endif

%if 0%{?suse_version}
BuildArchitectures: noarch
%endif

%description
This package has been joined to tomate-gtk.

To prevent upgrade problems in the tomate-gtk, this package will be still a dependency of it but will be empty.

%prep
cp %{SOURCE0} .

%build
#nothing to do

%install
# nothing to do

%files
%defattr(-,root,root,-)
%doc README.md

%changelog
* Wed Feb 10 2021 elio.esteves.duarte@gmail.com
- Dummy package