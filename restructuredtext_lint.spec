#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : restructuredtext_lint
Version  : 1.3.1
Release  : 48
URL      : https://files.pythonhosted.org/packages/36/a6/507be0d9125cd37530e96062b7f838ee1777a0e30855197964603da7b990/restructuredtext_lint-1.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/36/a6/507be0d9125cd37530e96062b7f838ee1777a0e30855197964603da7b990/restructuredtext_lint-1.3.1.tar.gz
Summary  : reStructuredText linter
Group    : Development/Tools
License  : Unlicense
Requires: restructuredtext_lint-bin = %{version}-%{release}
Requires: restructuredtext_lint-license = %{version}-%{release}
Requires: restructuredtext_lint-python = %{version}-%{release}
Requires: restructuredtext_lint-python3 = %{version}-%{release}
Requires: docutils
BuildRequires : buildreq-distutils3
BuildRequires : docutils

%description
=====================

%package bin
Summary: bin components for the restructuredtext_lint package.
Group: Binaries
Requires: restructuredtext_lint-license = %{version}-%{release}

%description bin
bin components for the restructuredtext_lint package.


%package license
Summary: license components for the restructuredtext_lint package.
Group: Default

%description license
license components for the restructuredtext_lint package.


%package python
Summary: python components for the restructuredtext_lint package.
Group: Default
Requires: restructuredtext_lint-python3 = %{version}-%{release}

%description python
python components for the restructuredtext_lint package.


%package python3
Summary: python3 components for the restructuredtext_lint package.
Group: Default
Requires: python3-core
Provides: pypi(restructuredtext_lint)
Requires: pypi(docutils)

%description python3
python3 components for the restructuredtext_lint package.


%prep
%setup -q -n restructuredtext_lint-1.3.1
cd %{_builddir}/restructuredtext_lint-1.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1591289688
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/restructuredtext_lint
cp %{_builddir}/restructuredtext_lint-1.3.1/UNLICENSE %{buildroot}/usr/share/package-licenses/restructuredtext_lint/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/restructuredtext-lint
/usr/bin/rst-lint

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/restructuredtext_lint/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
