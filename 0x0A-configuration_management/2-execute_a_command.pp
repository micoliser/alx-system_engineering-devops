# This puppet manifest executes a kill command

exec { 'pkill killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin',
}
