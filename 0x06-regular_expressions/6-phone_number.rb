#!/usr/bin/env ruby
#  regular expression that will match the 10 digit pgone numbers
puts ARGV[0].scan(/^[0-9]{10}$/).join
