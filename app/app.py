import os
import csv
import numpy as np

# Function to read the CSV and extract skill data
def read_csv(file_name):
    try:
        if not os.path.exists(file_name):
            print(f"Error: The file '{file_name}' was not found.")
            return None
        
        try:
            with open(file_name, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip header
                programs_data = []
                for row in reader:
                    program_name = row[0]
                    skill_scores = np.array(list(map(int, row[1:12])))  # Convert to numpy array
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
                    skill_scores = np.array(list(map(int, row[1:12])))  # Convert to numpy array
                    programs_data.append((program_name, skill_scores))
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
    return dot_prod / (magnitude1 * magnitude2)

# Main function to run the comparison
def main(inp):
    user_vector = np.array(inp)  # Convert user input to numpy array
    csv_file_name = r'C:\Users\T\sourcecode\Linear\app\skillmapping.csv'  # Use raw string for Windows path
    programs_data = read_csv(csv_file_name)
    
    if programs_data is None:
        return "No data found or file read error"

    similarities = []
    for program, skill_scores in programs_data:
        similarity = float(cosine_similarity(user_vector, skill_scores))  # Cast to native float
        similarities.append((program, similarity))

    # Return sorted similarities as a dictionary
    return dict(sorted(similarities, key=lambda x: x[1], reverse=True))

