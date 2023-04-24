# This puppet manifest installs and configures nginx server

exec {'update':
  command => 'sudo apt-get -y update',
  path    => '/usr/bin',
}

package {'ngix':
  ensure   => 'installed',
  command  => 'nginx',
  provider => 'apt',
}

file {'default html':
  ensure  => 'present',
  path    => '/var/www/html/index.nginx-debian.html',
  content => 'Hello World',
}

file {'404 error':
  ensure  => 'present',
  path    => '/usr/share/nginx/html/custom_404.html',
  content => 'Ceci n\'est pas une page',
}

exec {'configure':
  command => 'sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/micoliser permanent;\n\n\terror_page 404 \/custom_404.html;\n\tlocation = \/custom_404.html {\n\t\troot \/usr\/share\/nginx\/html;\n\t\tinternal;\n\t}/" /etc/nginx/sites-available/default',
  path    => '/usr/bin',
}

exec {'restart':
  command => 'sudo service nginx restart',
  path    => '/usr/bin',
}
