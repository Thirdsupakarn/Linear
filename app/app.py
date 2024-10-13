import csv
import os

# Define the 11 predefined skills
skills_list = [
    "Active Learning", "Analytical", "Communication", "Complex problem solving",
    "Creativity", "Digital quotience literacy", "Entrepreneurship", "Integrity",
    "Interpersonal Skills", "Leadership", "Resilience"
]

# Function to read the CSV and extract skill data
def read_csv(file_name):
    try:
        # Check if the file exists
        if not os.path.exists(file_name):
            print(f"Error: The file '{file_name}' was not found.")
            return None
        
        # Open and read the CSV file with 'utf-8' encoding; if that fails, try 'ISO-8859-1'
        try:
            with open(file_name, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip header
                programs_data = []
                for row in reader:
                    program_name = row[0]
                    skill_scores = list(map(int, row[1:12]))  # Read scores for 11 skills
                    programs_data.append((program_name, skill_scores))
                return programs_data
        except UnicodeDecodeError:
            print("UTF-8 encoding failed, trying ISO-8859-1 encoding...")
            with open(file_name, newline='', encoding='ISO-8859-1') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip header
                programs_data = []
                for row in reader:
                    program_name = row[0]
                    skill_scores = list(map(int, row[1:12]))  # Read scores for 11 skills
                    programs_data.append((program_name, skill_scores))
                return programs_data
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except IOError:
        print(f"Error: Could not read the file '{file_name}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Function to calculate dot product
def dot_product(vector1, vector2):
    return sum([vector1[i] * vector2[i] for i in range(len(vector1))])

# Function to calculate vector magnitude
def magnitude(vector):
    return sum([x * x for x in vector]) ** 0.5

# Function to calculate cosine similarity
def cosine_similarity(vector1, vector2):
    dot_prod = dot_product(vector1, vector2)
    magnitude1 = magnitude(vector1)
    magnitude2 = magnitude(vector2)
    
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    return dot_prod / (magnitude1 * magnitude2)

# Main function to run the comparison
def main(inp):

    user_vector = inp

    csv_file_name = 'C:\\Users\\T\\sourcecode\\Linear\\app\\skillmapping.csv'  
    programs_data = read_csv(csv_file_name)
    
    if programs_data is None:
        return

    similarities = []
    for program, skill_scores in programs_data:
        similarity = cosine_similarity(user_vector, skill_scores)
        similarities.append((program, similarity))
    
    # Sort programs by highest similarity
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    # Output results
    # print("\nCosine Similarity with Programs:")
    # for program, similarity in similarities:
    #     print(f"{program}: {similarity:.4f}")
    return similarities

# Run the main function
