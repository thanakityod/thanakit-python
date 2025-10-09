"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""

def get_temperatures():
    temperature = [32,34,2,31,32,33,4,29,1,31]
    return temperature
 
def analyze_temps(temp_list):
    sum = 0
    for temp in temp_list:
        sum = sum + temp
        average_temp = sum / len(temp_list)
        high_temp = max(temp_list)
        low_temp = min(temp_list)
        return (average_temp, high_temp, low_temp)
 
def display_analysis(avg,high,low):
    print("Temperature Analysis for the Week : ")
    print("Acerage ", avg, "C")
    print(f"Highest : {high} C")
    print("Lower %.1f C" % (low))
 
my_temp = get_temperatures()
analyzed_temp = analyze_temps(my_temp)
display_analysis(analyzed_temp[0], analyzed_temp[1], analyzed_temp[2])    