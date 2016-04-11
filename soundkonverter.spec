Summary:	An audio file converter, CD ripper and replay gain tool
Name:		soundkonverter
Version:	2.2.0
Release:	1
License:	GPLv2+
Group:		Sound
Url:		https://github.com/HessiJames/soundkonverter/
Source0:	https://github.com/HessiJames/soundkonverter/archive/v%{version}.tar.gz
Source1:	soundkonverter.desktop
# !!! Make sure to update this patch on EVERY version update !!!_
#Patch0:		soundkonverter-2.0.4-soname.patch
BuildRequires:	cmake
BuildRequires:	cdda-devel
BuildRequires:	libkcddb-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(taglib) >= 1.4
Requires:	cdparanoia
Requires:	flac
Requires:	fluidsynth
Requires:	ffmpeg
Requires:	opus-tools
Requires:	mplayer
Requires:	mppenc
Requires:	speex
Requires:	TiMidity++
Requires:	twolame
Requires:	vorbis-tools
Requires:	wavpack
# suggested requires on mrb to be imported in restricted eventually
Suggests:	aacgain
Suggests:	aften
Suggests:	faac
Suggests:	faad2
Suggests:	flac123
Suggests:	lame
Suggests:	mac
Suggests:	mp3gain
Suggests:	mppdec
Suggests:	neroaac
Suggests:	shorten
Suggests:	ttaenc
Suggests:	vorbisgain
# Wrong library package
Conflicts:	%{_lib}soundkonverter < 2.0.4

%description
An audio file converter, CD ripper and replay gain tool GUI for various
back-ends.

%files -f %{name}.lang
%{_kde_bindir}/%{name}
%{_kde_appsdir}/%{name}
%{_kde_appsdir}/solid/actions/%{name}-*
%{_datadir}/appdata/soundkonverter.appdata.xml
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_iconsdir}/hicolor/*/apps/*.png
%{_kde_services}/%{name}_*
%{_kde_servicetypes}/%{name}_*
# codecs, filters etc
%{_kde_libdir}/kde4/soundkonverter_*.so

#----------------------------------------------------------------------------

%define major 0
%define libsoundkonvertercore %mklibname soundkonvertercore %{major}

%package -n %{libsoundkonvertercore}
Summary:	Library for %{name}
Group:		System/Libraries
Obsoletes:	%{_lib}soundkonverter < 2.0.4

%description -n %{libsoundkonvertercore}
This package provides the library for %{name}.

%files -n %{libsoundkonvertercore}
%{_kde_libdir}/libsoundkonvertercore.so.%{major}*

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches
# fix debug linting more then 100 w
find . -type f -exec chmod -x {} \;

%build
pushd src
%cmake_kde4
%make
popd

%install
pushd src
%makeinstall_std -C build

# replace desktop file
rm -f %{buildroot}%{_kde_applicationsdir}/%{name}.desktop
install -m 644 %{SOURCE1} %{buildroot}%{_kde_applicationsdir}/%{name}.desktop

# We don't need it as there are no headers anyway
rm -f %{buildroot}%{_kde_libdir}/libsoundkonvertercore.so
popd

%find_lang %{name}

