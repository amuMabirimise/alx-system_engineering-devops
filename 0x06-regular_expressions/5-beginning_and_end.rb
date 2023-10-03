#!/usr/bin/env ruby

input_string = ARGV[0]

pattern = /^h.n$/

puts input_string =~ pattern ? input_string : ''
