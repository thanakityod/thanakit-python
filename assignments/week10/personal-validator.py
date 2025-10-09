"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""

print("=== PERSONAL INFORMATION VALIDATOR ===")
name = input("Enter your name:")
age = int(input("Enter your age:"))
phone = input("Enter your phone number:")
 
print("\nValidation Results:")
 
name_validator = True
for char in name:
  for char in name:
   if char.isalpha() == True or char == " ":
     name_validator = True
   else:
    name_validator = False
    break
 
 
age_validator = True
if 18 <= age and age <=65 :
 age_validator = True
else:
  age_validator = False
 
 
phone_validator = True
if len(phone) != 10 :
   phone_validator = False
else :
 for char in phone:
  if char.isdigit() == False:
     phone_validator = False
     break
 
 
if name_validator == True:
  print("Name: Valid (contains only letters and spaces)")
else :
  print("Name: Invalid")
 
 
if age_validator == True:
  print(f"Age: Valid ({age} years old)")
else :
  print("Age: Invalid")
 
 
if phone_validator == True:
  print("Phone: Valid (10-digit number)")
else :
  print("Phone: Invalid")
 
print("\nFormatted Information:")
 
name = name.upper()
print("name: ",name)
 
if age >= 0 and age <= 12:
    print("Age Group: Child (0-12)")
elif age >= 13 and age <=17:
    print("Age Group: Teenager (13-17)")
elif age >= 18 and age <=30:
    print("Age Group: Young Adult (18-30)")
elif age >= 31 and age <=59:
    print("Age Group: Adult (31-59)")
elif age >= 60:
    print("Age Group: Senior(>=60)")
else:
    print("***")
 
print("Phone: +66-",phone)