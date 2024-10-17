%define version 0.0.4
%define release %mkrel 8

Name:		gnome-u2ps
Summary:	UTF-8 text to a2ps style Postscript converter
Version:	%{version}
Release:	%{release}
License:	GPL
URL:		https://bonobo.gnome.gr.jp/~nakai/u2ps/
Group:		Text tools
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		http://bonobo.gnome.gr.jp/~nakai/u2ps/%{name}-%{version}.tar.bz2
BuildRequires:	fribidi-devel >= 0.10.4
BuildRequires:	libgnomeprint2-2-devel >= 2.5.4
BuildRequires:	libgnome2-devel
BuildRequires:	bzip2-devel
BuildRequires:	perl-XML-Parser

%description
u2ps is similar to a2ps, but with internationalization support in mind.
It includes feature such as:

* UTF-8 text conversion to PostScript
* Legacy codeset support
* Appropriate font guessing from current locale
* Arabic bidirectional text support with fribidi
* Legacy multi-byte codeset auto-detection of plain text
* Mail parse option --mail, similar to a2ps -=mail , but with MIME
  header decoding as well

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/*
