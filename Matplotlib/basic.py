import matplotlib.pyplot as plt
import pandas as pd

data = {
    "name": ["A", "B", "C"],
    "marks": [70, 85, 90]
}

df = pd.DataFrame(data)

plt.bar(df["name"], df["marks"])

plt.show()
# x = [1,2,3,4]
# y = [10,20,30,40]
# plt.plot(x,y)
# plt.show()

hours = [1,2,3,4]
marks = [40,50,70,90]
# plt.plot(hours, marks)
# plt.title("Student Marks")
# plt.xlabel("Hours")
# plt.ylabel("Marks")
# plt.show()


# students = ["A", "B", "C"]
# marks = [70, 85, 90]
# plt.bar(students, marks)
# plt.show()
