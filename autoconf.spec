#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xA7A16B4A2527436A (eblake@redhat.com)
#
Name     : autoconf
Version  : 2.69
Release  : 24
URL      : https://mirrors.kernel.org/gnu/autoconf/autoconf-2.69.tar.gz
Source0  : https://mirrors.kernel.org/gnu/autoconf/autoconf-2.69.tar.gz
Source1  : https://mirrors.kernel.org/gnu/autoconf/autoconf-2.69.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: autoconf-bin = %{version}-%{release}
Requires: autoconf-data = %{version}-%{release}
Requires: autoconf-info = %{version}-%{release}
Requires: autoconf-license = %{version}-%{release}
Requires: autoconf-man = %{version}-%{release}
BuildRequires : emacs
BuildRequires : grep
BuildRequires : sed
Patch1: 0001-tests-avoid-spurious-test-failure-with-libtool-2.4.3.patch

%description
Autoconf
Autoconf is an extensible package of M4 macros that produce shell
scripts to automatically configure software source code packages.
These scripts can adapt the packages to many kinds of UNIX-like
systems without manual user intervention.  Autoconf creates a
configuration script for a package from a template file that lists the
operating system features that the package can use, in the form of M4
macro calls.

%package bin
Summary: bin components for the autoconf package.
Group: Binaries
Requires: autoconf-data = %{version}-%{release}
Requires: autoconf-license = %{version}-%{release}

%description bin
bin components for the autoconf package.


%package data
Summary: data components for the autoconf package.
Group: Data

%description data
data components for the autoconf package.


%package info
Summary: info components for the autoconf package.
Group: Default

%description info
info components for the autoconf package.


%package license
Summary: license components for the autoconf package.
Group: Default

%description license
license components for the autoconf package.


%package man
Summary: man components for the autoconf package.
Group: Default

%description man
man components for the autoconf package.


%prep
%setup -q -n autoconf-2.69
cd %{_builddir}/autoconf-2.69
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592446096
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1592446096
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/autoconf
cp %{_builddir}/autoconf-2.69/COPYING %{buildroot}/usr/share/package-licenses/autoconf/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/autoconf-2.69/COPYINGv3 %{buildroot}/usr/share/package-licenses/autoconf/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/share/info/standards.info

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/autoconf
/usr/bin/autoheader
/usr/bin/autom4te
/usr/bin/autoreconf
/usr/bin/autoscan
/usr/bin/autoupdate
/usr/bin/ifnames

%files data
%defattr(-,root,root,-)
/usr/share/autoconf/Autom4te/C4che.pm
/usr/share/autoconf/Autom4te/ChannelDefs.pm
/usr/share/autoconf/Autom4te/Channels.pm
/usr/share/autoconf/Autom4te/Configure_ac.pm
/usr/share/autoconf/Autom4te/FileUtils.pm
/usr/share/autoconf/Autom4te/General.pm
/usr/share/autoconf/Autom4te/Getopt.pm
/usr/share/autoconf/Autom4te/Request.pm
/usr/share/autoconf/Autom4te/XFile.pm
/usr/share/autoconf/INSTALL
/usr/share/autoconf/autoconf/autoconf.m4
/usr/share/autoconf/autoconf/autoconf.m4f
/usr/share/autoconf/autoconf/autoheader.m4
/usr/share/autoconf/autoconf/autoscan.m4
/usr/share/autoconf/autoconf/autotest.m4
/usr/share/autoconf/autoconf/autoupdate.m4
/usr/share/autoconf/autoconf/c.m4
/usr/share/autoconf/autoconf/erlang.m4
/usr/share/autoconf/autoconf/fortran.m4
/usr/share/autoconf/autoconf/functions.m4
/usr/share/autoconf/autoconf/general.m4
/usr/share/autoconf/autoconf/go.m4
/usr/share/autoconf/autoconf/headers.m4
/usr/share/autoconf/autoconf/lang.m4
/usr/share/autoconf/autoconf/libs.m4
/usr/share/autoconf/autoconf/oldnames.m4
/usr/share/autoconf/autoconf/programs.m4
/usr/share/autoconf/autoconf/specific.m4
/usr/share/autoconf/autoconf/status.m4
/usr/share/autoconf/autoconf/types.m4
/usr/share/autoconf/autom4te.cfg
/usr/share/autoconf/autoscan/autoscan.list
/usr/share/autoconf/autotest/autotest.m4
/usr/share/autoconf/autotest/autotest.m4f
/usr/share/autoconf/autotest/general.m4
/usr/share/autoconf/autotest/specific.m4
/usr/share/autoconf/m4sugar/foreach.m4
/usr/share/autoconf/m4sugar/m4sh.m4
/usr/share/autoconf/m4sugar/m4sh.m4f
/usr/share/autoconf/m4sugar/m4sugar.m4
/usr/share/autoconf/m4sugar/m4sugar.m4f
/usr/share/autoconf/m4sugar/version.m4
/usr/share/emacs/site-lisp/autoconf-mode.el
/usr/share/emacs/site-lisp/autoconf-mode.elc
/usr/share/emacs/site-lisp/autotest-mode.el
/usr/share/emacs/site-lisp/autotest-mode.elc

%files info
%defattr(0644,root,root,0755)
/usr/share/info/autoconf.info

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/autoconf/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/autoconf/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/autoconf.1
/usr/share/man/man1/autoheader.1
/usr/share/man/man1/autom4te.1
/usr/share/man/man1/autoreconf.1
/usr/share/man/man1/autoscan.1
/usr/share/man/man1/autoupdate.1
/usr/share/man/man1/config.guess.1
/usr/share/man/man1/config.sub.1
/usr/share/man/man1/ifnames.1
