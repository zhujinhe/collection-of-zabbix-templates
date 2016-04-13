memcached-zabbix-template
=========================

Description
-----------

This is a minimal template to get info from your Memcached server from two possible places. Via zabbix-agentd in clients or via externalscripts in zabbix server. Choose your option.

Monitoring information by now:

* 'bytes',
* 'cmd_get',
* 'cmd_set',
* 'curr_items',
* 'curr_connections',
* 'limit_maxbytes',
* 'uptime',
* 'get_hits',
* 'get_misses',

And the special HIT-ratio in %:
 
 * 'ratio'
 
Installation in the Zabbix Server
---------------------------------

You should look for the external scripts directory in your Zabbix Server configuration file. 
In the CentOS 6.5 RPM Zabbix installation is: 

``` 
 /usr/lib/zabbix/externalscripts 
```

Or, you can search the externalscripts folder by running:

```
find / -name externalscripts
```

Copy the python script there. A chmod/chown to get execution permission is necessary.

Now, in your Zabbix frontend: Configuration-Templates section, Import bottom in the right side.

Choose the XML file and import.

Apply this new template to your Memcached servers. 

You don't need to modify the template if you are using the standard port to access to the Memcached (port 11211).

It permits a fast configuration because of you can apply the same template to all your memcached servers without modification/installation in the agents.

Of course, it can be to work in the agent/client side too.

Environment
-----------

I am using this script in my production environment:

* Zabbix 2.2.x

Screenshots
-----------

![Screenshot](img/memcached-zabbix.jpg)
