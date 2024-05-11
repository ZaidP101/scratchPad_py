#####class Employee:
#     def Details(self):
#         self.name = input("Employee Name: ")
#         self.id = int(input("Employee ID: "))
#         self.salary = int(input("salary of the employee : "))

#     def Display(self):
#         print("the Name of the Employee is : ", self.name)
#         print("the ID of the Employee is : ", self.id)
#         print("the Salary of the Employee is : ", self.salary)

# New = Employee()
# New.Details()
# New.Display()



###class Car:
#     def Details(self):
#         self.Colour = input("Colour of the car ? ")
#         self.seats = int(input("car type : 1) Suv / 2) Sidan "))
#
#     def Display(self):
#         print("the colour of the car is :", self.Colour)
#         if (self.seats == 1):
#             print("the number of seats are: 4\n the type is SUV\n Total fair = ", 4*10)
#         else:
#             print("the number of seats are : 6\n the type is Sidan\n Total fair = ", 6*10)
#
#
#
# vehical = Car()
# vehical.Details()
# vehical.Display()


######Double the number in a list
# 1) Numbers = [1,2,3,4,5,6,7,8,9,10]
# for num in Numbers:
    # num= num*2
    # print(num)

# 2) 
# def Double(numbers):
#     result = []
#     for num in numbers:
#         print(result)
#         result.append(num * 2)
#     return result

# print(Double([1,2,3,4]))


#####count the words 
# def count_words():
#     phrase = input("give a phrase : ")
#     print("the total words in the phrase are :", len(phrase.split()))

# count_words()



###### total of all in list
# 1)
# total = [10,20,30,40]
# count = 0 
# for num in total:
#      count += num
     
# print(count)


# 2)     
# def t_count(numbers):
#      count = 0
#      for num in numbers:
#           count += num
   
   
#      return count

# print(t_count([20,30,40,10]))

#######find max in list
# def F_max(numbers):
#     big = numbers[0]
#     for num in numbers:
#         if num > big:
#             big = num
#     return big 


# print(F_max([30,20,3,40,5,1]))

#####count the frequency of word in Dictionary
# def w_frequency(phrase):
#     result = {}
#     words = phrase.split()
#     for word in words:
#        if word not in result:
#          result[word] = 1
#        else:
#         result[word] +=1
#     return result

# print(w_frequency("The cat chased the cat around the tree while the cat watched from the tree"))

#####loops#####
#i =1
#while i < 6:
#    print(i)
#    if i == 3:
#        break
#    i += 1


    
