def get_marks():
    marks = []
    while True:
        entry = input("Enter student mark").strip()
        if entry.lower() == 'done':
            break
        elif entry.lower() == 'absent':
            marks.append(None)
        else:
            try:
                mark = float(entry)
                marks.append(mark)
            except ValueError:
                print("Invalid input. Please enter a numeric mark ")
    return marks

def average_score(marks):
    total = 0
    count = 0
    
    for mark in marks:
        if mark is not None:  
            total += mark  
            count += 1  
    
    if count == 0:  
        return 0  
    
    return total / count  
    
    
def highest_lowest_score(marks):
    highest = None
    lowest = None

    for mark in marks:
        if mark is not None:
            if highest is None or mark > highest:
                highest = mark
            if lowest is None or mark < lowest:
                lowest = mark

    return highest, lowest
    
def count_absent(marks):
    count = 0
    
    for mark in marks:
        if mark is None:
            count += 1
            
    return count


def mark_with_highest_frequency(marks):
    
    frequency = {}
    for mark in marks:
        if mark is not None:
            if mark in frequency:
                frequency[mark] += 1
          
            else:
                frequency[mark] = 1

   
    most_frequent_mark = None
    max_frequency = 0

    
    for mark, count in frequency.items():
        if count > max_frequency:
            max_frequency = count
            most_frequent_mark = mark

   
    return most_frequent_mark
def main():
      print("Welcome to DSA1 ASS System")
      marks = get_marks()
      for i in range(len(marks)):
        print(marks[i])
      avg_marks=average_score(marks)
      print(avg_marks)
      
      hig,low=highest_lowest_score(marks)
      print(hig,low)
      
      absent_count = count_absent(marks)
      print(absent_count)
      
      most_frequent_mark = mark_with_highest_frequency(marks)
      print(f"Highest Frequency: {most_frequent_mark}")
      

if __name__ == "__main__":
    main()
