Name:           gcompris-qt
Version:        3.0
Release:        1
Summary:        "J'ai compris" / I Have Understood, the new QT based version
License:        GPLv3+
Group:          Education
Url:            http://gcompris.net
Source0:        http://gcompris.net/download/qt/src/%{name}-%{version}.tar.xz
# Built with package-data.sh
Source1:        gcompris-qt-voices.tar.xz
Source10:	package-data.sh
# Packaged after running "make getSvnTranslations" inside
# the source tree
#Source2:	gcompris-translations.tar.xz
BuildRequires:  cmake(ECM)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(Qt5QuickParticles)
BuildRequires:  pkgconfig(Qt5QmlWorkerScript)
BuildRequires:  pkgconfig(Qt5Charts)
BuildRequires:  pkgconfig(Qt5Core) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Xml) >= 5.2.0
BuildRequires:  pkgconfig(Qt5XmlPatterns) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Multimedia) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Network) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Script) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Svg) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.2.0
BuildRequires:  pkgconfig(Qt5PrintSupport) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Quick) >= 5.2.0
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5OpenGL) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Sensors) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:	pkgconfig(libssl)
#BuildRequires:  pkgconfig(box2d)
#BuildRequires:  qml-box2d
BuildRequires:  libxml2-utils
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl

%rename gcompris
Requires:       %{name}-activities = %{version}
Requires:       %{name}-translations = %{version}
Requires:       %{name}-voices = %{version}


%description
GCompris-Qt is a high quality educational software suite comprising
of numerous activities for children aged 2 to 10. Some of the
activities are game orientated, but nonetheless still educational.

Currently GCompris offers in excess of 100 activities and more
are being developed. GCompris is free software, that means that
you can use it as you wish, adapt it to your own needs, improve
 it, and, most importantly, share it with everyone.

This version is a full rewrite of GCompris using the QtQuick
technology. It is developed within the KDE community and is
part of the GNU Project.
For such reason, it will only available for recent platforms.

Goal:
There are many simple activities dedicated to children on any
platforms, desktops, web and tablets. When they exist, they are
hard to find and request the teacher or parent to manage a lot
of independent small tools.

GCompris is an educational suite of activities all accessible
from a single unified user interface.

How:
GCompris is designed in a way that it is easy to add new activities
to it. The activity is free to implement the game scheme it wants.
The status bar is a common facility provided to the activities.

GCompris provides some tools to let teacher/educator to easily
add activities to GCompris.

This package contains the main binary. We recommend you to install
%{name}-activities and %{name}-translations.

A %{name}-voices is also proposed for a full offline experience.

%package activities
Group:          Education
Summary:        Activities files
Requires:       %{name} = %{version}

%description activities
This package contains the bundle of %{name} activities.
More than 100 activities are available.
You can addd the translations and voices packages to your system,
to benefit a full offline experience.


%package translations
Group:          Education
Summary:        Translations files
Requires:       %{name} = %{version}

%description translations
This package contains the bundle of %{name} translations.
More than 30 languages are available, and allow you to run
%{name} in differents languages, and play activities.


#The voices packages
%package voices
Summary:        Voices pack for %{name}
Group:          Education
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}

%description voices
This is voices packages for %{name}. This a full bundle useful if
you don't want to use the automatic online feature.

This allow you to play %{name} activities in differents languages.


%prep
%autosetup -p1


%build
%cmake_qt5 \
      -Wno-dev \
      -DCMAKE_SKIP_RPATH=ON \
      -DQML_BOX2D_MODULE=disabled

%make_build
# Build translastions too.
%make_build BuildTranslations

%install
%make_install -C build

cd %{buildroot}%{_kde5_datadir}/%{name}
tar -xJf %{S:1}

%files
%doc README.md
#doc #{_kde5_docdir}/HTML/en/%{name}/
%{_kde5_bindir}/%{name}
%{_kde5_applicationsdir}/org.kde.gcompris.desktop
%{_kde5_datadir}/metainfo/org.kde.gcompris.appdata.xml
%{_kde5_iconsdir}/hicolor/256x256/apps/gcompris-qt.png
%{_kde5_iconsdir}/hicolor/scalable/apps/gcompris-qt.svg
%{_kde5_datadir}/%{name}/data2/words/

%files activities
%doc README.md
#Activities
%dir %{_kde5_datadir}/%{name}
%dir %{_kde5_datadir}/%{name}/rcc
%{_kde5_datadir}/%{name}/rcc/*.rcc

#Translations goes to their own packages
%exclude %{_kde5_datadir}/%{name}/translations

%files translations
%doc README.md
%dir %{_kde5_datadir}/%{name}/translations
%{_kde5_datadir}/%{name}/translations/*.qm

%files voices
%doc README.md
%dir %{_kde5_datadir}/%{name}/
%dir %{_kde5_datadir}/%{name}/data2
%{_kde5_datadir}/%{name}/data2/voices-ogg/
%{_kde5_datadir}/%{name}/data2/backgroundMusic/
