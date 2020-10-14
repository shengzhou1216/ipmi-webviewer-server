# 使用namp扫描网络中支持IPMI的设备
- 方案1
> nmap -sU --script ipmi-version -p 623 10.1.35.155/24 
___
-sU: UDP端口扫描

-p: 扫描制定端口

--script : https://nmap.org/book/nse.html
___
扫描结果：
```
Starting Nmap 7.60 ( https://nmap.org ) at 2020-10-12 19:39 CST
Nmap scan report for _gateway (10.1.35.1)
Host is up (0.0030s latency).

PORT    STATE  SERVICE
623/udp closed asf-rmcp
MAC Address: 78:C5:F8:5B:4E:93 (Unknown)

Nmap scan report for 10.1.35.10
Host is up (0.0055s latency).

PORT    STATE  SERVICE
623/udp closed asf-rmcp
MAC Address: 34:48:ED:F3:37:50 (Unknown)

Nmap scan report for 10.1.35.11
Host is up (-0.076s latency).

PORT    STATE  SERVICE
623/udp closed asf-rmcp
MAC Address: E4:43:4B:E3:82:64 (Unknown)

Nmap scan report for 10.1.35.13
Host is up (-0.074s latency).

PORT    STATE SERVICE
623/udp open  asf-rmcp
| ipmi-version: 
|   Version: 
|     IPMI-2.0
|   UserAuth: md5
|   PassAuth: non_null_user
|_  Level: 2.0
MAC Address: 70:B5:E8:C8:75:2C (Unknown)

Nmap scan report for 10.1.35.15
Host is up (-0.075s latency).

PORT    STATE  SERVICE
623/udp closed asf-rmcp
MAC Address: 00:C0:FF:52:1A:7D (DOT Hill Systems)

Nmap scan report for 10.1.35.16
Host is up (-0.075s latency).

PORT    STATE  SERVICE
623/udp closed asf-rmcp
MAC Address: 00:C0:FF:52:16:67 (DOT Hill Systems)

Nmap scan report for 10.1.35.19
Host is up (0.0028s latency).

PORT    STATE SERVICE
623/udp open  asf-rmcp
| ipmi-version: 
|   Version: 
|     IPMI-2.0
|   UserAuth: md5
|   PassAuth: non_null_user
|_  Level: 2.0
MAC Address: 70:B5:E8:C8:84:C8 (Unknown)

Nmap scan report for 10.1.35.22
Host is up (0.0026s latency).

PORT    STATE  SERVICE
623/udp closed asf-rmcp
MAC Address: 00:22:E4:00:89:23 (Apass Technology)

Nmap scan report for 10.1.35.25
Host is up (0.0028s latency).

PORT    STATE  SERVICE
623/udp closed asf-rmcp
MAC Address: 00:22:E4:00:89:63 (Apass Technology)

Nmap scan report for 10.1.35.30
Host is up (-0.12s latency).

PORT    STATE         SERVICE
623/udp open|filtered asf-rmcp
MAC Address: E4:43:4B:E4:A1:52 (Unknown)

Nmap scan report for 10.1.35.31
Host is up (-0.073s latency).

PORT    STATE SERVICE
623/udp open  asf-rmcp
| ipmi-version: 
|   Version: 
|     IPMI-2.0
|   UserAuth: md5
|   PassAuth: auth_user, non_null_user
|_  Level: 1.5, 2.0
MAC Address: 5C:FF:35:E1:83:B1 (Wistron)

Nmap scan report for 10.1.35.32
Host is up (-0.074s latency).

PORT    STATE SERVICE
623/udp open  asf-rmcp
| ipmi-version: 
|   Version: 
|     IPMI-2.0
|   UserAuth: md5
|   PassAuth: auth_user, non_null_user
|_  Level: 1.5, 2.0
MAC Address: 5C:FF:35:E1:9A:41 (Wistron)

Nmap scan report for 10.1.35.33
Host is up (-0.072s latency).

PORT    STATE SERVICE
623/udp open  asf-rmcp
| ipmi-version: 
|   Version: 
|     IPMI-2.0
|   UserAuth: md5
|   PassAuth: auth_user, non_null_user
|_  Level: 1.5, 2.0
MAC Address: 5C:FF:35:E1:83:96 (Wistron)

Nmap scan report for 10.1.35.34
Host is up (-0.073s latency).

PORT    STATE SERVICE
623/udp open  asf-rmcp
| ipmi-version: 
|   Version: 
|     IPMI-2.0
|   UserAuth: md5
|   PassAuth: auth_user, non_null_user
|_  Level: 1.5, 2.0
MAC Address: 5C:FF:35:E1:9A:71 (Wistron)

Nmap scan report for 10.1.35.35
Host is up (-0.074s latency).

PORT    STATE SERVICE
623/udp open  asf-rmcp
| ipmi-version: 
|   Version: 
|     IPMI-2.0
|   UserAuth: md5
|   PassAuth: auth_user, non_null_user
|_  Level: 1.5, 2.0
MAC Address: 5C:FF:35:E1:83:41 (Wistron)

Nmap scan report for 10.1.35.36
Host is up (-0.072s latency).

PORT    STATE SERVICE
623/udp open  asf-rmcp
| ipmi-version: 
|   Version: 
|     IPMI-2.0
|   UserAuth: md5
|   PassAuth: auth_user, non_null_user
|_  Level: 1.5, 2.0
MAC Address: 5C:FF:35:E1:9A:A8 (Wistron)

Nmap scan report for 10.1.35.37
Host is up (-0.081s latency).

PORT    STATE SERVICE
623/udp open  asf-rmcp
| ipmi-version: 
|   Version: 
|     IPMI-2.0
|   UserAuth: md5
|   PassAuth: auth_user, non_null_user
|_  Level: 1.5, 2.0
MAC Address: 5C:FF:35:E1:9A:64 (Wistron)

Nmap scan report for 10.1.35.38
Host is up (-0.087s latency).

PORT    STATE SERVICE
623/udp open  asf-rmcp
| ipmi-version: 
|   Version: 
|     IPMI-2.0
|   UserAuth: md5
|   PassAuth: auth_user, non_null_user
|_  Level: 1.5, 2.0
MAC Address: 5C:FF:35:E1:83:8D (Wistron)

Nmap scan report for 10.1.35.89
Host is up (0.0031s latency).

PORT    STATE SERVICE
623/udp open  asf-rmcp
| ipmi-version: 
|   Version: 
|     IPMI-2.0
|   UserAuth: md5
|   PassAuth: non_null_user
|_  Level: 2.0
MAC Address: F4:02:70:B1:6D:8E (Unknown)

Nmap scan report for 10.1.35.95
Host is up (0.0035s latency).

PORT    STATE  SERVICE
623/udp closed asf-rmcp
MAC Address: E4:43:4B:CF:26:84 (Unknown)

Nmap scan report for 10.1.35.96
Host is up (0.0029s latency).

PORT    STATE  SERVICE
623/udp closed asf-rmcp
MAC Address: E4:43:4B:E8:94:EC (Unknown)

Nmap scan report for 10.1.35.99
Host is up (0.0034s latency).

PORT    STATE SERVICE
623/udp open  asf-rmcp
| ipmi-version: 
|   Version: 
|     IPMI-2.0
|   UserAuth: md5
|   PassAuth: non_null_user
|_  Level: 2.0
MAC Address: 4C:D9:8F:0B:97:1A (Unknown)

Nmap scan report for 10.1.35.101
Host is up (0.0032s latency).

PORT    STATE  SERVICE
623/udp closed asf-rmcp
MAC Address: 5C:FF:35:E1:83:02 (Wistron)

Nmap scan report for 10.1.35.106
Host is up (-0.074s latency).

PORT    STATE  SERVICE
623/udp closed asf-rmcp
MAC Address: 5C:FF:35:E1:99:A4 (Wistron)

Nmap scan report for 10.1.35.108
Host is up (-0.074s latency).

PORT    STATE  SERVICE
623/udp closed asf-rmcp
MAC Address: 5C:FF:35:E1:82:DE (Wistron)

Nmap scan report for 10.1.35.111
Host is up (-0.11s latency).

PORT    STATE  SERVICE
623/udp closed asf-rmcp
MAC Address: E4:43:4B:E3:83:10 (Unknown)

Nmap scan report for 10.1.35.113
Host is up (-0.073s latency).

PORT    STATE SERVICE
623/udp open  asf-rmcp
| ipmi-version: 
|   Version: 
|     IPMI-2.0
|   UserAuth: md5
|   PassAuth: non_null_user
|_  Level: 2.0
MAC Address: 70:B5:E8:C8:B7:3E (Unknown)

Nmap scan report for 10.1.35.115
Host is up (-0.074s latency).

PORT    STATE  SERVICE
623/udp closed asf-rmcp
MAC Address: 0C:42:A1:D8:8F:4A (Unknown)

Nmap scan report for 10.1.35.116
Host is up (-0.074s latency).

PORT    STATE  SERVICE
623/udp closed asf-rmcp
MAC Address: 0C:42:A1:D9:85:12 (Unknown)

Nmap scan report for 10.1.35.119
Host is up (-0.098s latency).

PORT    STATE         SERVICE
623/udp open|filtered asf-rmcp
MAC Address: 00:24:AC:C0:4B:8F (Hangzhou DPtech Technologies)

Nmap scan report for 10.1.35.132
Host is up (0.065s latency).

PORT    STATE  SERVICE
623/udp closed asf-rmcp
MAC Address: 74:B5:87:3C:5C:0D (Unknown)

Nmap scan report for 10.1.35.133
Host is up (0.063s latency).

PORT    STATE  SERVICE
623/udp closed asf-rmcp
MAC Address: 14:7D:DA:1C:73:C6 (Unknown)

Nmap scan report for 10.1.35.134
Host is up (0.058s latency).

PORT    STATE         SERVICE
623/udp open|filtered asf-rmcp
MAC Address: 1A:BB:53:D5:C1:DC (Unknown)

Nmap scan report for 10.1.35.135
Host is up (0.049s latency).

PORT    STATE         SERVICE
623/udp open|filtered asf-rmcp
MAC Address: F8:E4:E3:EA:1E:AB (Unknown)

Nmap scan report for 10.1.35.136
Host is up (0.059s latency).

PORT    STATE         SERVICE
623/udp open|filtered asf-rmcp
MAC Address: 04:33:C2:B9:54:8D (Unknown)

Nmap scan report for 10.1.35.139
Host is up (-0.041s latency).

PORT    STATE  SERVICE
623/udp closed asf-rmcp
MAC Address: 40:74:E0:DB:F1:5A (Unknown)

Nmap scan report for 10.1.35.141
Host is up (0.0025s latency).

PORT    STATE         SERVICE
623/udp open|filtered asf-rmcp
MAC Address: 70:B5:E8:C8:86:9C (Unknown)

Nmap scan report for 10.1.35.142
Host is up (-0.031s latency).

PORT    STATE  SERVICE
623/udp closed asf-rmcp
MAC Address: 84:FD:D1:3C:63:51 (Unknown)

Nmap scan report for 10.1.35.144
Host is up (-0.086s latency).

PORT    STATE         SERVICE
623/udp open|filtered asf-rmcp
MAC Address: 70:B5:E8:C8:82:6A (Unknown)

Nmap scan report for 10.1.35.145
Host is up (0.0034s latency).

PORT    STATE         SERVICE
623/udp open|filtered asf-rmcp
MAC Address: 70:B5:E8:C8:86:06 (Unknown)

Nmap scan report for 10.1.35.150
Host is up (-0.13s latency).

PORT    STATE         SERVICE
623/udp open|filtered asf-rmcp
MAC Address: 70:B5:E8:C8:76:34 (Unknown)

Nmap scan report for 10.1.35.151
Host is up (-0.12s latency).

PORT    STATE         SERVICE
623/udp open|filtered asf-rmcp
MAC Address: 70:B5:E8:C8:B9:4E (Unknown)

Nmap scan report for 10.1.35.152
Host is up (-0.12s latency).

PORT    STATE         SERVICE
623/udp open|filtered asf-rmcp
MAC Address: 70:B5:E8:C8:BB:40 (Unknown)

Nmap scan report for 10.1.35.153
Host is up (-0.11s latency).

PORT    STATE         SERVICE
623/udp open|filtered asf-rmcp
MAC Address: AC:07:5F:34:91:B5 (Unknown)

Nmap scan report for 10.1.35.154
Host is up (-0.098s latency).

PORT    STATE  SERVICE
623/udp closed asf-rmcp
MAC Address: B8:CB:29:98:D5:23 (Unknown)

Nmap scan report for stark-900X3L (10.1.35.155)
Host is up (0.00014s latency).

PORT    STATE  SERVICE
623/udp closed asf-rmcp

Nmap done: 256 IP addresses (46 hosts up) scanned in 6.97 seconds
```

# 如何处理脚本输出的数据
迭代输出流，使用python的字符串相关的方法处理

# 