library(ggplot2)
library(dplyr)
library(tibble)
library(readr)
library(stringr)


##############################
# Load Data
##############################

# as_metadata <- read_tsv('../data/as_metadata/seed_1_1_trails_k1_capture_avoid_list_traceback_asn_brackets_removed.tsv')

tsv_file_path <- commandArgs(trailingOnly=TRUE)[1]
as_metadata <- read_tsv(tsv_file_path)

##############################
# Preprocess Data
##############################

avoid_list_as_sting <- as_metadata$simAvoidList[which(!is.na(as_metadata$simAvoidList))][1]
avoid_list <- as.numeric(strsplit(avoid_list_as_sting, ", ")[[1]])

attacker_asn = as_metadata$attackerASN[1] 
victim_asn = as_metadata$victimASN[1]

# Get the disconnected cases
outcomes_vec <- c()
avoided_asn_traceback_asns_vec <- c()
for (avoided_asn in avoid_list) {
  avoided_asn_traceback_asn <- as_metadata$traceback_asn[as_metadata$asn == avoided_asn]
  avoided_asn_traceback_asns_vec <- c(avoided_asn_traceback_asns_vec, 
                                      avoided_asn_traceback_asn)
  outcome <- NA
  if (avoided_asn_traceback_asn == attacker_asn) {
    outcome <- "Attacker"
  } else if (avoided_asn_traceback_asn == victim_asn) {
    outcome <- "Victim"
  } else {
    outcome <- "Disconnected"
  }
  outcomes_vec <- c(outcomes_vec, outcome)
}

reduced_data <- tibble(avoidListASN=avoid_list,
                       outcome=outcomes_vec,
                       tracebackASN=avoided_asn_traceback_asns_vec)
print(reduced_data)