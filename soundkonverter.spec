%define name	soundkonverter
%define	version	2.0.2
%define release	1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	An audio file converter, CD ripper
Group:		Sound
License:	GPLv2
URL:		https://gitorious.org/soundkonverter/soundkonverter
Source0:	https://gitorious.org/soundkonverter/soundkonverter/blobs/raw/180e777aa3d91456ac386868a1e324ca28649e2e/release/soundkonverter-%{version}.tar.gz
Source1:	soundkonverter.desktop
BuildRequires:  cdda-devel 
BuildRequires:  libkcddb-devel
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(taglib) >= 1.4 
BuildRequires:  kdelibs4-devel
#BuildRequires:  kdemultimedia4-devel 
BuildRequires:  cmake 
BuildRequires:  gcc 
BuildRequires:  gcc-c++ 
BuildRequires:  automoc4
Requires:       cdparanoia
Requires:       flac
Requires:       speex
Requires:       TiMidity++
Requires:       vorbis-tools
Requires:       wavpack
Requires:       mplayer
Requires:       faac
Requires:       faad2
Requires:       ffmpeg
Requires:       lame
Requires:       mac
Requires:       mppenc 
Requires:       fluidsynth
Requires:       twolame
# suggested requires on mrb to be imported in restricted eventually 
Suggests:       shorten
Suggests:       vorbisgain
Suggests:       mppdec
Suggests:       aacgain
Suggests:       neroaac
Suggests:       flac123
Suggests:       aften ttaenc
Suggests:       mp3gain

%description
An audio file converter, CD ripper and
replay gain tool GUI for various backends

%prep
%setup -q

%build
%cmake_kde4 
%make

%install
%makeinstall_std -C build DESTDIR=%{buildroot} 

rm -rf %{buildroot}%{_datadir}/applications/kde4/soundkonverter.desktop

install -p -m 755  %{SOURCE1} %{buildroot}%{_datadir}/applications/kde4/soundkonverter.desktop


%find_lang %{name}


%files -f %{name}.lang
%doc CHANGELOG README
%dir %{_datadir}/apps/solid
%dir %{_datadir}/apps/solid/actions
%dir %{_datadir}/apps/soundkonverter
%{_datadir}/apps/soundkonverter/*
%{_bindir}/soundkonverter
%{_libdir}/libsoundkonvertercore.so
%{_datadir}/kde4/services/soundkonverter_*
%{_libdir}/kde4/soundkonverter_*
%{_datadir}/applications/kde4/soundkonverter.desktop
%{_datadir}/icons/hicolor/16x16/apps/*.png                                                                                    
%{_datadir}/icons/hicolor/22x22/apps/*.png                                                                                    
%{_datadir}/icons/hicolor/32x32/apps/*.png                                                                                    
%{_datadir}/icons/hicolor/48x48/apps/*.png                                                                                    
%{_datadir}/icons/hicolor/64x64/apps/*.png  
%{_datadir}/kde4/servicetypes/soundkonverter_codecplugin.desktop
%{_datadir}/kde4/servicetypes/soundkonverter_replaygainplugin.desktop
%{_datadir}/kde4/servicetypes/soundkonverter_ripperplugin.desktop
%{_datadir}/kde4/servicetypes/soundkonverter_filterplugin.desktop	
%{_datadir}/apps/solid/actions/soundkonverter-rip-audiocd.desktop
