# increase the limit on open files to allow requests to be handled

exec {'start':
  provider => shell,
  command  => 'sudo sed -i "s/15/4000/" /etc/default/nginx;sudo service nginx restart'
}
