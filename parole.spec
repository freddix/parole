Summary:	Simple media player based on the GStreamer framework
Name:		parole
Version:	0.3.0.3
Release:	2
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://archive.xfce.org/src/apps/parole/0.3/%{name}-%{version}.tar.bz2
# Source0-md5:	d13ece4c5a4980a1aedfed8eb3c6172d
Patch0:		1201f19a53e87fbf99018eaef4bbe8d832f114c2.patch
URL:		http://www.xfce.org/projects/parole/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	gstreamer010-plugins-base-devel
BuildRequires:	gtk+-devel
BuildRequires:	intltool
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	pkg-config
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	hicolor-icon-theme
Requires:	gstreamer010-ffmpeg
Requires:	gstreamer010-plugins-bad
Requires:	gstreamer010-plugins-base
Requires:	gstreamer010-plugins-good
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parole is a modern simple media player based on the GStreamer
framework and written to fit well in the Xfce desktop.
Parole is designed with simplicity, speed and resource usage in mind.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-browser-plugin
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_includedir}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/parole-0/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database

%postun
%update_icon_cache hicolor
%update_desktop_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/parole
%dir %{_libdir}/parole-0
%attr(755,root,root) %{_libdir}/parole-0/*.so
%{_datadir}/parole
%{_desktopdir}/parole.desktop
%{_iconsdir}/hicolor/*/apps/parole.*

