
file {'/tmp/school':
path               => # 'file';
source_permissions => # '0744';
owner              => # 'www-data';
group              => # 'www-data';
content            => 'I love Puppet';
}
