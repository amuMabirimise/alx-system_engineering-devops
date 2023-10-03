#!/usr/bin/env ruby
# Accept the argument from the command line
reg = /hbt{0,1}n/
puts ARGV[0].scan(reg).join
