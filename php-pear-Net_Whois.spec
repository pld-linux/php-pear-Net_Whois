%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Whois
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - PEAR::Net_Whois class
Summary(pl):	%{_pearname} - klasa PEAR::Net_Whois
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	cc172a0afdf4c630bd5a9128e35ce935
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/Net_Whois/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Net_Socket
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::Net_Whois looks up records in the databases maintained by
several Network Information Centers (NICs).

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa PEAR::Net_Whois przeszukuje rekordy w bazach danych zarz±dzanych
przez ró¿ne Network Information Centers (NICs).

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
