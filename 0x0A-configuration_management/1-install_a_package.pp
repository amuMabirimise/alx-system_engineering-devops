# 2-install_puppet_lint.pp

# Exec resource to install puppet-lint
exec { 'install_puppet_lint':
  command => '/usr/bin/gem install puppet-lint -v 2.5.0',
  path    => '/usr/bin',
  unless  => '/usr/bin/gem list puppet-lint | grep -q 2.5.0',
}
