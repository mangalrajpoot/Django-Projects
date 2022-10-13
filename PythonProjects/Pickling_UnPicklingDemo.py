import pickle, StudentDemo
with open("Student.dat",mode='wb') as f:
    stud1 = StudentDemo.Student("Rahul Sharma",101,"BCA",34567.34)
    stud2 = StudentDemo.Student("Neha Sharma",102,"MCA",45678.45)
    pickle.dump(stud1,f)
    pickle.dump(stud2,f)
    print("Pickling Done!!")

with open("Student.dat",mode='rb') as f:
    obj1=pickle.load(f)
    obj2=pickle.load(f)
    print("UnPickling Done!!")
    obj1.display()
    obj2.display()