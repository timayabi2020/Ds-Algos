# Levene's statistical test for homogeneity of variance
# This code implements Levene's test to check if multiple groups have equal variances.
from scipy.stats import levene
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
