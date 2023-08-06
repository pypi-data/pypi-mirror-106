Ibnsession
=======

Multi-vendor library to control network devices


## tool introducition
This tool is for ibn design


## Environment
```
[root@local ~]# cat /etc/redhat-release 
CentOS Linux release 7.2.1511 (Core) 

[root@szzabbixt01 ~]# python
Python 2.7.5 (default, Nov 20 2015, 02:00:19) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-4)] on linux2

[root@local ~]# pip show netmiko
Metadata-Version: 1.1
Name: netmiko
Version: 2.0.2
```

## Dir tree introduction
```
```



## Example
```
```

## Update log
#### 0.01 Design this package

#### 0.02 Add hillstone related update
- add function : generate_access_script(self,basic_info,session_list)
- add function : execute_access_script(self,access_script_list)

#### 0.1.0 Add SRX related update
- add function : generate_routing_script(self, route_info_list)
- add function : get_running_config(self)

#### 1.3 Add new module
- add huawei.py
- add cisco.py

#### 1.3.1 update huawei module
- remove print info
- update all module , add new parameter:config_mode_tag
```
account_verification(self, config_mode_tag="config"):
```  
