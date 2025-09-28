def calculate_percent_reduction(original_value, new_value):
    try:
        # Calculate the percentage reduction
        percent_reduction = ((original_value - new_value) / original_value) * 100
        return percent_reduction
    except ZeroDivisionError:
        # Handle the case where the original_value is 0 to avoid division by zero
        print("Error: Division by zero. Cannot calculate percentage reduction.")
        return None

# Example usage:
original_value = 627
new_value = 501
percent_reduction = calculate_percent_reduction(original_value, new_value)

if percent_reduction is not None:
    print(f"The percent reduction is: {percent_reduction:.2f}%")
else:
    print("Unable to calculate percentage reduction.")
