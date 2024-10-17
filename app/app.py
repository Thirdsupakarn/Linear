import os
import csv
import numpy as np

def read_csv(file_name):
    try:
        if not os.path.exists(file_name):
            print(f"Error: The file '{file_name}' was not found.")
            return None
        
        programs_data = {}
        
        with open(file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                program_name = row[0]
                skill_scores = np.array(list(map(int, row[1:12])))
                
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

def cosine_similarity(vector1, vector2):
    dot_prod = np.dot(vector1, vector2)
    magnitude1 = np.linalg.norm(vector1)
    magnitude2 = np.linalg.norm(vector2)
    
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    cosine = dot_prod / (magnitude1 * magnitude2)
    return cosine * (min(magnitude1,magnitude2)/max(magnitude1,magnitude2))

def main(inp):
    user_vector = np.array(inp) 
    csv_file_name = r'C:\Users\T\sourcecode\Linear\app\skill mapping kmitl.csv' 
    programs_data = read_csv(csv_file_name)
    
    if programs_data is None:
        return "No data found or file read error"

    average_programs = {}
    for program, scores in programs_data.items():

        average_scores = np.mean(scores, axis=0)  
        average_programs[program] = average_scores

    similarities = []
    for program, avg_scores in average_programs.items():

        similarity = float(cosine_similarity(user_vector, avg_scores)) 
        similarities.append((program, similarity))
    

    return dict(sorted(similarities, key=lambda x: x[1], reverse=True))
