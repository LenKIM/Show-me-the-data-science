```
login as: root
root@192.168.56.101's password:
Last login: Thu Oct 25 15:19:49 2018 from gateway
[root@sever01 ~]# cd /root
[root@sever01 ~]#
[root@sever01 ~]# wget https://archive.cloudera.com/cm5/installer/latest/clouder                                                                                               a-manager-installer.bin
-bash: wget: command not found
[root@sever01 ~]# wget
-bash: wget: command not found
[root@sever01 ~]# yum install wget
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirror.kakao.com
 * extras: mirror.kakao.com
 * updates: mirror.kakao.com
base                                                     | 3.6 kB     00:00
extras                                                   | 3.4 kB     00:00
updates                                                  | 3.4 kB     00:00
updates/7/x86_64/primary_db                                | 6.0 MB   00:00
Resolving Dependencies
--> Running transaction check
---> Package wget.x86_64 0:1.14-15.el7_4.1 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package        Arch             Version                   Repository      Size
================================================================================
Installing:
 wget           x86_64           1.14-15.el7_4.1           base           547 k

Transaction Summary
================================================================================
Install  1 Package

Total download size: 547 k
Installed size: 2.0 M
Is this ok [y/d/N]: y
Downloading packages:
wget-1.14-15.el7_4.1.x86_64.rpm                            | 547 kB   00:00
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : wget-1.14-15.el7_4.1.x86_64                                  1/1
  Verifying  : wget-1.14-15.el7_4.1.x86_64                                  1/1

Installed:
  wget.x86_64 0:1.14-15.el7_4.1

Complete!
[root@sever01 ~]# wget https://archive.cloudera.com/cm5/installer/latest/clouder                                                                                               a-manager-installer.bin
--2018-10-25 15:24:58--  https://archive.cloudera.com/cm5/installer/latest/cloud                                                                                               era-manager-installer.bin
Resolving archive.cloudera.com (archive.cloudera.com)... 151.101.112.167
Connecting to archive.cloudera.com (archive.cloudera.com)|151.101.112.167|:443..                                                                                               . connected.
HTTP request sent, awaiting response... 200 OK
Length: 521199 (509K) [application/octet-stream]
Saving to: ‘cloudera-manager-installer.bin’

100%[======================================>] 521,199      322KB/s   in 1.6s

2018-10-25 15:25:01 (322 KB/s) - ‘cloudera-manager-installer.bin’ saved [521199/                                                                                               521199]

[root@sever01 ~]# vi /root/cloudera-manager-installer.bin
anaconda-ks.cfg                 .bashrc
.bash_history                   cloudera-manager-installer.bin
.bash_logout                    .cshrc
.bash_profile                   .tcshrc
[root@sever01 ~]# rm -rf cloudera-manager-installer.bin
[root@sever01 ~]# wget http://archive.cloudera.com/cm5/redhat/6/x86_64/cm/cloude                                                                                               ra-manager.repo
--2018-10-25 15:26:42--  http://archive.cloudera.com/cm5/redhat/6/x86_64/cm/clou                                                                                               dera-manager.repo
Resolving archive.cloudera.com (archive.cloudera.com)... 151.101.112.167
Connecting to archive.cloudera.com (archive.cloudera.com)|151.101.112.167|:80...                                                                                                connected.
HTTP request sent, awaiting response... 200 OK
Length: 290 [binary/octet-stream]
Saving to: ‘cloudera-manager.repo’

100%[======================================>] 290         --.-K/s   in 0s

2018-10-25 15:26:43 (31.2 MB/s) - ‘cloudera-manager.repo’ saved [290/290]

[root@sever01 ~]# vi /root/cloudera-manager.repo
[root@sever01 ~]# mv /root/cloudera-manager.repo /etc/yum.repos.d/
[root@sever01 ~]# yum install oracle-j2sdk1.7
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirror.navercorp.com
 * extras: mirror.navercorp.com
 * updates: mirror.navercorp.com
cloudera-manager                                         |  951 B     00:00
cloudera-manager/primary                                   | 4.3 kB   00:01
cloudera-manager                                                            7/7
Resolving Dependencies
--> Running transaction check
---> Package oracle-j2sdk1.7.x86_64 0:1.7.0+update67-1 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package             Arch       Version              Repository            Size
================================================================================
Installing:
 oracle-j2sdk1.7     x86_64     1.7.0+update67-1     cloudera-manager     135 M

Transaction Summary
================================================================================
Install  1 Package

Total download size: 135 M
Installed size: 279 M
Is this ok [y/d/N]: y
Downloading packages:
warning: /var/cache/yum/x86_64/7/cloudera-manager/packages/oracle-j2sdk1.7-1.7.0+update67-1.x86_64.rpm: Header V4 DSA/SHA1 Signature, key ID e8f86acd: NOKEY5 MB  00:00:00 ETA
Public key for oracle-j2sdk1.7-1.7.0+update67-1.x86_64.rpm is not installed
oracle-j2sdk1.7-1.7.0+update67-1.x86_64.rpm                                                                                                             | 135 MB  00:01:05
Retrieving key from https://archive.cloudera.com/cm5/redhat/6/x86_64/cm/RPM-GPG-KEY-cloudera
Importing GPG key 0xE8F86ACD:
 Userid     : "Yum Maintainer <webmaster@cloudera.com>"
 Fingerprint: 5f14 d39e f068 1aca 6f04 4a43 f90c 0d8f e8f8 6acd
 From       : https://archive.cloudera.com/cm5/redhat/6/x86_64/cm/RPM-GPG-KEY-cloudera
Is this ok [y/N]: y
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : oracle-j2sdk1.7-1.7.0+update67-1.x86_64                                                                                                                     1/1
  Verifying  : oracle-j2sdk1.7-1.7.0+update67-1.x86_64                                                                                                                     1/1

Installed:
  oracle-j2sdk1.7.x86_64 0:1.7.0+update67-1

Complete!
[root@sever01 ~]# yum install cloudera-manger-deamons cloudera-manager-server
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: centos.mirror.cdnetworks.com
 * extras: centos.mirror.cdnetworks.com
 * updates: centos.mirror.cdnetworks.com
No package cloudera-manger-deamons available.
Resolving Dependencies
--> Running transaction check
---> Package cloudera-manager-server.x86_64 0:5.9.0-1.cm590.p0.249.el6 will be installed
--> Processing Dependency: cloudera-manager-daemons = 5.9.0 for package: cloudera-manager-server-5.9.0-1.cm590.p0.249.el6.x86_64
--> Running transaction check
---> Package cloudera-manager-daemons.x86_64 0:5.9.0-1.cm590.p0.249.el6 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

===============================================================================================================================================================================
 Package                                         Arch                          Version                                           Repository                               Size
===============================================================================================================================================================================
Installing:
 cloudera-manager-server                         x86_64                        5.9.0-1.cm590.p0.249.el6                          cloudera-manager                        8.3 k
Installing for dependencies:
 cloudera-manager-daemons                        x86_64                        5.9.0-1.cm590.p0.249.el6                          cloudera-manager                        528 M

Transaction Summary
===============================================================================================================================================================================
Install  1 Package (+1 Dependent package)

Total download size: 528 M
Installed size: 679 M
Is this ok [y/d/N]: y
Downloading packages:
(1/2): cloudera-manager-server-5.9.0-1.cm590.p0.249.el6.x86_64.rpm                                                                                      | 8.3 kB  00:00:01
(2/2): cloudera-manager-daemons-5.9.0-1.cm590.p0.249.el6.x86_64.rpm                                                                                     | 528 MB  00:03:53
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                                          2.3 MB/s | 528 MB  00:03:53
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : cloudera-manager-daemons-5.9.0-1.cm590.p0.249.el6.x86_64                                                                                                    1/2
  Installing : cloudera-manager-server-5.9.0-1.cm590.p0.249.el6.x86_64                                                                                                     2/2
  Verifying  : cloudera-manager-server-5.9.0-1.cm590.p0.249.el6.x86_64                                                                                                     1/2
  Verifying  : cloudera-manager-daemons-5.9.0-1.cm590.p0.249.el6.x86_64                                                                                                    2/2

Installed:
  cloudera-manager-server.x86_64 0:5.9.0-1.cm590.p0.249.el6

Dependency Installed:
  cloudera-manager-daemons.x86_64 0:5.9.0-1.cm590.p0.249.el6

Complete!
[root@sever01 ~]# yum install cloudera-manager-server-db-2
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: centos.mirror.cdnetworks.com
 * extras: centos.mirror.cdnetworks.com
 * updates: centos.mirror.cdnetworks.com
Resolving Dependencies
--> Running transaction check
---> Package cloudera-manager-server-db-2.x86_64 0:5.9.0-1.cm590.p0.249.el6 will be installed
--> Processing Dependency: postgresql-server >= 8.4 for package: cloudera-manager-server-db-2-5.9.0-1.cm590.p0.249.el6.x86_64
--> Running transaction check
---> Package postgresql-server.x86_64 0:9.2.24-1.el7_5 will be installed
--> Processing Dependency: postgresql-libs(x86-64) = 9.2.24-1.el7_5 for package: postgresql-server-9.2.24-1.el7_5.x86_64
--> Processing Dependency: postgresql(x86-64) = 9.2.24-1.el7_5 for package: postgresql-server-9.2.24-1.el7_5.x86_64
--> Processing Dependency: libpq.so.5()(64bit) for package: postgresql-server-9.2.24-1.el7_5.x86_64
--> Running transaction check
---> Package postgresql.x86_64 0:9.2.24-1.el7_5 will be installed
---> Package postgresql-libs.x86_64 0:9.2.24-1.el7_5 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

===============================================================================================================================================================================
 Package                                            Arch                         Version                                          Repository                              Size
===============================================================================================================================================================================
Installing:
 cloudera-manager-server-db-2                       x86_64                       5.9.0-1.cm590.p0.249.el6                         cloudera-manager                        10 k
Installing for dependencies:
 postgresql                                         x86_64                       9.2.24-1.el7_5                                   updates                                3.0 M
 postgresql-libs                                    x86_64                       9.2.24-1.el7_5                                   updates                                234 k
 postgresql-server                                  x86_64                       9.2.24-1.el7_5                                   updates                                3.8 M

Transaction Summary
===============================================================================================================================================================================
Install  1 Package (+3 Dependent packages)

Total download size: 7.1 M
Installed size: 33 M
Is this ok [y/d/N]: y
Downloading packages:
(1/4): postgresql-libs-9.2.24-1.el7_5.x86_64.rpm                                                                                                        | 234 kB  00:00:00
(2/4): postgresql-9.2.24-1.el7_5.x86_64.rpm                                                                                                             | 3.0 MB  00:00:00
(3/4): postgresql-server-9.2.24-1.el7_5.x86_64.rpm                                                                                                      | 3.8 MB  00:00:00
(4/4): cloudera-manager-server-db-2-5.9.0-1.cm590.p0.249.el6.x86_64.rpm                                                                                 |  10 kB  00:00:01
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                                          4.9 MB/s | 7.1 MB  00:00:01
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : postgresql-libs-9.2.24-1.el7_5.x86_64                                                                                                                       1/4
  Installing : postgresql-9.2.24-1.el7_5.x86_64                                                                                                                            2/4
  Installing : postgresql-server-9.2.24-1.el7_5.x86_64                                                                                                                     3/4
  Installing : cloudera-manager-server-db-2-5.9.0-1.cm590.p0.249.el6.x86_64                                                                                                4/4
  Verifying  : postgresql-server-9.2.24-1.el7_5.x86_64                                                                                                                     1/4
  Verifying  : postgresql-libs-9.2.24-1.el7_5.x86_64                                                                                                                       2/4
  Verifying  : cloudera-manager-server-db-2-5.9.0-1.cm590.p0.249.el6.x86_64                                                                                                3/4
  Verifying  : postgresql-9.2.24-1.el7_5.x86_64                                                                                                                            4/4

Installed:
  cloudera-manager-server-db-2.x86_64 0:5.9.0-1.cm590.p0.249.el6

Dependency Installed:
  postgresql.x86_64 0:9.2.24-1.el7_5                    postgresql-libs.x86_64 0:9.2.24-1.el7_5                    postgresql-server.x86_64 0:9.2.24-1.el7_5

Complete!
[root@sever01 ~]#

```

