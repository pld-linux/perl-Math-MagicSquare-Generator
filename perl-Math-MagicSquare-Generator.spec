#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	MagicSquare-Generator
Summary:	Math::MagicSquare::Generator - Magic Square generator
Summary(pl):	Math::MagicSquare::Generator - generator kwadratów magicznych
Name:		perl-Math-MagicSquare-Generator
Version:	0.01
Release:	1
License:	Public Domain
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	408501cf0474f95234eb1bfdb4832d42
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module creates magic squares. A magic square is a square in which
all numbers are different and the sums of all rows, all columns and
the two diagonals are equal.

Math::MagicSquare::Generator cannot create panmagic squares, or
squares that have an even size. (A panmagic square is magic square
where the "wrapped" diagonals are also equal.)

%description -l pl
Ten modu³ tworzy kwadraty magiczne. Kwadrat magiczny to kwadrat, w
którym wszystkie liczby s± ró¿ne, a sumy we wszystkich wierszach,
we wszystkich kolumnach i na dwóch przek±tnych s± równe.

Math::MagicSquare::Generator nie potrafi tworzyæ kwadratów
panmagicznych ani kwadratów o parzystym rozmiarze (kwadrat panmagiczny
to kwadrat magiczny, w którym sumy na "zawieniêtych" przek±tnych s±
tak¿e równe).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

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
%dir %{perl_vendorlib}/Math/MagicSquare
%{perl_vendorlib}/Math/MagicSquare/Generator.pm
%{_mandir}/man3/*
