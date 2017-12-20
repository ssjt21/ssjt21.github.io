---
layout: post
title: "Linux Shell OpenSSH 安装脚本"
date: 2017-12-13 11:13:06 
description: "Linux Shell 山东中移在线 项目实施过程中，客户要求要写的脚本"
tag: Shell
---

记一次山东项目实施OpenSSH安装脚本的实现

### CentOS 7 SHELL实现
```Shell
#!/bin/bash
echo -e "\033[31m ----------------- Statement -----------------------\033[0m"

echo -e "All responsibility for using this shell is borne by the user, and developers of this shell do not take any responsibility!When openssh install complete,Please decide how to handle the unzip file of OpenSSH. The shell dose not perform any deleting on the host!"

echo -e "\033[31m ---------The end of Statement -----------------------\033[0m"

echo -e "\033[31m 
Agree with the above statement please enter key to continue ,if not ,please use CTR+C to exit!\033[0m"
read -p "" var
echo -e "\033[35m * Currently installed Version of OpenSSH.. \033[0m" 
ssh -V

read -p "# Press enter key to continue.." var

echo -e "\033[35m * Directory information of the OpenSSH that has installed..\033[0m"

whereis ssh
whereis sshd
whereis opensssh 

read -p "# Press enter key to continue.." var

echo -e "\033[35m * OpenSSH Service is stoping.....\033[0m"
SSHD=`whereis -b sshd | awk '$2~/sshd$/{print $2}'`
systemctl stop sshd || service sshd stop || $SSHD stop

read -p "# Press enter key to continue.." var

echo -e "\033[35m Backuping OpenSSH Files....\033[0m"

for ssh_file in `whereis -b ssh && whereis -b sshd | awk -F " " {print}`
do
    if [ -e $ssh_file ] && [[ -d $ssh_file || -f $ssh_file ]]
    then
        Time=$(date +%Y_%m_%d_%H%M%S)
        newname=${ssh_file}_bak_${Time}
        echo -e "\033[32m Backup ${ssh_file} file to  ${newname}.....\033[0m"
        if [ -d $ssh_file ]
        then
            #cp -r $ssh_file $newname
            echo "backuing..."
        else
            #cp $ssh_file $newname
            echo "backuping..."
        fi
    fi
done

read -p "# Backuping has been completed!.... Press enter key to continue." var

echo -e "\033[32m * Current dir
ectory '.tar.gz' package:\033[0m"

ls | grep .tar.gz

if [ `ls | grep *ssh*.tar.gz` ]
then
ssh_package=`ls | grep *ssh*.tar.gz`
else
echo -e "\033[33m Please copy your OpenSSH '.tar.gz' package  to current folder..."
exit
fi

read -p "# Press enter key to continue.." var

echo -e "\033[32m Execute tar -xzf ${ssh_package}...\033[0m"

tar -xzf $ssh_package

ssh_dir=${ssh_package%.*}
ssh_dir=${ssh_dir%.*}
echo -e "\033[32m Execute cd ${ssh_dir}...\033[0m"
cd $ssh_dir

read -p "# Press enter key to continue.." var

echo -e "\033[32m Execute ./configure  ...\033[0m"
./configure

read -p "# Press enter key to continue.." var

echo -e "\033[32m Execute make && make install  ...\033[0m"

make && make install

read -p "# Press enter key to continue.." var

echo -e "\033[32m $ssh_dir has installed successful ! The OpenSSH Service will statred ...\033[0m"

systemctl restart sshd || service sshd restart || $SSHD restart

echo -e "\033[32m OpenSSH services has started !  ...\033[0m"
echo -e "\033[32m Current OpenSSH version:\033[0m"

ssh -V

echo -e "\033[31m Install OpenSSH has completed! The shell will be exit. Please decide how to handle the unzip file of OpenSSH. The shell dose not perform any deleting on the host!All responsibility for using this shell is borne by the user, and developers of this shell do not take any responsibility.\033[0m" 
```

推荐阅读：

- [Linux Shell 四种读取文件内容的方式](http://ssjt21.github.io/2017/12/Shell_Readfile/)

- [Linux 系统目录结构](http://ssjt21.github.io/2017/11/Linux_DirStruct/)

- [Linux 获取系统登陆用户密码的加密方式](http://ssjt21.github.io/2017/11/Linux_Get_SYS_CryptMode/)


<br>

转载请注明：[随时静听的博客](http://ssjt21.github.io) » [点击阅读原文](http://ssjt21.github.io/2017/12/Shell_OpenSSH_autoinstall/)