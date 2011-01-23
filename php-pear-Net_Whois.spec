%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Whois
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - PEAR::Net_Whois class
Summary(pl.UTF-8):	%{_pearname} - klasa PEAR::Net_Whois
Name:		php-pear-%{_pearname}
Version:	1.0.4
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a726e55297b169fef9c264228916276b
URL:		http://pear.php.net/package/Net_Whois/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Net_Socket
Obsoletes:	php-pear-Net_Whois-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::Net_Whois looks up records in the databases maintained by
several Network Information Centers (NICs).

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa PEAR::Net_Whois przeszukuje rekordy w bazach danych zarządzanych
przez różne Network Information Centers (NICs).

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
