#!/usr/bin/env python3
import json
import random

def randomize_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Randomize question order
    random.shuffle(data)
    
    # Reassign sequential IDs
    for i, question in enumerate(data, 1):
        question['id'] = i
    
    # Randomize answer options and update correct indices
    for question in data:
        if 'options' in question and 'correct' in question:
            options = question['options']
            correct_indices = question['correct']
            
            # Create mapping of old index to new index
            old_to_new = list(range(len(options)))
            random.shuffle(old_to_new)
            
            # Reorder options
            new_options = [options[i] for i in old_to_new]
            
            # Update correct indices
            new_correct = []
            for old_idx in correct_indices:
                new_idx = old_to_new.index(old_idx)
                new_correct.append(new_idx)
            
            question['options'] = new_options
            question['correct'] = sorted(new_correct)
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"Randomized {len(data)} questions and their answers")

if __name__ == "__main__":
    randomize_data("/Users/hungtn/Desktop/aws-certificates/AWS Dump/AWS DevOps Profestional/final_repo/apps/data.json")
