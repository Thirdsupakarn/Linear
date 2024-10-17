import os
import csv
import numpy as np

# Define the 11 predefined skills
skills_list = [
    "Active Learning", "Analytical", "Communication", "Complex problem solving",
    "Creativity", "Digital quotience literacy", "Entrepreneurship", "Integrity",
    "Interpersonal Skills", "Leadership", "Resilience"
]

# Function to read the CSV and extract skill data
def read_csv(file_name):
    try:
        if not os.path.exists(file_name):
            print(f"Error: The file '{file_name}' was not found.")
            return None
        
        programs_data = {}
        
        with open(file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header
            for row in reader:
                program_name = row[0]
                skill_scores = np.array(list(map(int, row[1:12])))  # Convert to numpy array
                
                if program_name not in programs_data:
                    programs_data[program_name] = []
                programs_data[program_name].append(skill_scores)
                
        return programs_data
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except IOError:
        print(f"Error: Could not read the file '{file_name}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Function to calculate cosine similarity using numpy
def cosine_similarity(vector1, vector2):
    dot_prod = np.dot(vector1, vector2)
    magnitude1 = np.linalg.norm(vector1)
    magnitude2 = np.linalg.norm(vector2)
    
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    cosine = dot_prod / (magnitude1 * magnitude2)
    return cosine * (min(magnitude1,magnitude2)/max(magnitude1,magnitude2))

# Main function to run the comparison
def main(inp):
    user_vector = np.array(inp)  # Convert user input to numpy array
    csv_file_name = r'C:\Users\T\sourcecode\Linear\app\skill mapping kmitl.csv' 
    programs_data = read_csv(csv_file_name)
    
    if programs_data is None:
        return "No data found or file read error"

    # for i in programs_data:
    #     print(i)
    # Calculate average skill scores for each program
    average_programs = {}
    for program, scores in programs_data.items():
        # Stack all the skill scores for a program and calculate the mean across rows
        average_scores = np.mean(scores, axis=0)  # Average skill scores for all instances of the same program
        average_programs[program] = average_scores

    # Calculate similarity to the user's input
    similarities = []
    for program, avg_scores in average_programs.items():
        # print(program, avg_scores)
        similarity = float(cosine_similarity(user_vector, avg_scores))  # Cast to native float
        similarities.append((program, similarity))
    
    # Return sorted similarities as a dictionary
    return dict(sorted(similarities, key=lambda x: x[1], reverse=True))

# Convert input to a list of integers or floats
# x = list(map(int, input("Enter your skill scores separated by space: ").split()))  # Assuming integers
# temp = main(x)
# print(temp)
# # # print(main(x))
# # for i in temp:
# #     print(i)
