#!/usr/bin/env python3

import random

# TODO: Add shebang line: #!/usr/bin/env python3
# Assignment 5, Question 2: Python Data Processing
# Process configuration files for data generation.


def parse_config(filepath: str) -> dict:
    """
    Parse config file (key=value format) into dictionary.

    Args:
        filepath: Path to q2_config.txt

    Returns:
        dict: Configuration as key-value pairs

    Example:
        >>> config = parse_config('q2_config.txt')
        >>> config['sample_data_rows']
        '100'
    """
    # TODO: Read file, split on '=', create dict
    config = {}
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("#"):
                if "=" in line:
                    key, value = line.split("=", 1)
                    config[key.strip()] = value.strip()
    return config


def validate_config(config: dict) -> dict:
    """
    Validate configuration values using if/elif/else logic.

    Rules:
    - sample_data_rows must be an int and > 0
    - sample_data_min must be an int and >= 1
    - sample_data_max must be an int and > sample_data_min

    Args:
        config: Configuration dictionary

    Returns:
        dict: Validation results {key: True/False}

    Example:
        >>> config = {'sample_data_rows': '100', 'sample_data_min': '18', 'sample_data_max': '75'}
        >>> results = validate_config(config)
        >>> results['sample_data_rows']
        True
    """
    # TODO: Implement with if/elif/else
    results = {}
    # Validate sample_data_rows int and >0
    if "sample_data_rows" in config:
        try:
            rows = int(config["sample_data_rows"])
            if rows > 0:
                results["sample_data_rows"] = True
            else:
                results["sample_data_rows"] = False
        except ValueError:
            results["sample_data_rows"] = False
        else:
            results["sample_data_rows"] = False

    # Validate sample_data_min
    if "sample_data_min" in config:
        try:
            min_val = int(config["sample_data_min"])
            if min_val >= 1:
                results["sample_data_min"] = True
            else:
                results["sample_data_min"] = False
        except ValueError:
            results["sample_data_min"] = False
        else:
            results["sample_data_min"] = False

    # Validate sample_data_max
    if "sample_data_max" in config:
        try:
            max_val = int(config["sample_data_max"])
            if "sample_data_min" in config:
                try:
                    min_val = int(config["sample_data_min"])
                    if max_val > min_val:
                        results["sample_data_max"] = True
                    else:
                        results["sample_data_max"] = False
                except ValueError:
                    results["sample_data_max"] = False
            else:
                # If min doesn't exist, can't validate max properly
                results["sample_data_max"] = False
        except ValueError:
            results["sample_data_max"] = False
    else:
        results["sample_data_max"] = False

    return results


def generate_sample_data(filename: str, config: dict) -> None:
    """
    Generate a file with random numbers for testing, one number per row with no header.
    Uses config parameters for number of rows and range.

    Args:
        filename: Output filename (e.g., 'sample_data.csv')
        config: Configuration dictionary with sample_data_rows, sample_data_min, sample_data_max

    Returns:
        None: Creates file on disk

    Example:
        >>> config = {'sample_data_rows': '100', 'sample_data_min': '18', 'sample_data_max': '75'}
        >>> generate_sample_data('sample_data.csv', config)
        # Creates file with 100 random numbers between 18-75, one per row
        >>> import random
        >>> random.randint(18, 75)  # Returns random integer between 18-75
    """

    # TODO: Parse config values (convert strings to int)
    num_rows = int(config.get("sample_data_rows"))
    min_val = int(config.get("sample_data_min"))
    max_val = int(config.get("sample_data_max"))

    # TODO: Generate random numbers and save to file
    with open(filename, "w") as file:
        for i in range(num_rows):
            random_num = random.randint(min_val, max_val)
            file.write(f"{random_num}\n")


# TODO: Use random module with config-specified range
config = {
    "sample_data_rows": "100",
    "sample_data_min": "18",
    "sample_data_max": "75",
}
generate_sample_data("output/sample_data.csv", config)


def calculate_statistics(data: list) -> dict:
    """
    Calculate basic statistics.

    Args:
        data: List of numbers

    Returns:
        dict: {mean, median, sum, count}

    Example:
        >>> stats = calculate_statistics([10, 20, 30, 40, 50])
        >>> stats['mean']
        30.0
    """
    # TODO: Calculate stats
    # Count
    count = len(data)
    # Sum
    total = sum(data)
    # Mean
    mean = total / count if count > 0 else 0
    # Median
    sorted_data = sorted(data)
    if count == 0:
        median = 0
    elif count % 2 == 1:  # odd number of elements
        median = sorted_data[count // 2]
    else:  # even number of elements
        mid1 = sorted_data[count // 2 - 1]
        mid2 = sorted_data[count // 2]
        median = (mid1 + mid2) // 2

    return {"mean": mean, "median": median, "sum": total, "count": count}


# Example usage
stats = calculate_statistics([10, 20, 30, 40, 50])
print(stats)
if __name__ == "__main__":
    # TODO: Test your functions with sample data
    # Example:
    # config = parse_config('q2_config.txt')
    config = parse_config("q2_config.txt")
    print("Configuration loaded:")
    print(config)
    print()
    # validation = validate_config(config)
    validation = validate_config(config)
    if all(validation.values()):
        print("Configuration is valid! Generating sample data...")
        # generate_sample_data('data/sample_data.csv', config)
        generate_sample_data("data/sample_data.csv", config)
        print("Sample data generated in data/sample_data.csv")
        print()

    # TODO: Read the generated file and calculate statistics
    data = []
    with open("data/sample_data.csv", "r") as file:
        for line in file:
            data.append(int(line.strip()))
    print(f"Read {len(data)} numbers from sample_data.csv")
    print()
    # Calculate statistics
    stats = calculate_statistics(data)
    print("Statistics calculated:")
    print(stats)
    print()
    # TODO: Save statistics to output/statistics.txt
    with open("output/statistics.txt", "w") as file:
        file.write("Sample Data Statistics\n")
        file.write("=" * 30 + "\n")
        file.write(f"Count: {stats['count']}\n")
        file.write(f"Sum: {stats['sum']}\n")
        file.write(f"Mean: {stats['mean']: .2f}\n")
        file.write(f"Median: {stats['median']: .2f}\n")
        print("Statistics saved to output/statistics.txt")
else:
    print("Validation failed! Please check configuration values.")
    print("Failed validations:", [k for k, v in validation.items() if not v])
