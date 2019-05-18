import sys

phone_directory = {
                   'ankit':['Ankit Chaubey','ankit.chaubey@gmail.com','886-037-9656'],
                   'amit':['Amit Singh','amit.singh@gmail.com','886-067-9651'],
                   'kushagra':['Kushagra Sharma','ksharma@gmail.com','881-035-9116'],
                   'nasik':['Nasik Mehto','nmehto@gmail.com','811-032-9696'],
                   'vimal':['Vimal Jain','vimal.jain@gmail.com','811-907-1156'],
                   'rahul':['Rahul Kishan','r.kishan@gmail.com','833-041-4556'],
                   'Jai':['Jai Yadav','j.yadav@gmail.com','800-013-9600'],
                   'Vimal':['Vimal Dogra','v.dogra@gmail.com','811-000-1111']
                   }

i = int(input("Enter 0 for name,1 for email, 2 for phone number and anything else for complete details:  "))
name = input("Enter the name for which you need the record: ")

try:
    if i == 0 or i == 1 or i == 2:
        print("The detail you required is {}", phone_directory[name][i])
    else:
        print("let me me help you with all I have for {}, here you go...... {}", phone_directory[name])
except KeyError as e:
    print("Please enter a valid name")
