# Local Git repo creation
для начала исходя из [следующего руководства](https://git-scm.com/book/en/v2/Git-on-the-Server-Setting-Up-the-Server) 

относительно выбранной рабочей папки например jenkins_work

```bash
    mkdir jenkins_work
    cd jenkins_work
```
я создал локальный гит сервер содержащий проект myproject.git с помощью следующего набора команд 

```bash
    mkdir -p gitserver/.ssh
    cd gitserver
    chmod 700 .ssh
    touch .ssh/authorized_keys && chmod 600 .ssh/authorized_keys
    cat ~/.ssh/id_rsa.pub >> .ssh/authorized_keys 
    mkdir myproject.git
    cd myproject.git
    git init --bare
```
    Initialized empty Git repository in gitserver/myproject.git/


Далее мы либо создаём локальный гит репозитрорий

```bash
    cd jenkins_work
    mkdir my_project
    cd my_project
    git init
```

либо в папке my_project с уже имеющимся локальным гит репозиторием создаём remote url который соответствует файловому пути к папке моего проекта в гитрепозитории

```bash
    git remote add origin jenkins_work/gitserver/myproject.git
```

или если локальный репозиторий уже имеет remote url тогда меняяем его

```bash
    git remote set-url origin jenkins_work/gitserver/myproject.git
```

проверяем

```bash
    git remote -v
```

origin	jenkins_work/gitserver/myproject.git (fetch)
origin	jenkins_work/gitserver/myproject.git (push)


Далее возвращаемся в рабочую папку и клонируем в нее текущий репозиторий

```bash
    cd jenkins_work
    git clone https://github.com/daju1/jenkins.git
```

таким обюразом мы имеем следующую структуру папок

```
jenkins_work$ ls -la
gitserver  jenkins  my_project
```

для аутентификации в папке

docker/ssh-agent

нужно сгенерировать

у меня эти ключи сгенерированы для пользователя jenkins

```bash
    cd jenkins_work/jenkins/docker/ssh-agent
```

```bash
    mkdir .ssh/
    ssh-keygen -f .ssh/id_rsa -C jenkins
```

или скопировать в эту папку уже имеющиеся ключи (по желанию)

```bash
    jenkins$ ls docker/ssh-agent/.ssh/
    id_rsa id_rsa.pub
```

Далее приступаем к билду и запуску докер контейнеров

для этого переходим в папку
```bash
    cd jenkins_work/jenkins/docker$
```

где выполняем следующие команды 

```bash
    docker compose build
    docker compose up
```

в случае ошибки связанной с настройкой сети удаляем контейнеры и сети докера 

```bash
    docker compose rm
    docker network prune
    docker compose up --force-recreate --remove-orphans
```

(возможно на этом этапе понадобится перезагрузка системы если сеть таки не подымется)

Теперь по адресу http://localhost:8082/

нам будут доступны следующие страницы

![screenshot 1](images/01.png)

![screenshot 2](images/02.png)

![screenshot 3](images/03.png)

![screenshot 4](images/04.png)

![screenshot 5](images/05.png)

![screenshot 6](images/06.png)

ну а после того как поднимутся все сервисы нужно запустить пайтон скрипт

```bash
    jenkins/docker$ ./exec_ssh-keyscan.py
```

```
    jenkins_agent IP is 172.18.0.3
    docker exec -it --workdir=/var/jenkins_home jenkins_sandbox
    # Host 172.18.0.3 found: line 52
    # Host 172.18.0.3 found: line 53
    # Host 172.18.0.3 found: line 54
    /var/jenkins_home/.ssh/known_hosts updated.
    Original contents retained as /var/jenkins_home/.ssh/known_hosts.old
    docker exec -it --workdir=/root/ jenkins_sandbox
    Cannot stat /root//.ssh/known_hosts: No such file or directory
    docker exec -it --workdir=/var/jenkins_home jenkins_sandbox
    known_hosts  known_hosts.old
    docker exec -it --workdir=/var/jenkins_home jenkins_sandbox
    .ssh/known_hosts
    ['docker', 'exec', '-it', '--workdir=/var/jenkins_home', 'jenkins_sandbox', '/scan-host-key.sh', '172.18.0.3', '/var/jenkins_home']
    # 172.18.0.3:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u6
    # 172.18.0.3:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u6
    # 172.18.0.3:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u6
    # 172.18.0.3:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u6
    # 172.18.0.3:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u6

    docker exec -it --workdir=/root/ jenkins_sandbox
    ls: cannot access '.ssh': No such file or directory
    docker exec -it --workdir=/root/ jenkins_sandbox
    docker exec -it --workdir=/root/ jenkins_sandbox
    ls: cannot access '.ssh/known_hosts': No such file or directory
    docker exec -it --workdir=/root/ jenkins_sandbox
    ['docker', 'exec', '-it', '--workdir=/root/', 'jenkins_sandbox', '/scan-host-key.sh', '172.18.0.3', '/root/']
    # 172.18.0.3:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u6
    # 172.18.0.3:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u6
    # 172.18.0.3:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u6
    # 172.18.0.3:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u6
    # 172.18.0.3:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u6

    jenkins_agent_android IP is 172.18.0.4
    docker exec -it --workdir=/var/jenkins_home jenkins_sandbox
    # Host 172.18.0.4 found: line 52
    # Host 172.18.0.4 found: line 53
    # Host 172.18.0.4 found: line 54
    /var/jenkins_home/.ssh/known_hosts updated.
    Original contents retained as /var/jenkins_home/.ssh/known_hosts.old
    docker exec -it --workdir=/root/ jenkins_sandbox
    Host 172.18.0.4 not found in /root//.ssh/known_hosts
    docker exec -it --workdir=/var/jenkins_home jenkins_sandbox
    known_hosts  known_hosts.old
    docker exec -it --workdir=/var/jenkins_home jenkins_sandbox
    .ssh/known_hosts
    ['docker', 'exec', '-it', '--workdir=/var/jenkins_home', 'jenkins_sandbox', '/scan-host-key.sh', '172.18.0.4', '/var/jenkins_home']
    # 172.18.0.4:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u6
    # 172.18.0.4:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u6
    # 172.18.0.4:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u6
    # 172.18.0.4:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u6
    # 172.18.0.4:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u6

    docker exec -it --workdir=/root/ jenkins_sandbox
    known_hosts
    docker exec -it --workdir=/root/ jenkins_sandbox
    .ssh/known_hosts
    ['docker', 'exec', '-it', '--workdir=/root/', 'jenkins_sandbox', '/scan-host-key.sh', '172.18.0.4', '/root/']
    # 172.18.0.4:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u6
    # 172.18.0.4:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u6
    # 172.18.0.4:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u6
    # 172.18.0.4:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u6
    # 172.18.0.4:22 SSH-2.0-OpenSSH_9.2p1 Debian-2+deb12u6

    git_server_rockstorm IP is 172.18.0.5
    docker exec -it --workdir=/var/jenkins_home jenkins_sandbox
    # Host 172.18.0.5 found: line 52
    # Host 172.18.0.5 found: line 53
    # Host 172.18.0.5 found: line 54
    /var/jenkins_home/.ssh/known_hosts updated.
    Original contents retained as /var/jenkins_home/.ssh/known_hosts.old
    docker exec -it --workdir=/root/ jenkins_sandbox
    Host 172.18.0.5 not found in /root//.ssh/known_hosts
    docker exec -it --workdir=/var/jenkins_home jenkins_sandbox
    known_hosts  known_hosts.old
    docker exec -it --workdir=/var/jenkins_home jenkins_sandbox
    .ssh/known_hosts
    ['docker', 'exec', '-it', '--workdir=/var/jenkins_home', 'jenkins_sandbox', '/scan-host-key.sh', '172.18.0.5', '/var/jenkins_home']
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0

    docker exec -it --workdir=/root/ jenkins_sandbox
    known_hosts
    docker exec -it --workdir=/root/ jenkins_sandbox
    .ssh/known_hosts
    ['docker', 'exec', '-it', '--workdir=/root/', 'jenkins_sandbox', '/scan-host-key.sh', '172.18.0.5', '/root/']
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0

    docker exec -it --workdir=/home/jenkins jenkins_agent
    Cannot stat /home/jenkins/.ssh/known_hosts: No such file or directory
    docker exec -it --workdir=/root/ jenkins_agent
    Cannot stat /root//.ssh/known_hosts: No such file or directory
    docker exec -it --workdir=/home/jenkins jenkins_agent
    authorized_keys
    docker exec -it --workdir=/home/jenkins jenkins_agent
    ls: cannot access '.ssh/known_hosts': No such file or directory
    docker exec -it --workdir=/home/jenkins jenkins_agent
    ['docker', 'exec', '-it', '--workdir=/home/jenkins', 'jenkins_agent', '/scan-host-key.sh', '172.18.0.5', '/home/jenkins']
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0

    docker exec -it --workdir=/root/ jenkins_agent
    ls: cannot access '.ssh': No such file or directory
    docker exec -it --workdir=/root/ jenkins_agent
    docker exec -it --workdir=/root/ jenkins_agent
    ls: cannot access '.ssh/known_hosts': No such file or directory
    docker exec -it --workdir=/root/ jenkins_agent
    ['docker', 'exec', '-it', '--workdir=/root/', 'jenkins_agent', '/scan-host-key.sh', '172.18.0.5', '/root/']
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0

    docker exec -it --workdir=/home/jenkins jenkins_agent_android
    Cannot stat /home/jenkins/.ssh/known_hosts: No such file or directory
    docker exec -it --workdir=/root/ jenkins_agent_android
    Cannot stat /root//.ssh/known_hosts: No such file or directory
    docker exec -it --workdir=/home/jenkins jenkins_agent_android
    authorized_keys
    docker exec -it --workdir=/home/jenkins jenkins_agent_android
    ls: cannot access '.ssh/known_hosts': No such file or directory
    docker exec -it --workdir=/home/jenkins jenkins_agent_android
    ['docker', 'exec', '-it', '--workdir=/home/jenkins', 'jenkins_agent_android', '/scan-host-key.sh', '172.18.0.5', '/home/jenkins']
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0

    docker exec -it --workdir=/root/ jenkins_agent_android
    ls: cannot access '.ssh': No such file or directory
    docker exec -it --workdir=/root/ jenkins_agent_android
    docker exec -it --workdir=/root/ jenkins_agent_android
    ls: cannot access '.ssh/known_hosts': No such file or directory
    docker exec -it --workdir=/root/ jenkins_agent_android
    ['docker', 'exec', '-it', '--workdir=/root/', 'jenkins_agent_android', '/scan-host-key.sh', '172.18.0.5', '/root/']
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0
    # 172.18.0.5:22 SSH-2.0-OpenSSH_10.0
```


из логов пайтон скрипта нужно узнать айпишники ssh-agent, ssh-agent-android и гитсервера

```bash
    jenkins_agent IP is 172.18.0.3
    jenkins_agent_android IP is 172.18.0.4
    git_server_rockstorm IP is 172.18.0.5
```

Эти айпишники нужно использовать при конфигурации нодов

![screenshot 7](images/07.png)

![screenshot 8](images/08.png)

![screenshot 9](images/09.png)

![screenshot 10](images/10.png)

![screenshot 11](images/11.png)

и гитсервера

New job APK_Jenkinsfiles

![screenshot 12](images/12.png)

Now we create new pipeline using local git repo as source

![screenshot 13](images/13.png)

![screenshot 14](images/14.png)

![screenshot 15](images/15.png)
