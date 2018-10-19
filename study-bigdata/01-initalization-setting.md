# config

OS는 cent OS

메모리 크기는 2048MB

하드디스크 크기는 20GB

**가상머신만들 때 필요한 설정은 다음과 같다.**

ios는 https://www.centos.org/download/

 지금 가상 하드 드라이브 만들기 / VDI / 동적 할당

---

각각의 가상머신에 설정해야 될 부분은?

1. Hostname

2. 정적 IP부여  
   $ vi /etc/sysconfig/network-scripts/ifcfg-eth0  

   ```
   DEVICE=eth0
   HWADDR= 5번 참조
   TYPE=Ethernet
   ONBOOT=yes
   BOOTPROTO=static
   IPADDR=192.168.56.101
   NETMASK=255.255.255.0
   GATEWAY=192.168.56.1
   NETWORK=192.168.56.0
   ```

   가상머신의 전원 자체를 종료후 재실행 한 뒤  
   root 로그인 후, 다음과 같이 입력한다.  
   $ service network restart  
   만약 어떠한 오류가 없다면 고정IP 설정이 잘마친것 확인 방법은   
   $ ifconfig eth0

3. Kdump 해제

4. GUI 모드 해제  
   $ su root  
   $ Password: adminuser  
   $ vi /etc/inittab  

5. MAC 주소는 가상머신 설정 -> 네트워크 -> 어탭터2 -> 고급

6. SSH접속을 위한 패키지를 설정해야 한다.  

   ```tex
   $ yum install openssh*
   $ service sshd restart
   $ chkconfig sshd on
   $ reboot
   
   리부팅이 완료되면 다음 명령으로 네트워크 설정을 다시 한번 재시작한다.
   
   $ service network restart
   ```

   원도우는 putty를 통해 접속을 시도한다.

7.  위에까지 모두다 잘 된다면 마지막으로 가상머신의 호스트 정보를 수정한다.  

   > $ vi /etc/hosts

   모든 내용을 지운 후 다음과 같이 입력한다.

   ```
   127.0.0.1 localhost server01
   192.168.56.101 server01.hadoop.com server01
   192.168.56.102 server03.hadoop.com server02
   192.168.56.102 server03.hadoop.com server03
   ```

   > $ vi /etc/sysconfig/network

   ```
   NETWORKING=yes
   NETWORKING IPV6=no
   HOSTNAME=server01.hadoop.com
   ```

   이 후 다시한번 서비스를 재시작한다.

   > $ service network restart

   cf) 여기서 이슈가 하나 발생하는데, 호스트 네임을 변경해도 변경되지 않는 이슈, 이럴 때는  

   > $ vi /etc/hostname

   으로 들어가 이름을 수정한다.

8. 마지막으로 방화벽 및 기타 커널 매개변수 설정을 위해 아래의 명령을 하나씩 실행한다. 여기서 각각의 매개변수를 이해하는건 Homework로 놔두자.  

   ```
   $ vi /etc/selinux/config # config 파일에서 SELINUX를 "SELINUX=disabled"로 수정
   $ service iptables stop # iptables 중지 명령
   $ chkconfig iptables off # iptables 자동 시작 중지 명령
   $ chkconfig ip6tables off # ip6tables 자동 시작 중지 명령
   $ sysctl -w vm.swappiness=100 #vm swappiness 사용 제어 설정
   $ vi /etc/sysctl.conf # sysctl.conf 파일에서 "vm.swappiness=100" 설정을 추가
   $ vi /etc/rc.local # rc.local 파일에서 아래 명령어를 추가
   /bin/echo never > /sys/kernal/mm/transparent_hugepage/enabled
   $ vi /etc/security/limits.conf # limits.conf 파일에서 아래의 파일 디스크립터 설정을 추가
   root soft nofile 65536
   root hard nofile 65536
   * soft nofile 65536
   * hard nofile 65536
   root soft nproc 32768
   root hard nproc 32768
   * soft nproc 32768
   * hard nproc 32768
   
   $ reboot
   ```

9.  위 설정을 가상머신에서 복제.  
   `모든 네트워크 카드의 MAC주소 초기화` > `완전한 복제`  
   다음 복제된 가상머신에 들어가  
   $ vi /etc/sysconfig/network-scripts/ifcfg-eth0 에서 HWADDR과 IPADDR을 수정한다.  
   다음 호스트정보를 수정한다.  

   > $ vi /etc/hosts
   >
   > $ vi /etc/sysconfig/network

   다음 네트워크 설정 정보를 재시작하고 운영체제를 리부트한다.

   > $ service network restart
   >
   > $ reboot

10. 마지막으로 복제된 가상머신의 정적IP와 HOSTNAME을 확인한다.  

    > ifconfig eth0
    >
    > hostname

# 이슈

1. YUM 이 동작하지 않을 때

   ifconfig가 안되서 발생하는 문제임.

   http://skysoo1111.tistory.com/36

   https://zetawiki.com/wiki/CentOS_7_ifconfig_%EB%AA%85%EB%A0%B9%EC%96%B4_%EC%97%86%EC%9D%8C

2. username이 변하지 않는 이슈 발생