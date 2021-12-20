import pandas as pd
import statistics
import csv

df = pd.read_csv('StudentsPerformance.csv')

total_score = df['writing score']+df['math score']+df['reading score'].tolist()

total_mean = statistics.mean(total_score)
total_mode = statistics.mode(total_score)
total_median = statistics.median(total_score)

total_std_dev = statistics.stdev(total_score)


first_std_dev_start,first_std_dev_end = total_mean-total_std_dev,total_mean+total_std_dev
second_std_dev_start,second_std_dev_end = total_mean-(2*total_std_dev),total_mean+(2*total_std_dev)
third_std_dev_start,third_std_dev_end = total_mean-(3*total_std_dev),total_mean+(3*total_std_dev)

total_score_of_data_within_1_std_deviation = [result for result in total_score if result > first_std_dev_start and result < first_std_dev_end]
total_score_of_data_within_2_std_deviation = [result for result in total_score if result > second_std_dev_start and result < second_std_dev_end]
total_score_of_data_within_3_std_deviation = [result for result in total_score if result > third_std_dev_start and result < third_std_dev_end]

print("mean={} median={} mode={} standerd_deviation={}".format(total_mean,total_median,total_mode,total_std_dev))

print("{}% of data for height lies within 1 standard deviation".format(len(total_score_of_data_within_1_std_deviation)*100.0/len(total_score)))
print("{}% of data for height lies within 2 standard deviations".format(len(total_score_of_data_within_2_std_deviation)*100.0/len(total_score)))
print("{}% of data for height lies within 3 standard deviations".format(len(total_score_of_data_within_3_std_deviation)*100.0/len(total_score)))
