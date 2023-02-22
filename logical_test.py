
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""


class NumThai:

    def __init__(self):

        self.number = None
        self.num_text = {
            '-': "ลบ", '.': "จุด", 0: "ศูนย์", 1: "หนึ่ง",
            2: "สอง", 3: "สาม", 4: "สี่", 5: "ห้า",
            6: "หก", 7: "เจ็ด", 8: "แปด", 9: "เก้า",
            "0": "", "1": "สิบ", "2": "ร้อย", "3": "พัน",
            "4": "หมื่น", "5": "แสน", "6": "ล้าน"
        }

    def process_int(self):
        result = []
        le = len(str(self.number))
        val = self.num_text['6']
        i = 0

        for x in range(0, le):
            n = int(self.number % 10)
            self.number /= 10

            if le > 1:
                if x >= 1 and x % 6 == 0:
                    if n == 1 and le < 8:
                        result.append(self.num_text[n]+val)
                    elif n == 1 and le > 7:
                        result.append("เอ็ด"+val)
                    else:
                        if n != 0:
                            result.append(self.num_text[n]+val)
                        else:
                            result.append(val)

                elif x == 0 and n == 1:
                    result.append("เอ็ด")
                else:
                    if i == 1 and n == 1:
                        result.append(self.num_text[str(i)])
                    elif i == 1 and n == 2:
                        result.append("ยี่"+self.num_text[str(i)])
                    elif n == 0:
                        pass
                    else:
                        result.append(self.num_text[n]+self.num_text[str(i)])
            else:
                result.append(self.num_text[n])

            if i > 5:
                val += val
                i = 0
            i += 1

        return list(reversed(result))

    def NumberToTextThai(self, number):

        result = []
        fnumber = 0

        if type(number) not in [int, float]:

            raise TypeError("ใส่ตัวเลขเท่านั้น")

        # if len(str(abs(number))) === 8

        if len(str(abs(number))) > 8 or len(str(abs(number))) < 1 or number < 0 or number > 10000000:

            raise ValueError(
                "ตัวเลขที่ใส่จะต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน")

        if type(number) in [int]:
            self.number = number

        result.extend(self.process_int())

        if fnumber > 0:
            str1 = str(fnumber)
            for i in range(1, len(str1)):
                if str1[i] == '.':
                    result.append(self.num_text[str1[i]])
                else:
                    result.append(self.num_text[int(str1[i])])

        return result


while True:
    number = int(input("Enter number:"))

    n = NumThai().NumberToTextThai(number)

    for x in n:
        print(x, end="")

    end = input("\nEnter to continue or \"n\" to close:")

    if end == "n":
        break
