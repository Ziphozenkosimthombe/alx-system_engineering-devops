#!/usr/bin/env ruby
#  regular expression that will match the given expression pattern.
puts ARGV[0].scan(/[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
