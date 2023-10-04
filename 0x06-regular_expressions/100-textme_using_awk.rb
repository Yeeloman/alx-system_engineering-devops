#!/usr/bin/env ruby
if File.file?(ARGV[0])
  output = `awk '{print $15","$16","$17}' #{ARGV[0]} | tr "]" ":" | awk -F ":" '{print $2","$4","$6":"$7":"$8":"$9":"$10}'`
  puts output
else
  output = `echo #{ARGV[0]} | awk '{print $15","$16","$17}' | tr "]" ":" | awk -F ":" '{print $2","$4","$6":"$7":"$8":"$9":"$10}'`
  puts output
end

