#!/usr/bin/env ruby

input_string = ARGV[0]

pattern = /.+Holberton.+/ 

puts input_string.match(pattern) || ""
