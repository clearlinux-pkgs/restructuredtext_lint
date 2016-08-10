#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : restructuredtext_lint
Version  : 0.17.0
Release  : 16
URL      : http://pypi.debian.net/restructuredtext_lint/restructuredtext_lint-0.17.0.tar.gz
Source0  : http://pypi.debian.net/restructuredtext_lint/restructuredtext_lint-0.17.0.tar.gz
Summary  : reStructuredText linter
Group    : Development/Tools
License  : Unlicense
Requires: restructuredtext_lint-bin
Requires: restructuredtext_lint-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
restructuredtext-lint
=====================
.. image:: https://travis-ci.org/twolfson/restructuredtext-lint.png?branch=master
:target: https://travis-ci.org/twolfson/restructuredtext-lint
:alt: Build Status

%package bin
Summary: bin components for the restructuredtext_lint package.
Group: Binaries

%description bin
bin components for the restructuredtext_lint package.


%package python
Summary: python components for the restructuredtext_lint package.
Group: Default

%description python
python components for the restructuredtext_lint package.


%prep
%setup -q -n restructuredtext_lint-0.17.0

%build
export LANG=C
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/restructuredtext-lint
/usr/bin/rst-lint

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
