Summary:	An audio file converter, CD ripper and replay gain tool
Name:		soundkonverter
Version:	3.0.1
Release:	3
License:	GPLv2+
Group:		Sound
Url:		https://github.com/HessiJames/soundkonverter/
Source0:	https://github.com/HessiJames/soundkonverter/archive/v%{version}/%{name}-%{version}.tar.gz
# Support for Taglib 2
Patch0:  https://github.com/dfaust/soundkonverter/commit/dd52d33046cf740415f8507a3ffd5b37dffc5a2c.patch
BuildRequires:	cmake
BuildRequires:	cdda-devel
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Cddb)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(Phonon4Qt5)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(KF5WidgetsAddons)
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
%{_kde5_bindir}/%{name}
%{_kde5_datadir}/solid/actions/%{name}-*
%{_datadir}/appdata/soundkonverter.appdata.xml
%{_kde5_applicationsdir}/%{name}.desktop
%{_kde5_iconsdir}/hicolor/*/apps/*.png
%{_kde5_services}/%{name}_*
%{_kde5_servicetypes}/%{name}_*
# codecs, filters etc
%{_kde5_libdir}/qt5/plugins/soundkonverter_*.so
%{_libdir}/libsoundkonvertercore.so
%{_datadir}/%{name}
%{_datadir}/kxmlgui5/%{name}

#----------------------------------------------------------------------------

%prep
%autosetup -p1
# fix debug linting more then 100 w
find . -type f -exec chmod -x {} \;

%build
pushd src
%cmake_kde5
%ninja
popd

%install
pushd src
%ninja_install -C build

popd

%find_lang %{name}

