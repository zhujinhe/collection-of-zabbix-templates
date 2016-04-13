此模板为监控HOST到某个IP的某个端口的TCP连通性.

1.导入zbx_connectivity_template.xml到模板
2.在主机上连接此模板
3.重要:在主机上增加Macros宏:
{$CONNIP1}和{$CONNPORT1},分别对应的值为例如172.27.2.123和3306
{$CONNIP2}和{$CONNPORT2},第2个检测值,如果不需要则不需要填写,(可选:并在host的items中的status选择设置为disabled)
{$CONNIP3}和{$CONNPORT3},第3个检测值,如果不需要则不需要填写,(可选:并在host的items中的status选择设置为disabled)
{$CONNIP4}和{$CONNPORT4},第4个检测值,如果不需要则不需要填写,(可选:并在host的items中的status选择设置为disabled)