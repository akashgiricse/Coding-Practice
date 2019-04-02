points = {'A+':4.0, 'A':4.0, 'A-':3.67,
          'B+':3.33, 'B':3.0, 'B-':2.67,
          }

num_course = 0
total_point = 0

done = False

while not done:
    grade = input()
    if grade == '':
        done = True
    elif grade not in points:
        print("Unknown grade '{0}' being ignored".format(grade))
    else:
        num_course += 1
        total_point += points[grade]

if num_course > 0:
    print('Your GPA is {0:.3}'.format(total_point/num_course))
