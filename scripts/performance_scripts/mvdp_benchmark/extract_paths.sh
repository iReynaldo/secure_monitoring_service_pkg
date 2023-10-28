#!/bin/sh

file=${1};
outfile_name=${2};

# Remove the first line
first_line_stripped="first_line_stripped_$file";
tail -n +2 $file > $first_line_stripped; 

# Remove the last line
last_line_stripped="last_line_stripped_${first_line_stripped}";
sed '$ d' $first_line_stripped > $last_line_stripped;

# Append to a list
report_list="report_list_${last_line_stripped}"
sed 's/Report/reports_path_list.append(Report/g' $last_line_stripped | sed 's/))/)).as_path)/g' > $report_list

# Add import line
cat import_lines.txt $report_list > $outfile_name

rm $first_line_stripped $last_line_stripped $report_list
