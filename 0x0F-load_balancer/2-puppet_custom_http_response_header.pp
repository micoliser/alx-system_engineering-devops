# This puppet manifest creates a custom header for a server
servie {'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

exec {'custom header':
  command  => "sed -i \"s/^\tlocation \/ {/\tlocation \/ {\n\t\tadd_header X-Served-By \'$HOSTNAME\';/\" /etc/nginx/sites-available/default",
  path     => 'usr/bin',
}

exec {'restart':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
  subscribe   => Service['nginx'],
}
