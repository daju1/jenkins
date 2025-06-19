# Local Git repo creation

```bash
    CI_CD/gitserver$ mkdir .ssh && chmod 700 .ssh
    CI_CD/gitserver$ touch .ssh/authorized_keys && chmod 600 .ssh/authorized_keys
    CI_CD/gitserver$ cat ~/.ssh/id_rsa.pub >> .ssh/authorized_keys 
    CI_CD/gitserver$ mkdir project.git
    CI_CD/gitserver$ cd project.git
    CI_CD/gitserver/project.git$ git init --bare
    Initialized empty Git repository in CI_CD/gitserver/project.git/
```

после апдейта репозитория можно остановить docker composer с помощью Ctrl+C в терминале где он запущен, затем 

```bash
    docker compose build
    docker compose up
```

ну а после того как поднимутся все сервисы нужно запустить пайтон скрипт

```bash
    jenkins/docker$ ./exec_ssh-keyscan.py
```

# jenkins
```bash
    cd jenkins/docker

    jenkins/docker$ docker compose build
    jenkins/docker$ docker compose up
    jenkins/docker$ ./exec_ssh-keyscan.py 
    jenkins_agent IP is 172.21.0.6
    # Host 172.21.0.6 found: line 28
    # Host 172.21.0.6 found: line 29
    # Host 172.21.0.6 found: line 30
    /var/jenkins_home/.ssh/known_hosts updated.
    Original contents retained as /var/jenkins_home/.ssh/known_hosts.old
    known_hosts  known_hosts.old
    .ssh/known_hosts
    ['docker', 'exec', '-it', '--workdir=/var/jenkins_home', 'jenkins_sandbox', '/scan-host-key.sh', '172.21.0.6']
    /scan-host-key.sh: 5: cannot create /root/.ssh/known_hosts: Directory nonexistent
    # 172.21.0.6:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u5
    # 172.21.0.6:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u5
    # 172.21.0.6:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u5
    # 172.21.0.6:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u5
    # 172.21.0.6:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u5

    jenkins_agent_android IP is 172.21.0.9
    # Host 172.21.0.9 found: line 28
    # Host 172.21.0.9 found: line 29
    # Host 172.21.0.9 found: line 30
    /var/jenkins_home/.ssh/known_hosts updated.
    Original contents retained as /var/jenkins_home/.ssh/known_hosts.old
    known_hosts  known_hosts.old
    .ssh/known_hosts
    ['docker', 'exec', '-it', '--workdir=/var/jenkins_home', 'jenkins_sandbox', '/scan-host-key.sh', '172.21.0.9']
    /scan-host-key.sh: 5: cannot create /root/.ssh/known_hosts: Directory nonexistent
    # 172.21.0.9:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u5
    # 172.21.0.9:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u5
    # 172.21.0.9:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u5
    # 172.21.0.9:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u5
    # 172.21.0.9:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u5

    git_server_rockstorm IP is 172.21.0.4
    # Host 172.21.0.4 found: line 28
    # Host 172.21.0.4 found: line 29
    # Host 172.21.0.4 found: line 30
    /var/jenkins_home/.ssh/known_hosts updated.
    Original contents retained as /var/jenkins_home/.ssh/known_hosts.old
    Cannot stat /root//.ssh/known_hosts: No such file or directory
    known_hosts  known_hosts.old
    .ssh/known_hosts
    ['docker', 'exec', '-it', '--workdir=/var/jenkins_home', 'jenkins_sandbox', '/scan-host-key.sh', '172.21.0.4']
    /scan-host-key.sh: 5: cannot create /root/.ssh/known_hosts: Directory nonexistent
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0

    ls: cannot access '.ssh': No such file or directory
    ls: cannot access '.ssh/known_hosts': No such file or directory
    ['docker', 'exec', '-it', '--workdir=/root/', 'jenkins_sandbox', '/scan-host-key.sh', '172.21.0.4']
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0

    # Host 172.21.0.4 found: line 1
    # Host 172.21.0.4 found: line 2
    # Host 172.21.0.4 found: line 3
    /home/jenkins/.ssh/known_hosts updated.
    Original contents retained as /home/jenkins/.ssh/known_hosts.old
    authorized_keys  known_hosts  known_hosts.old
    .ssh/known_hosts
    ['docker', 'exec', '-it', '--workdir=/home/jenkins', 'jenkins_agent', '/scan-host-key.sh', '172.21.0.4']
    /scan-host-key.sh: 5: cannot create /root/.ssh/known_hosts: Directory nonexistent
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0

    ls: cannot access '.ssh': No such file or directory
    ls: cannot access '.ssh/known_hosts': No such file or directory
    ['docker', 'exec', '-it', '--workdir=/root/', 'jenkins_agent', '/scan-host-key.sh', '172.21.0.4']
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0

    # Host 172.21.0.4 found: line 1
    # Host 172.21.0.4 found: line 2
    # Host 172.21.0.4 found: line 3
    /home/jenkins/.ssh/known_hosts updated.
    Original contents retained as /home/jenkins/.ssh/known_hosts.old
    authorized_keys  known_hosts  known_hosts.old
    .ssh/known_hosts
    ['docker', 'exec', '-it', '--workdir=/home/jenkins', 'jenkins_agent_android', '/scan-host-key.sh', '172.21.0.4']
    /scan-host-key.sh: 5: cannot create /root/.ssh/known_hosts: Directory nonexistent
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0

    ls: cannot access '.ssh': No such file or directory
    ls: cannot access '.ssh/known_hosts': No such file or directory
    ['docker', 'exec', '-it', '--workdir=/root/', 'jenkins_agent_android', '/scan-host-key.sh', '172.21.0.4']
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0
    # 172.21.0.4:22 SSH-2.0-OpenSSH_10.0

```


из логов пайтон скрипта нужно узнать айпишники ssh-agent, ssh-agent-android и гитсервера

```bash
    jenkins_agent IP is 172.21.0.9
    jenkins_agent_android IP is 172.21.0.5
    git_server_rockstorm IP is 172.21.0.8
```

Эти айпишники нужно использовать при конфигурации нодов и гитсервера


functions inside docker/exec_ssh-keyscan.py


Now we create new pipeline using local git repo as source



New job APK_Jenkinsfiles


functions inside docker/exec_ssh-keyscan.py

для аутентификации в папке

docker/ssh-agent

нужно сгенерировать или скопировать в эту папку ключи

```bash
    jenkins$ ls docker/ssh-agent/.ssh/
    id_rsa id_rsa.pub
```
у меня эти ключи сгенерированы для пользователя jenkins
