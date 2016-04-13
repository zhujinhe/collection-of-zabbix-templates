修改1:

默认的模板中关于进程数量的设置分别为所有进程300,running进程30,Load average默认值5.无法针对机器进行个性化设置.
因此在默认的模板基础上增加了3个macros:
{$PROCESS_NUMBER}:300
{$RUNNING_PROCESS_NUMBER}:30
{$PROCESSOR_LOAD}:5
需要针对某台机器个性化设置可以在主机模板增加相应的宏,并设置数值.

注:
针对macros的设置生效时间较长.

修改2:
默认模板中的Regular expressions中File systems for discovery未设置监控nfs格式的磁盘.
修改前:^(btrfs|ext2|ext3|ext4|jfs|reiser|xfs|ffs|ufs|jfs|jfs2|vxfs|hfs|ntfs|fat32|zfs)$	[Result is TRUE]
修改后:^(btrfs|ext2|ext3|ext4|jfs|reiser|xfs|ffs|ufs|jfs|jfs2|vxfs|hfs|ntfs|fat32|zfs|nfs)$	[Result is TRUE]


如果Template连接大量的hosts后,在web页面修改Template容易执行超时.举例:
修改Template OS Linux(templateid=10001)中的Trigger:Too many processes on {HOST.NAME}(Expression的itemid=10009,连接的triggerid=10190)
#  trigger表的表结构说明“CONSTRAINT `c_triggers_1` FOREIGN KEY (`templateid`) REFERENCES `triggers` (`triggerid`) ON DELETE CASCADE”,修改模板和对应hosts的此trigger需要更改的地方。这里的templateid字段代表的是trigger的模板,不是host的template.

select * from triggers where triggerid='10190';
select * from `triggers` where templateid='10190';
update `triggers` set expression=REPLACE(expression,'>350','>{$PROCESS_NUMBER}') where triggerid='10190';
update `triggers` set expression=REPLACE(expression,'>350','>{$PROCESS_NUMBER}') where templateid='10190';
