library(ggplot2)
library(dplyr)

##############################
# Load Data
##############################

data <- read.csv('./report_path_lists/avoid_list_10_trials.tsv', sep='\t')

##############################
# Preprocess Data
##############################

data$attackerInAvoidList <- as.logical(data$attackerInAvoidList)
averaged_data <- data %>% group_by(percentAdoption, k) %>% summarise(avgAvoidListSize = round(mean(avoidListSize)), 
                                                                     avgAttackerInAvoidList = mean(attackerInAvoidList))
averaged_data$k <- as.factor(as.character(averaged_data$k))


##############################
# Plotting
##############################

# Avoid List Size

ggplot(averaged_data) + geom_line(mapping = aes(x=percentAdoption, y=avgAvoidListSize, group=k, color=k)) +
  geom_point(mapping = aes(x=percentAdoption, y=avgAvoidListSize, group=k, color=k)) +
  labs(title="Avoid List Size vs. Percent Adoption w/ k",
       x="Percent Adoption",
       y="Avg Avoid List Size") +
  theme(legend.title = element_text(size = 14),
        legend.text = element_text(size = 14),
        axis.title = element_text(size = 14),
        axis.text.x = element_text(size = 12),
        axis.text.y = element_text(size = 12),
        plot.title = element_text(size = 16))


# Attacker in Avoid List

ggplot(averaged_data) + geom_line(mapping = aes(x=percentAdoption, y=avgAttackerInAvoidList, group=k, color=k)) +
  geom_point(mapping = aes(x=percentAdoption, y=avgAttackerInAvoidList, group=k, color=k)) +
  labs(title="Avg Times Attacker in Avoid List vs. Percent Adoption w/ k",
       x="Percent Adoption",
       y="Avg Times Attacker in Avoid List") +
  theme(legend.title = element_text(size = 14),
        legend.text = element_text(size = 14),
        axis.title = element_text(size = 14),
        axis.text.x = element_text(size = 12),
        axis.text.y = element_text(size = 12),
        plot.title = element_text(size = 16))
