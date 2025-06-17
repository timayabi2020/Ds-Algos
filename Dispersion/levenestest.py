# Levene's statistical test for homogeneity of variance
# This code implements Levene's test to check if multiple groups have equal variances.
from scipy.stats import levene
from scipy.stats import ttest_ind
def levene_test(*args):
    """
    Perform Levene's test for homogeneity of variance.
    
    Parameters:
    *args: Variable number of arrays containing the data for each group.
    Returns:
    tuple: A tuple containing the test statistic and the p-value.
    """
    if len(args) < 2:
        raise ValueError("At least two groups are required for Levene's test.")
    
    # Perform Levene's test
    stat, p_value = levene(*args)
    
    return stat, p_value

# Adding t-test for example usage

def t_test(group1, group2):
    """
    Perform an independent t-test between two groups.

    Parameters:
    group1: First group of data.
    group2: Second group of data.
    Returns:
    tuple: A tuple containing the t-statistic and the p-value.
    """
    if len(group1) == 0 or len(group2) == 0:
        raise ValueError("Both groups must contain data for t-test.")

    # Perform independent t-test
    stat, p_value = ttest_ind(group1, group2)

    return stat, p_value

# Example usage

# Sample data for three groups
group1 = [70, 75, 80, 85, 90]
group2 = [65, 70, 75, 80, 85]
group3 = [60, 65, 70, 75, 80]

# Perform Levene's test
stat, p_value = levene_test(group1, group2, group3)

print("Levene's Test Statistic:", stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Reject the null hypothesis: Variances are not equal.")
else:
    print("Fail to reject the null hypothesis: Variances are equal.")

# Perform t-test between group1 and group2
t_stat, t_p_value = t_test(group1, group2)
print("\nIndependent T-Test between Group 1 and Group 2:")
print("T-statistic:", t_stat)
print("P-value:", t_p_value)
if t_p_value < 0.05:
    print("Reject the null hypothesis: Means are significantly different.")
else:
    print("Fail to reject the null hypothesis: Means are not significantly different.")
