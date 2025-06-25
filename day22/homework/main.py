#2) ჩამოწერეთ პირობითი განცხადებების შემადგენელი ყველა Keyword-ი, თითოეულს თან დაურთეთ განმარტება და თქვენი სიტყვებით ახსენით თუ რატომ/რა შემთხვევებში არის elif keyword-ი საჭირო.

#3) ცვლადში შეინახეთ თქვენი ასაკი. შემდეგ მომხმარებელს შემოატანინეთ თავისი ასაკი. თუ თქვენი გვარები დაემთხვევა გამოიტანეთ "We are the same age", სხვა შემთხვევაში - "We are not the same age".

#4) დააკვირდით მოცემულ flowchart-ს, ახსენით მისი მუშაობის პრინციპი. მისი მიხედვით Vscode-ში დაწერეთ პროგრამა და აღწერეთ რა შედეგს გამოიტანს კოდი იმ შემთხვევაში, როდესაც მომხმარებელი არის 14 წლის და არ არის სტუდენტი.

#my_age=17
#user_age=int(input("Enter your age: "))
#if my_age == user_age:
#    print("We are the same age")
#elif my_age < user_age:
#   print("We are not the same age")

#age=int(input("Enter your age :"))
#if age < 18:
#    print("you are a student and you get 20 percent discount")
#elif age > 18:
#    print("your an adult and you pay the regular price")
#else:
#    print("or u get a 10 percent discount ")



required_number=20
user_number=int(input("Enter required number :"))
if required_number !=user_number:
    print("Incorect you must write  right required number")
elif required_number == user_number:
    print("Correct u wrote the right number!")