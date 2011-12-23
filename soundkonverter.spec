Name:           soundkonverter
Version:        1.2.1
Release:        %mkrel 1
License:        GPLv2
Group:          Sound
Summary:        An audio file converter, CD ripper and Replay Gain tool
URL:            http://kde-apps.org/content/show.php?content=29024
Source0:         %{name}-%{version}.tar.gz
 
BuildRequires:  kdelibs4-devel
BuildRequires:  taglib-devel >= 1.4
BuildRequires:  kdemultimedia4-devel
BuildRequires:  cdda-devel
 
Requires:       flac
Requires:       cdparanoia
Requires:       speex
Requires:       fluidsynth
Requires:       vorbis-tools
Requires:       wavpack
Requires:       vorbisgain
Suggests:       ffmpeg
Suggests:       mp3gain
 
%description
SoundKonverter is a frontend to various audio converters.
 
The key features are:
 Audio file conversion
 Replay Gain calculation
 CD ripping
 
It is extendable by plug-ins and supports many backends.
soundKonverter supports reading and writing tags for many formats, so the tags
are preserved when converting files.
 
%prep
%setup -q
 
%build
%cmake_kde4
%make
 
%install
pushd build
%makeinstall_std
popd
 
%find_lang %{name}
 
%clean
rm -rf %{buildroot}
 
%files -f %{name}.lang
%defattr(-,root,root,-)
%doc CHANGELOG README
%dir %{_kde_appsdir}/solid
%dir %{_kde_appsdir}/solid/actions
%dir %{_kde_appsdir}/soundkonverter
%{_kde_appsdir}/soundkonverter/*
%{_kde_bindir}/soundkonverter
%{_kde_libdir}/soundkonverter/libsoundkonvertercore.so
%{_kde_services}/soundkonverter_*
%{_kde_libdir}/kde4/soundkonverter_*.so
%{_kde_applicationsdir}/soundkonverter.desktop
%{_kde_iconsdir}/*/*x*/apps/*.png
%{_kde_servicetypes}/soundkonverter_*.desktop
%{_kde_appsdir}/solid/actions/soundkonverter-rip-audiocd.desktop
