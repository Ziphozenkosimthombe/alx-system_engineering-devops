# insatlling flask from pip3 using Puppet
package { 'python3-pip':
  ensure => present,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0 Werkzeug==2.0.2',
  path    => '/usr/bin',
  require => Package['python3-pip'],
}
