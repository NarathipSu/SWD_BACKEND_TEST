
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""


def roman(num: int) -> str:

    chlist = "VXLCDM"
    rev = [int(ch) for ch in reversed(str(num))]
    chlist = ["I"] + [chlist[i % len(chlist)] + "\u0304" * (i // len(chlist))
                      for i in range(0, len(rev) * 2)]

    def period(p: int, ten: str, five: str, one: str) -> str:
        if p == 9:
            return one + ten
        elif p >= 5:
            return five + one * (p - 5)
        elif p == 4:
            return one + five
        else:
            return one * p

    return "".join(reversed([period(rev[i], chlist[i * 2 + 2], chlist[i * 2 + 1], chlist[i * 2])
                            for i in range(0, len(rev))]))


while True:
    number = int(input("Enter number:"))

    if number < 1 or number > 1000:
        print("ตัวเลขต้องมีค่ามากกว่า 0 จนถึง 1000")
    else:
        print(roman(number))

    end = input("Enter to continue or \"n\" to close:")

    if end == "n":
        break
