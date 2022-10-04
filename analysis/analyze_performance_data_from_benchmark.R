library(readr)
library(ggplot2)
library(dplyr)

raw_data = read_tsv('../secure_monitoring_service_pkg/tests/performance_tests/benchmark/results.tsv')
raw_data$policy <- as.factor(raw_data$policy)
raw_data$percentages <- as.factor(raw_data$percentages)
selected_raw_data <- raw_data[raw_data$tag == "analysis", ]

percentage_grouping <- selected_raw_data %>% group_by(policy, percentages) %>% summarise(avg_max_memory = mean(max_memory),
                                                                                        avg_runtime = mean(runtime))
trials_grouping <- selected_raw_data %>% group_by(policy, num_trials) %>% summarise(avg_max_memory = mean(max_memory),
                                                                                    avg_runtime = mean(runtime))

# Memory Plots
ggplot(percentage_grouping, aes(x=percentages, y=avg_max_memory, color=policy, group=policy)) + geom_point() + geom_line() + labs(title = "Average Peak Memory Usage vs Percent Adoption")
ggplot(trials_grouping, aes(x=num_trials, y=avg_max_memory, color=policy)) + geom_point() + geom_line() + labs(title = "Average Peak Memory Usage vs Number of Trials")

# Runtime Results
ggplot(percentage_grouping, aes(x=percentages, y=avg_runtime, color=policy, group=policy)) + geom_point() + geom_line() + labs(title = "Average Runtime vs Percent Adoption")
ggplot(trials_grouping, aes(x=num_trials, y=avg_runtime, color=policy)) + geom_point() + geom_line() + labs(title = "Average Runtime vs Number of Trials")
