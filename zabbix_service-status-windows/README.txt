说明:检测windows中服务的状态.数据来源为windows的服务管理器.

Template Windows Service State模板中共有4个宏,最多检测4个windows service.
{$WIN_SERVICE_NAME_1}
{$WIN_SERVICE_NAME_2}
{$WIN_SERVICE_NAME_3}
{$WIN_SERVICE_NAME_4}

主机Link到本模板,然后在主机中添加宏和对应的值(windows服务名称),然后禁用掉不需要的items.

cmd中输入net start 查看现在已启动的命令
