## Simple REST

is_logged_in: '/rest/account/is_logged_in',<br/>
login:        '/rest/account/login',<br/>
logout:       '/rest/account/logout',<br/>
refreshSeal:  '/rest/account/update_seal',<br/>
server_about: '/rest/server/about',<br/>

server_license: '/rest/server/license',<br/>
refreshLicense: '/rest/server/refresh_license',<br/>

getTreeNode:    '/rest/tree/node',<br/>
getTreeNodes:   '/rest/tree/nodes',<br/>
getTargetInfo:  '/rest/device/target',<br/>
target_views: '/rest/device/target_views',<br/>
report_views: '/rest/device/report_view',<br/>
targets: '/rest/device/targets',<br/>
locale: '/rest/server/locale',<br/>

alerts_current: '/rest/alert/history',<br/>
alerts_history: '/rest_long/alert/history',<br/>

alerts_history_update: '/rest/alert/history',<br/>

alerts_new_comment:   '/rest/alert/new_comment',<br/>
alerts_get_comments:  '/rest_long/alert/comments',<br/>

inventory_device_descr: '/rest/inventory/device_descr',<br/>
inventory_targets:      '/rest/inventory/targets',<br/>

getUsers:   '/rest/access/userget',<br/>
createUser: '/rest/access/useradd',<br/>
editUser:   '/rest/access/usermod',<br/>
delUsers:   '/rest/access/userdel',<br/>

getGroups:   '/rest/access/groupget',<br/>
createGroup: '/rest/access/groupadd',<br/>
editGroup:   '/rest/access/groupmod',<br/>
delGroups:   '/rest/access/groupdel',<br/>

addUsersToGroup:   '/rest/access/group_addusers',<br/>
delUsersFromGroup: '/rest/access/group_delusers',<br/>

getGroupPaths: '/rest/access/get_group_paths',<br/>
delPathsFromGroup: '/rest/access/group_delpaths',<br/>

changePermissions: '/rest/access/permsmod',<br/>

syncAD: '/rest/access/ldap_sync_ad'<br/>
