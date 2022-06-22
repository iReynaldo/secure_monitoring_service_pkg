library(ggplot2)
library(dplyr)
library(tibble)
library(readr)

##############################
# Load Data
##############################

avoid_lists <- read_tsv('./report_path_lists/avoid_list_5_trails.tsv')
reduced_avoid_list <- avoid_lists[which(avoid_lists$trial %in% c(0)), ]
write_tsv(reduced_avoid_list, './report_path_lists/avoid_list_1_trails.tsv')


as_metadata <- read_tsv('./as_metadata/k0_5_trials_as_metadata.tsv')
reduced_as_metadata <- as_metadata[which(as_metadata$trial %in% c(0)), ]
write_tsv(reduced_as_metadata, './as_metadata/k0_1_trials_as_metadata.tsv')
