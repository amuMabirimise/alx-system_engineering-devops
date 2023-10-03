#!/usr/bin/env ruby

input_string = ARGV[0]

puts input_string.match(/.+Holberton.+/) ? input_string : ""
