#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	TEA
Summary:	Crypt::TEA Perl module - Tiny Encryption Algorithm
Summary(pl):	Modu³ Perla Crypt::TEA - Tiny Encryption Algorithm
Name:		perl-Crypt-TEA
Version:	1.25
Release:	3
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6e53511e455724b40007e4f2c0050270
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements TEA (Tiny Encryption Algorithm) encryption. It
supports the Crypt::CBC interface. TEA is a 64-bit symmetric block
cipher with a 128-bit key and a variable number of rounds (32 is
recommended). It has a low setup time, and depends on a large number
of rounds for security, rather than a complex algorithm. It was
developed by David J. Wheeler and Roger M. Needham, and is described
at <http://www.ftp.cl.cam.ac.uk/ftp/papers/djw-rmn/djw-rmn-tea.html>.

%description -l pl
Ten modu³ jest implementacj± szyfrowania TEA (Tiny Encryption
Algorithm - niewielki algorytm szyfrowania). Obs³uguje interfejs
Crypt::CBC. TEA jest 64-bitowym symetrycznym szyfrem blokowym ze
128-bitowym kluczem i zmienn± liczb± kroków (zaleca siê 32). Wymaga
ma³o czasu do uruchomienia i dla zapewnienia bezpieczeñstwa polega na
du¿ej liczbie kroków, a nie skomplikowanym algorytmie. TEA zosta³
opracowany przez Davida J. Wheelera i Rogera M. Needhama, a jego opis
mo¿na znale¼æ pod adresem:
<http://www.ftp.cl.cam.ac.uk/ftp/papers/djw-rmn/djw-rmn-tea.html>.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Crypt/TEA.pm
%dir %{perl_vendorarch}/auto/Crypt/TEA
%{perl_vendorarch}/auto/Crypt/TEA/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/TEA/*.so
%{_mandir}/man3/*
