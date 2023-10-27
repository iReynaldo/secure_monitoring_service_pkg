library(jsonlite)
library(ggplot2)
library(dplyr)

json = read_json('../data/performance_data/peformance_test.json', simplifyVector = TRUE)
json$policy <- as.factor(json$policy)

percentage_grouping <- json %>% group_by(policy, percentage) %>% summarise(avg_max_memory = mean(max_memory),
                                                                           avg_runtime = mean(total_time))
trials_grouping <- json %>% group_by(policy, trials) %>% summarise(avg_max_memory = mean(max_memory),
                                                                   avg_runtime = mean(total_time))

# Memory Plots
ggplot(percentage_grouping, aes(x=percentage, y=avg_max_memory, color=policy)) + geom_point() + geom_line() + labs(title = "Average Peak Memory Usage vs Percent Adoption")
ggplot(trials_grouping, aes(x=trials, y=avg_max_memory, color=policy)) + geom_point() + geom_line() + labs(title = "Average Peak Memory Usage vs Number of Trials")

# Runtime Results
ggplot(percentage_grouping, aes(x=percentage, y=avg_runtime, color=policy)) + geom_point() + geom_line() + labs(title = "Average Runtime vs Percent Adoption")
ggplot(trials_grouping, aes(x=trials, y=avg_runtime, color=policy)) + geom_point() + geom_line() + labs(title = "Average Runtime vs Number of Trials")
