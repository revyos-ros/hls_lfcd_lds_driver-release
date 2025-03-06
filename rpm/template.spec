%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-hls-lfcd-lds-driver
Version:        2.1.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS hls_lfcd_lds_driver package

License:        BSD
URL:            http://wiki.ros.org/hls_lfcd_lds_driver
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-jazzy-rclcpp
Requires:       ros-jazzy-sensor-msgs
Requires:       ros-jazzy-ros-workspace
BuildRequires:  boost-devel
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-rclcpp
BuildRequires:  ros-jazzy-sensor-msgs
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
ROS package for LDS-01(HLS-LFCD2). The LDS (Laser Distance Sensor) is a sensor
sending the data to Host for the simultaneous localization and mapping (SLAM).
Simultaneously the detecting obstacle data can also be sent to Host.
HLDS(Hitachi-LG Data Storage) is developing the technology for the moving
platform sensor such as Robot Vacuum Cleaners, Home Robot, Robotics Lawn Mower
Sensor, etc.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Thu Mar 06 2025 Pyo <pyo@robotis.com> - 2.1.0-1
- Autogenerated by Bloom

* Fri Jun 21 2024 Will Son <willson@robotis.com> - 2.0.4-7
- Autogenerated by Bloom

* Thu Apr 18 2024 Will Son <willson@robotis.com> - 2.0.4-6
- Autogenerated by Bloom

* Wed Mar 06 2024 Will Son <willson@robotis.com> - 2.0.4-5
- Autogenerated by Bloom

