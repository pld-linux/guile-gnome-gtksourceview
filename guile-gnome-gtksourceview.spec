Summary:	Guile wrapper for GtkSourceView library
Summary(pl.UTF-8):	Wrapper Guile dla biblioteki GtkSourceView
Name:		guile-gnome-gtksourceview
Version:	1.8.0
Release:	0.1
License:	GPL v2+
Group:		Development/Languages/Scheme
Source0:	http://ftp.gnu.org/pub/gnu/guile-gnome/guile-gnome-gtksourceview/%{name}-%{version}.tar.gz
# Source0-md5:	f49df7fd463873fa736214b41e7e6b27
URL:		http://www.gnu.org/software/guile-gnome/
BuildRequires:	g-wrap-devel >= 1.9.7
BuildRequires:	gtksourceview-devel >= 1.8.0
BuildRequires:	guile-gnome-glib-devel
BuildRequires:	guile-gnome-gtk
BuildRequires:	guile-devel >= 5:1.6.4
BuildRequires:	pkgconfig >= 1:0.9.0
Requires:	g-wrap >= 1.9.7
Requires:	guile >= 5:1.6.4
Requires:	guile-gnome-gtk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
guile-gnome-gtksourceview is a Guile wrapper for GtkSourceView, a
TextBuffer/TextView-based source editing widget.

%description -l pl.UTF-8
guile-gnome-gtksourceview to wrapper Guile dla biblioteki
GtkSourceView - widgetu edycji źródeł opartego na obiektach
TextBuffer/TextView.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/guile-gnome-0/libgw-guile-gnome-*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc gtksourceview/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/guile-gnome-0/libgw-guile-gnome-gtksourceview.so*
# conflict with guile-gnome-platform
#%{_datadir}/guile-gnome-0/gnome/defs/gtksourceview.defs
#%{_datadir}/guile-gnome-0/gnome/defs/gtksourceview-types.defs
%{_datadir}/guile-gnome-0/gnome/gtksourceview.scm
%{_datadir}/guile-gnome-0/gnome/gw/gtksourceview.scm
%{_datadir}/guile-gnome-0/gnome/gw/gtksourceview-spec.scm
%{_datadir}/guile-gnome-0/gnome/overrides/gtksourceview.defs
