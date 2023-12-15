%define byaccdate 20230521

Name:       byacc
Summary:    Berkeley Yacc, a parser generator
Version:    2.0.%{byaccdate}
Release:    1
License:    Public Domain
URL:        http://invisible-island.net/byacc/byacc.html
Source0:    ftp://invisible-island.net/byacc/byacc-%{byaccdate}.tgz

%description
Byacc (Berkeley Yacc) is a public domain LALR parser generator which
is used by many programs during their build process.

If you are going to do development on your system, you will want to install
this package.

%prep
%setup -q -n %{name}-%{byaccdate}

%build

autoreconf -v -f -i
%configure --disable-static \
    --disable-dependency-tracking

%make_build

%install
%make_install

ln -s yacc $RPM_BUILD_ROOT/%{_bindir}/byacc
ln -s yacc.1 $RPM_BUILD_ROOT/%{_mandir}/man1/byacc.1

%check
make check

%files
%defattr(-,root,root,-)
%doc ACKNOWLEDGEMENTS CHANGES NEW_FEATURES NOTES NO_WARRANTY README
%{_bindir}/yacc
%{_bindir}/byacc
%{_mandir}/man1/yacc.1*
%{_mandir}/man1/byacc.1*
