import matplotlib.pyplot as plt

abhishek_marks = [45,20,60,55,78,40]
rahul_marks = [45,30,78,90,20,10]
plt.plot([1,2,3,4,5,6],abhishek_marks)
plt.plot([1,2,3,4,5,6],rahul_marks)

plt.title('marks')
plt.xlabel('subject')
plt.ylabel('marks')
plt.grid()
for x,y in enumerate(abhishek_marks,1):
    plt.text(x,y,str(y))


plt.axhline(y=40, color='green')
plt.legend(['abhishek','rahul'])
plt.xticks(range(1,7),['english','math','computer','dbms','ai','design'])

plt.show()