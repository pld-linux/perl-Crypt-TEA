#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	TEA
Summary:	Crypt::TEA Perl module - Tiny Encryption Algorithm
Summary(pl.UTF-8):	Moduł Perla Crypt::TEA - Tiny Encryption Algorithm
Name:		perl-Crypt-TEA
Version:	1.25
Release:	11
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6e53511e455724b40007e4f2c0050270
URL:		http://search.cpan.org/dist/Crypt-TEA/
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

%description -l pl.UTF-8
Ten moduł jest implementacją szyfrowania TEA (Tiny Encryption
Algorithm - niewielki algorytm szyfrowania). Obsługuje interfejs
Crypt::CBC. TEA jest 64-bitowym symetrycznym szyfrem blokowym ze
128-bitowym kluczem i zmienną liczbą kroków (zaleca się 32). Wymaga
mało czasu do uruchomienia i dla zapewnienia bezpieczeństwa polega na
dużej liczbie kroków, a nie skomplikowanym algorytmie. TEA został
opracowany przez Davida J. Wheelera i Rogera M. Needhama, a jego opis
można znaleźć pod adresem:
<http://www.ftp.cl.cam.ac.uk/ftp/papers/djw-rmn/djw-rmn-tea.html>.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/TEA/*.so
%{_mandir}/man3/*
