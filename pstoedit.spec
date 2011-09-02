Name:           pstoedit
Version:        3.45
Release:        10%{?dist}
Summary:        Translates PostScript and PDF graphics into other vector formats

Group:          Applications/Productivity
License:        GPLv2+
URL:            http://www.pstoedit.net/
Source0:        http://downloads.sourceforge.net/project/pstoedit/pstoedit/%{version}/pstoedit-%{version}.tar.gz
Patch0:		pstoedit-3.44-cxxflags.patch
Patch1:		pstoedit-3.45-quiet.patch
Patch2:		pstoedit-3.45-gcc43.patch
Patch3:         pstoedit-3.45-asy.patch
Patch4:         pstoedit-3.45-elif.patch
# Patch5: fix parallel build
Patch5:         pstoedit-3.45-build.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	ghostscript
BuildRequires:	gd-devel
BuildRequires:	libpng-devel
BuildRequires:	dos2unix
BuildRequires:	ghostscript
BuildRequires:	plotutils-devel
%ifnarch ia64
BuildRequires:	libEMF-devel
%endif


%description
Pstoedit converts PostScript and PDF files to various vector graphic
formats. The resulting files can be edited or imported into various
drawing packages. Pstoedit comes with a large set of integrated format
drivers


%package devel
Summary:        Headers for developing programs that will use %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:	libpng-devel

%description devel
This package contains the header files needed for developing %{name}
applications


%prep
%setup -q
%patch0 -p1 -b .cxxflags
%patch1 -p1 -b .quiet
%patch2 -p1 -b .gcc43
%patch3 -p1 -b .asy
%patch4 -p1 -b .elif
%patch5 -p1 -b .build
dos2unix doc/*.htm doc/readme.txt


%build
# Buildling without ImageMagick support, to work around bug 507035
%configure --disable-static --with-emf --without-swf --without-magick
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 doc/pstoedit.1 $RPM_BUILD_ROOT%{_mandir}/man1/
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, -)
%doc copying doc/readme.txt doc/index.htm doc/pstoedit.htm
%{_datadir}/pstoedit
%{_mandir}/man1/*
%{_bindir}/pstoedit
%{_libdir}/*.so.*
%{_libdir}/pstoedit


%files devel
%defattr(-, root, root, -)
%doc doc/changelog.htm
%{_includedir}/pstoedit
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4


%changelog
* Thu Jan 07 2010 Jiri Popelka <jpopelka@redhat.com> - 3.45-10
- Fixed Source0 URL

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 3.45-9.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.45-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul  9 2009 Denis Leroy <denis@poolshark.org> - 3.45-8
- Fix parallel build (#510281)
- Remove ImageMagick support, to work around bug 507035

* Tue Mar 10 2009 Denis Leroy <denis@poolshark.org> - 3.45-7
- Removed EMF BR for ia64 arch (#489412)
- Rebuild for ImageMagick

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.45-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb  7 2009 Denis Leroy <denis@poolshark.org> - 3.45-5
- Added patch for improved asymptote support (#483503)
- Added patch to fix incorrect cpp directive

* Wed Sep 24 2008 Denis Leroy <denis@poolshark.org> - 3.45-4
- Fixed cxxflags patch fuziness issue

* Wed May 14 2008 Denis Leroy <denis@poolshark.org> - 3.45-3
- Rebuild for new ImageMagick

* Sun Feb 17 2008 Denis Leroy <denis@poolshark.org> - 3.45-2
- Added patch for gcc 4.3 rebuild

* Thu Sep 20 2007 Denis Leroy <denis@poolshark.org> - 3.45-1
- Update to new upstream 3.45, bugfix release
- Updated quiet patch for 3.45

* Mon Aug 20 2007 Denis Leroy <denis@poolshark.org> - 3.44-7
- License tag update

* Sun Mar 25 2007 Denis Leroy <denis@poolshark.org> - 3.44-6
- Added patch to add -quiet option

* Wed Nov 22 2006 Denis Leroy <denis@poolshark.org> - 3.44-5
- Added libEMF support

* Mon Aug 28 2006 Denis Leroy <denis@poolshark.org> - 3.44-4
- FE6 Rebuild

* Fri Aug 18 2006 Denis Leroy <denis@poolshark.org> - 3.44-3
- Added svg/libplot support

* Thu Jun 15 2006 Denis Leroy <denis@poolshark.org> - 3.44-2
- Added missing Requires and BuildRequires
- Patched configure to prevent CXXFLAGS overwrite

* Thu Jun  8 2006 Denis Leroy <denis@poolshark.org> - 3.44-1
- First version

