import random
import time

names = [
    "ნუკი გაგნიძე",
    "გიორგი ყორანაშვილი",
    "იოანე ჯიშკარიანი",
    "თიკა ქათამაძე",
    "ლილე ძნელაძე",
    "ანდრია მაღლაფერიძე",
    "ზაზა ბორისოვი",
    "ნანუკა დეკანოსიძე",
    "ნიკოლოზ ცაავა",
    "ირაკლი გერაძე",
    "ნიკოლოზ ნადირაძე",
    "გაბრიელ თორია",
    "მირანდა ჯინჭარაძე "
]

lucky_controllers = []
def get_cont(ls):
    new_cont = random.choice(ls)
    ls.remove(new_cont)

    lucky_controllers.append(new_cont)

for _ in range(3):
    wait_time = random.randint(1, 5)
    time.sleep(wait_time) 
    
    get_cont(names)
    print(f"\n{"-"*(len(lucky_controllers[-1])+16)}\n\nNew controller: {lucky_controllers[-1]}\n\n{"-"*(len(lucky_controllers[-1])+16)}\n")