%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       Whois
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - PEAR::Net_Whois class
Summary(pl):	%{_pearname} - klasa PEAR::Net_Whois
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::Net_Whois looks up records in the databases maintained by
several Network Information Centers (NICs).

This class has in PEAR status: %{_status}.

%description -l pl
Klasa PEAR::Net_Whois przeszukuje rekordy w bazach danych zarz±dzanych
przez ró¿ne Network Information Centers (NICs).

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/%{_subclass}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
