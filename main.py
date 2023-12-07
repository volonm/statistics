# Homework Assignment 3
# Volodymyr Lysenko s2880911

import numpy as np
import matplotlib.pyplot as pyplot
from scipy.stats import skew, kurtosis, sem, probplot, chi2, ttest_1samp


def solution_exercise1():
    print("\nExercise 1.0 \n")
    # Calculations using numpy library for first group
    mean_group1 = np.mean(data_group1)
    variance_group1 = np.var(data_group1, ddof=1)
    std_dev_group1 = np.std(data_group1, ddof=1)
    median_group1 = np.median(data_group1)
    sum_group1 = np.percentile(data_group1, [0, 25, 50, 75, 100])
    # Printing values
    print("Data for the Group 1:")
    print(f"Mean : {mean_group1}\nMedian : {median_group1}\n"
          f"Variance : {variance_group1}\nStandard Deviation: {std_dev_group1}")
    print(f"Five-number Summary:\n\tlowest = {sum_group1[0]}, Q1 = {sum_group1[1]}, Q2 = {sum_group1[2]},"
          f"Q3 = {sum_group1[3]}, highest = {sum_group1[4]} ")
    # Calculations using numpy library for second group
    mean_group2 = np.mean(data_group2)
    variance_group2 = np.var(data_group2, ddof=1)
    std_dev_group2 = np.std(data_group2, ddof=1)
    summary_group2 = np.percentile(data_group2, [0, 25, 50, 75, 100])
    median_group2 = np.median(data_group2)
    # Printing Values
    print("\nData for the Group 2:")
    print(f"Mean : {mean_group2}\nMedian = {median_group2}"
          f"\nVariance : {variance_group2}\nStandard Deviation: {std_dev_group2} ")
    print(f"Five-number Summary:\n\tlowest = {summary_group2[0]}, Q1 = {summary_group2[1]}, "
          f"Q2 = {summary_group2[2]}, Q3 = {summary_group2[3]}, highest = {summary_group2[4]} ")


def solution_exercise2():
    print('\nExercise 2.0')
    print('\n Needs to be written!')


def solution_exercise3():
    print('\nExercise 3.0\n')
    # Plot histograms
    pyplot.figure(figsize=(10, 6))
    pyplot.subplot(2, 1, 1)
    pyplot.hist(data_group1, bins='auto', color='blue', alpha=0.7, edgecolor='black', rwidth=0.98)
    pyplot.title('Group 1')
    pyplot.xlabel('Target Selection Speed Data (in ms) for Group 1 with mouse')
    pyplot.ylabel('Number of Kids')

    pyplot.subplot(2, 1, 2)
    pyplot.hist(data_group2, bins='auto', color='red', alpha=0.7, edgecolor='black', rwidth=0.98)
    pyplot.title('Group 2')
    pyplot.xlabel('Target Selection Speed Data (in ms) for Group 2 with joystick')
    pyplot.ylabel('Number of kids')

    pyplot.tight_layout()
    pyplot.show()


def solution_exercise5():
    print("\n Exercise 5.0")

    # Calculate skewness and kurtosis for each group
    skewness_group1 = skew(data_group1)
    kurtosis_group1 = kurtosis(data_group1)
    n = len(data_group1)
    se_skew = ((6 * n * (n - 1)) / ((n - 2) * (n + 1) * (n + 3))) ** 0.5
    se_kurtosis = 2 * se_skew * np.sqrt(((n ** 2) - 1) / ((n - 3) * (n + 5)))

    skewness_group2 = skew(data_group2)
    kurtosis_group2 = kurtosis(data_group2)

    # Print the results
    print("\nGroup 1:")
    print(f"Skewness: {skewness_group1}, Standard Error: {se_skew}")
    print(f"Kurtosis: {kurtosis_group1}, Standard Error: {se_kurtosis}")

    print("\nGroup 2:")
    print(f"Skewness: {skewness_group2}, Standard Error: {se_skew}")
    print(f"Kurtosis: {kurtosis_group2}, Standard Error: {se_kurtosis}")

    # Generate QQ plots
    pyplot.figure(figsize=(12, 6))

    pyplot.subplot(1, 2, 1)
    probplot(data_group1, plot=pyplot, dist='norm', fit=True)
    pyplot.title('Normal QQ Plot for Group 1')

    pyplot.subplot(1, 2, 2)
    probplot(data_group2, plot=pyplot, dist='norm', fit=True)
    pyplot.title('Normal QQ Plot for Group 2')

    pyplot.tight_layout()
    pyplot.show()


def solution_exercise4():
    print("\n Exercise 4.0")
    combined_data = [data_group1, data_group2]
    # Plot combined boxplot
    pyplot.figure(figsize=(8, 6))
    pyplot.boxplot(combined_data, labels=['Group 1', 'Group 2'], patch_artist=True, medianprops={'color': 'black'})
    pyplot.title('Boxplot Comparison: Group 1 vs. Group 2')
    pyplot.xlabel('Groups')
    pyplot.ylabel('Values')
    pyplot.show()


def solution_exercise6():
    print("\n Exercise 6.0")
    # Calculate sample standard deviation and sample size
    sample_std_dev = np.std(data_group1, ddof=1)  # ddof=1 for sample standard deviation
    sample_size = len(data_group1)

    # Degrees of freedom for chi-square distribution
    df = sample_size - 1

    # Chi-square critical values for 99% confidence interval
    chi_lower = chi2.ppf(0.005, df)
    chi_upper = chi2.ppf(0.995, df)

    # Calculate confidence interval
    lower_bound = np.sqrt((df * sample_std_dev ** 2) / chi_upper)
    upper_bound = np.sqrt((df * sample_std_dev ** 2) / chi_lower)

    # Print the results
    print(f"Sample Standard Deviation: {sample_std_dev}")
    print(f"99% Confidence Interval for Standard Deviation (Chi-Square): ({lower_bound}, {upper_bound})")


def solution_exercise7():
    print("\nExercise 7.0\n")
    # Given claim of the producer
    claim_mean = 350

    # Perform one-sample t-test
    t_statistic, p_value = ttest_1samp(data_group2, claim_mean)

    # Print the results
    print(f"Test Statistic: {t_statistic}")
    print(f"P-value: {p_value}")

    # Check if the null hypothesis is rejected
    alpha = 0.05
    if p_value < alpha:
        print("Reject the null hypothesis. There is enough evidence to dispute the claim.")
    else:
        print("Fail to reject the null hypothesis. There is not enough evidence to dispute the claim.")


if __name__ == '__main__':
    print("Statistics homework:\tAssignment 3\nVolodymyr Lysenko s2880911")
    data_group1 = [420, 395, 412, 380, 405, 415, 395, 408, 390, 410,
                   402, 395, 405, 420, 390, 410, 395, 385, 408, 402,
                   415, 400, 420, 390, 405, 410, 415, 395, 402, 410]

    data_group2 = [395, 420, 408, 385, 405, 398, 410, 420, 395, 392,
                   400, 408, 415, 385, 398, 410, 385, 402, 415, 398,
                   405, 390, 402, 410, 395, 420, 392, 385, 400, 415]
    solution_exercise1()
    solution_exercise2()
    # solution_exercise3()
    # solution_exercise4()
    # solution_exercise5()
    solution_exercise6()
    solution_exercise7()
