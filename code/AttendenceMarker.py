# function to mark attendance of students by taking name as input
def mark_attendance(name):
    from datetime import datetime
    print(f'marking attendance for {name}')
    with open("C:\\Users\\charanreddy\\PycharmProjects\\labproject\\attendence\\count.csv", 'r+') as f:
        my_data = f.readlines()
        namelist = []
        for line in my_data:
            entry = line.split(',')
            namelist.append(entry[0])
        # checking whether already present or not
        if name not in namelist:
            here = datetime.now()
            current = here.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{current}')
