# Using Puppet, create a manifest that kills a process named killmenow
exec { 'kill':
  command      => 'pkill -f killmenow',
  path         => '/usr/bin/',
  onlyif       => 'pgrep -f killmenow',
  logoutput    => true,
  refreshonly  => true,
}
