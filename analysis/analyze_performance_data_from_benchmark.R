library(readr)
library(ggplot2)
library(dplyr)

############################
# Load Data
############################

raw_data = read_tsv('../secure_monitoring_service_pkg/tests/performance_tests/benchmark/results.tsv')


############################
# Preprocessing
############################

# Set columns types as needed
raw_data$policy <- as.factor(raw_data$policy)
raw_data$hijack_type <- as.factor(raw_data$hijack_type)
raw_data$percentages <- as.factor(raw_data$percentages)

# Select benchmarks
selected_raw_data <- raw_data[raw_data$tag == "analysis", ]
not_optimized_raw_data <- raw_data[raw_data$tag == "notOptimized", ]
optimization_raw_data <- raw_data[raw_data$tag == "optimization", ]
aws_raw_data <- raw_data[raw_data$tag == "aws-z1d.3xlarge", ]


# -----------------------------
# Aggregate Data
# -----------------------------

# Subprefix Attack
subprefix_percentage_grouping <- selected_raw_data %>% group_by(tag, policy, hijack_type, percentages) %>% summarise(avg_max_memory = mean(max_memory),
                                                                                                                 avg_runtime = mean(runtime)) %>% filter(hijack_type == "V4SubprefixHijackScenario")
subprefix_trials_grouping <- selected_raw_data %>% group_by(policy, hijack_type, num_trials) %>% summarise(avg_max_memory = mean(max_memory),
                                                                                                            avg_runtime = mean(runtime)) %>% filter(hijack_type == "V4SubprefixHijackScenario")


# AutoImmune Attack Before Optimization
autoimmune_percentage_grouping <- not_optimized_raw_data %>% group_by(tag, policy, hijack_type, percentages) %>% summarise(avg_max_memory = mean(max_memory),
                                                                                            avg_runtime = mean(runtime)) %>% filter(hijack_type == "SubprefixAutoImmuneScenario")
autoimmune_trials_grouping <- not_optimized_raw_data %>% group_by(tag, policy, hijack_type, num_trials) %>% summarise(avg_max_memory = mean(max_memory),
                                                                                    avg_runtime = mean(runtime)) %>% filter(hijack_type == "SubprefixAutoImmuneScenario")

# AutoImmune Attack After Optimization
optimization_percentage_grouping <- optimization_raw_data %>% group_by(tag, policy, hijack_type, percentages) %>% summarise(avg_max_memory = mean(max_memory),
                                                                                                                 avg_runtime = mean(runtime))
optimization_trials_grouping <- optimization_raw_data %>% group_by(tag, policy, hijack_type, num_trials) %>% summarise(avg_max_memory = mean(max_memory),
                                                                                                                  avg_runtime = mean(runtime))

# AutoImmune Attack After Optimization on AWS
aws_optimization_percentage_grouping <- aws_raw_data %>% group_by(tag, policy, hijack_type, percentages) %>% summarise(avg_max_memory = mean(max_memory),
                                                                                                                            avg_runtime = mean(runtime))
aws_optimization_trials_grouping <- aws_raw_data %>% group_by(tag, policy, hijack_type, num_trials) %>% summarise(avg_max_memory = mean(max_memory),
                                                                                                                       avg_runtime = mean(runtime))

# Merged Percentage Group
merged_data_percentage <- rbind(subprefix_percentage_grouping, autoimmune_percentage_grouping)
merged_data_percentage <- rbind(merged_data_percentage, optimization_percentage_grouping)
merged_data_percentage <- rbind(merged_data_percentage, aws_optimization_percentage_grouping)
k1_policy_merged_percentage <- merged_data_percentage %>% filter(policy == 'v4k1')

# Merged Trials Group
merged_data_trials <- rbind(subprefix_trials_grouping, autoimmune_trials_grouping)
merged_data_trials <- rbind(merged_data_trials, optimization_trials_grouping)
merged_data_trials <- rbind(merged_data_trials, aws_optimization_trials_grouping)
k1_policy_merged_trials <- merged_data_trials %>% filter(policy == 'v4k1')


##################################
# Plotting
##################################

# -----------------------------
# Memory Plots
# -----------------------------

ggplot(k1_policy_merged_percentage, aes(x=percentages, y=avg_max_memory, color=tag, group=tag)) + 
  geom_point() + 
  geom_line() + 
  labs(title = "Average Peak Memory Usage vs Percent Adoption")

ggplot(k1_policy_merged_trials, aes(x=num_trials, y=avg_max_memory, color=tag, group=tag)) + 
  geom_point() + 
  geom_line() + 
  labs(title = "Average Peak Memory Usage vs Number of Trials")


# ggplot(percentage_grouping, aes(x=percentages, y=avg_max_memory, color=policy, group=policy)) + geom_point() + geom_line() + labs(title = "Average Peak Memory Usage vs Percent Adoption")
# ggplot(trials_grouping, aes(x=num_trials, y=avg_max_memory, color=policy)) + geom_point() + geom_line() + labs(title = "Average Peak Memory Usage vs Number of Trials")


# -----------------------------
# Runtime Results
# -----------------------------

ggplot(k1_policy_merged_percentage, aes(y=avg_runtime, x=percentages, group=tag, color=tag)) + 
  geom_line() + 
  geom_point() + 
  labs(title = "Average Runtime vs Percent Adoption")

ggplot(k1_policy_merged_trials, aes(y=avg_runtime, x=num_trials, group=tag, color=tag)) + 
  geom_line() + 
  geom_point() + 
  labs(title = "Average Runtime vs Number of Trials")


# ggplot(percentage_grouping, aes(x=percentages, y=avg_runtime, color=policy, group=policy)) + geom_point() + geom_line() + labs(title = "Average Runtime vs Percent Adoption")
# ggplot(trials_grouping, aes(x=num_trials, y=avg_runtime, color=policy)) + geom_point() + geom_line() + labs(title = "Average Runtime vs Number of Trials")
