# Using strace, find out why Apache is returning a 500 error.

file {'.phpp':
  ensure => 'file',
  path   => '/var/www/html/wp-includes/class-wp-locale.phpp',
  source => '/var/www/html/wp-includes/class-wp-locale.php',
}

file {'.php':
  ensure  => 'absent',
  path    => '/var/www/html/wp-includes/class-wp-locale.php',
  require => FILE['.phpp'],
}
