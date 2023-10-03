#!/usr/bin/env ruby
#accepts one argument and pass it to a regular expression matching method
reg = /hbt{1,}n/
puts ARGV[0].scan(reg).join
