#!/usr/bin/python3
#
# stderr: No ED25519 host key is known for 172.18.0.7 and you have requested strict checking.
# Host key verification failed.

def sys_cmd (jenkins_container_name, workdir, cmd):
    import os
    command = "docker exec -it "

    if None != workdir:
        command += "--workdir=" + workdir + " "

    command += jenkins_container_name
    print(command)

    ret = os.system(command + " " + cmd)
    return ret

def proc_out(args):
    import subprocess

    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    output =  stdout.decode()

    return output

def get_container_ip (host_container_name):
    import re

    args = ["docker", "exec", "-it",  host_container_name, "ifconfig"]
    ifconfig_output =  proc_out(args)
    if len (ifconfig_output) > 0:
        #print(host_container_name, "ifconfig_output = ", ifconfig_output)

        pattern = "inet addr:(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})  Bcast:"
        a = re.findall(pattern, ifconfig_output)
        if len(a):
            return a[0]

        pattern = "inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})  netmask"
        a = re.findall(pattern, ifconfig_output)
        if len(a):
            return a[0]

        print(ifconfig_output)
    else:
        sys_cmd (host_container_name, None, "ifconfig")

def exec_cmd (jenkins_container_name, workdir, cmd):
    command = "docker exec -it --workdir=" + workdir + " " + jenkins_container_name
    # print(command)

    args = command.split(" ")
    args += cmd.split(" ")
    print(args)

    out = proc_out(args)
    return out


def all_ls_ssh ():
    cmd="ls .ssh"
    cmd="ls -la"

    out = exec_cmd ("jenkins_sandbox", "/var/jenkins_home", cmd)
    print (out)

    out = exec_cmd ("jenkins_agent",             "/home/jenkins",     cmd)
    print (out)

    out = exec_cmd ("jenkins_agent_android",     "/home/jenkins",     cmd)
    print (out)


def add_known_hosts (jenkins_container_name, workdir, host_container_ip):
    #cmd = "ssh-keyscan " + host_container_ip
    #out = exec_cmd (jenkins_container_name, workdir, cmd)
    #print (out)

    cmd = "ls .ssh"
    ret = sys_cmd (jenkins_container_name, workdir, cmd)
    if 0 == ret:
        pass
    else:
        cmd="mkdir .ssh"
        sys_cmd (jenkins_container_name, workdir, cmd)

    cmd = "ls .ssh/known_hosts"
    ret = sys_cmd (jenkins_container_name, workdir, cmd)
    if 0 == ret:
        pass
    else:
        cmd="touch .ssh/known_hosts"
        sys_cmd (jenkins_container_name, workdir, cmd)

    #ret = sys_cmd (jenkins_container_name, workdir, "find / -name scan-host-key.sh")

    cmd = "/scan-host-key.sh " + host_container_ip + " " + workdir
    out = exec_cmd (jenkins_container_name, workdir, cmd)
    print (out)

    #cmd = "cat .ssh/known_hosts"
    #ret = sys_cmd (jenkins_container_name, workdir, cmd)

def ssh_keygen_R (jenkins_container_name, workdir, host_container_ip):
    #cmd = "ls -la .ssh"
    #out = exec_cmd (jenkins_container_name, workdir, cmd)
    #print (jenkins_container_name, workdir, cmd, " -->" ,out)

    cmd = 'ssh-keygen -f "' + workdir + '/.ssh/known_hosts" -R ' + host_container_ip
    ret = sys_cmd (jenkins_container_name, workdir, cmd)

def ssh_git_gitserver(jenkins_container_name, host_container_ip):
    cmd = 'ssh git@' + host_container_ip
    ret = sys_cmd (jenkins_container_name, None, cmd)

def view_pub_key (jenkins_container_name, workdir):
    cmd = "pwd"
    cmd = "ls -la .ssh"
    out = exec_cmd (jenkins_container_name, workdir, cmd)
    print (jenkins_container_name, workdir, cmd, " -->" ,out)

    cmd = "cat .ssh/authorized_keys"
    out = exec_cmd (jenkins_container_name, workdir, cmd)
    print (jenkins_container_name, workdir, cmd, " -->" ,out)

    #cmd = "ls -la agent"
    #cmd = "ls -la"
    #ret = sys_cmd (jenkins_container_name, workdir, cmd)
    #print(ret)

def add_jenkins_agent_known_host_ip(jenkins_builtin_container_name,  host_container_ip):
    ssh_keygen_R    (jenkins_builtin_container_name, "/var/jenkins_home", host_container_ip)
    ssh_keygen_R    (jenkins_builtin_container_name, "/root/",            host_container_ip)
    add_known_hosts (jenkins_builtin_container_name, "/var/jenkins_home", host_container_ip)
    add_known_hosts (jenkins_builtin_container_name, "/root/",            host_container_ip)

def add_jenkins_agent_known_host (jenkins_builtin_container_name, host_container):
    host_container_ip = get_container_ip (host_container)
    if host_container_ip is not None:
        print(host_container + " IP is " + host_container_ip)
        add_jenkins_agent_known_host_ip(jenkins_builtin_container_name, host_container_ip)
        return True
    return False

def add_git_server_known_host_ip (host_container_ip):

    jenkins_builtin_container_name = "jenkins_sandbox"

    ssh_keygen_R    (jenkins_builtin_container_name,       "/var/jenkins_home", host_container_ip)
    ssh_keygen_R    (jenkins_builtin_container_name,       "/root/",            host_container_ip)
    add_known_hosts (jenkins_builtin_container_name,       "/var/jenkins_home", host_container_ip)
    add_known_hosts (jenkins_builtin_container_name,       "/root/",            host_container_ip)

    jenkins_agent_container_name = "jenkins_agent"

    ssh_keygen_R    (jenkins_agent_container_name,         "/home/jenkins",     host_container_ip)
    ssh_keygen_R    (jenkins_agent_container_name,         "/root/",            host_container_ip)
    add_known_hosts (jenkins_agent_container_name,         "/home/jenkins",     host_container_ip)
    add_known_hosts (jenkins_agent_container_name,         "/root/",            host_container_ip)

    jenkins_agent_android_container_name = "jenkins_agent_android"

    ssh_keygen_R    (jenkins_agent_android_container_name, "/home/jenkins",     host_container_ip)
    ssh_keygen_R    (jenkins_agent_android_container_name, "/root/",            host_container_ip)
    add_known_hosts (jenkins_agent_android_container_name, "/home/jenkins",     host_container_ip)
    add_known_hosts (jenkins_agent_android_container_name, "/root/",            host_container_ip)

def add_git_server_known_host (host_container):
    host_container_ip = get_container_ip (host_container)
    if host_container_ip is not None:
        print(host_container + " IP is " + host_container_ip)
        add_git_server_known_host_ip (host_container_ip)
        return True
    return False

jenkins_builtin_container_name = "jenkins_sandbox"
# jenkins_builtin_container_name = "jenkins-blueocean"

add_jenkins_agent_known_host (jenkins_builtin_container_name, "jenkins_agent")
add_jenkins_agent_known_host (jenkins_builtin_container_name, "jenkins_agent_android")

add_git_server_known_host ("git_server_rockstorm")


# view_pub_key("jenkins_agent", "/home/jenkins")
# view_pub_key("git_server_rockstorm", "/home/git")
# all_ls_ssh ()