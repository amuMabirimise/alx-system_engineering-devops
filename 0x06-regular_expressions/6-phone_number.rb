#!/usr/bin/env ruby

input_string = ARGV[0]

pattern = /^\d{10}$/

puts input_string.match?(pattern) ? "#{input_string}$" : ''
