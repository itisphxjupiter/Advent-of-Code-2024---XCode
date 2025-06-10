import math


def is_safe_report(report):
    """Checks if a list of numbers is a safe red-nosed report, allowing one bad level to be ignored (Problem Dampener)."""

    def check_safe(r):
        # Check for increasing order
        is_increasing = all(r[i] <= r[i+1] for i in range(len(r) - 1))
        # Check for decreasing order
        is_decreasing = all(r[i] >= r[i+1] for i in range(len(r) - 1))
        # If not increasing or decreasing, it's not safe
        if not (is_increasing or is_decreasing):
            return False
        # Check differences for increasing order
        if is_increasing:
            return all(1 <= r[i+1] - r[i] <= 3 for i in range(len(r) - 1))
        # Check differences for decreasing order
        if is_decreasing:
            return all(1 <= r[i] - r[i+1] <= 3 for i in range(len(r) - 1))

    if check_safe(report):
        return True
    # Try removing each element once (Problem Dampener)
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if check_safe(new_report):
            return True
    return False


safe = 0
unsafe = 0

with open("/Volumes/nas/VSCode/Advent-of-Code-2024---XCode/Day2/day2-input.md") as f:
    for line in f:
        numbers = [int(x) for x in line.strip().split()]  # adjust parsing as needed
        print(is_safe_report(numbers))
        if is_safe_report(numbers):
            safe = safe + 1
        else:
            unsafe = unsafe + 1


print("The safe ones are:" + str(safe))


