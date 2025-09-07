"""Any intelligent fool can make things bigger and more complex. It takes a touch of genius - and a lot of courage to move in the opposite direction."""
# E. F. Schumacher


import numpy as np
import webbrowser

# 17 goals
goals ="""
1  | No Poverty
2  | Zero Hunger
3  | Good Health and Well-being
4  | Quality Education
5  | Gender Equality
6  | Clean Water and Sanitation
7  | Affordable and Clean Energy
8  | Decent Jobs and Economic Growth
9  | Industry, Innovation and Infrastructure
10 | Reduced Inequalities
11 | Sustainable Cities and Communities
12 | Responsible Consumption and Production
13 | Climate Action
14 | Life below Water
15 | Life on Land
16 | Peace and Justice - Strong Institutions
17 | Partnerships for the Goals
"""

print("Welcome to Ideate. The choices for this session are: ")
print(goals)

num = input('Enter the number of people who want to participate in this brainstorming: ')
num = int(num)

# order of merit or borda count method

def normalize(ch):
    r = np.zeros(17, int)
    size = len(ch)
    for i, e in enumerate(ch):
        r[e-1] += (size-i)
    return r

pooled_scores = np.zeros(17, int)

for i in range(num):
    choice = input(f'Enter top 5 choices of user#{i+1} seperated by space ')
    choice = list(map(int, choice.split()))
    t = normalize(choice)
    pooled_scores += t

top_choice = i = np.argmax(pooled_scores) + 1

print('\nYour top goal based on this voting is: ', top_choice)

print('Here are some resources for you:')
print('1. https://sdgs.un.org/goals/goal'+str(i))
print('2. https://unstats.un.org/sdgs/report/2025/The-Sustainable-Development-Goals-Report-2025.pdf')
print('3. How does this voting work: https://en.wikipedia.org/wiki/Borda_count\n')


p = input('Press 1 to see the websites. ')

if p == '1':

    webbrowser.open_new_tab('https://unstats.un.org/sdgs/report/2025/The-Sustainable-Development-Goals-Report-2025.pdf')
    webbrowser.open_new_tab('https://sdgs.un.org/goals/goal'+str(i))

    if i==2:
        webbrowser.open_new_tab('https://sdgs.un.org/sites/default/files/2023-08/SDG_report_2023_infographics_Goal%202.jpg')
    
    elif i==15:
        webbrowser.open_new_tab('https://sdgs.un.org/sites/default/files/2025-07/2025_SDG_Goal-Level_Social_Media_Cards_Goal_15_-_1_small.png')
    
    else:
        webbrowser.open_new_tab('https://sdgs.un.org/sites/default/files/2025-07/2025_SDG_Goal-Level_Social_Media_Cards_Goal_'+str(i)+'_small.png')

print('Session complete. Bye now!')
