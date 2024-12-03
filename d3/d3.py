import re

pattern = r"\(-?\d+,-?\d+\)"

# Example usage
text = "Here are some pairs: (1,2), (-5,10), (123, -456)"
matches = re.findall(pattern, text)

print(matches)
