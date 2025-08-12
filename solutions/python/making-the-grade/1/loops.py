def round_scores(student_scores):
    new_list=[]
    for scores in student_scores:
        new_list.append(round(scores))
    return new_list
def count_failed_students(student_scores):
    count=0
    for i in student_scores:
        if i<=40:
            count+=1
    return count
def above_threshold(student_scores, threshold):
    new_list=[]
    for i in student_scores:
        if i>=threshold:
            new_list.append(i)
    return new_list
def letter_grades(highest):
    new_list=[]
    step=int((highest-40)/4)
    for i in range(41,highest,step):
        new_list.append(i)
    return new_list
def student_ranking(student_scores, student_names):
    new_list=[]
    for i,value in enumerate(student_names):
        temp=''
        temp=str(i+1) + '. ' + value + ': ' + str(student_scores[i])
        new_list.append(temp)
    return new_list
def perfect_score(student_info):
    for i in student_info:
        if i[1]==100:
            return i
    return []
        