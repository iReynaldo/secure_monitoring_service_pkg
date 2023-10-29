library(ggplot2)
library(dplyr)
library(tibble)
library(readr)
library(stringr)

##############################
# Load Data
##############################


# avoid_lists <- read_tsv('./report_path_lists/avoid_list_5_trails_brackets_removed.tsv')
# as_metadata <- read_tsv('./as_metadata/sed_head_80000_k0_5_trials_as_metadata.tsv')
# as_metadata <- read_tsv('as_metadata/head_80000_k0_5_trials_as_metadata_brackets_removed.tsv')

triggerASes <- read_tsv('./triggerASes.tsv')

##############################
# Preprocess Data
##############################



triggerASes$triggerASes <- as.factor(as.character(triggerASes$triggerASes))

# # Avoid list Preprocessing
# avoid_lists_averaged_data <- avoid_lists %>% group_by(percentAdoption, k) %>% summarise(avgAvoidListSize = round(mean(avoidListSize)), 
#                                                                      avgAttackerInAvoidList = mean(attackerInAvoidList))
# avoid_lists_averaged_data$k <- as.factor(as.character(avoid_lists_averaged_data$k))
# 
# # Merge data
# merged_data <- merge(avoid_lists, as_metadata, by = c('percentAdoption', 'trial'))
# 
# # Function to use in mutation
# intersect_numeric_char_lists <- function(x, y) {
#   result =  intersect(
#               as.numeric(strsplit(x, split=',')[[1]]),
#               as.numeric(strsplit(y, split=',')[[1]])
#             )
#   if (length(result) == 0) {
#     return(c())
#   } else {
#     return(result)
#   }
# }
# 
# merged_data$legitPrefixASPath[1] = "1, 2, 6, 8, 5, 9"
# merged_data$avoidList[1] = "2, 3"
# 
# merged_data$legitPrefixASPath[2] = "1, 2, 6, 8, 5, 9"
# merged_data$avoidList[2] = "1, 5, 0, 9"
# 
# merged_data <- merged_data %>% mutate(in_avoid_list = mapply(intersect_numeric_char_lists, legitPrefixASPath, avoidList))


##############################
# Plotting
##############################

ggplot(triggerASes, aes(x = triggerASes)) + geom_histogram(stat="count")
