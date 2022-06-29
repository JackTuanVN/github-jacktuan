# thong_tin = {"chieu_cao": 1.7 , "can_nang": 54}
# hoc_luc = "gioi"
# print(str(thong_tin['chieu_cao']) + '\t' + hoc_luc)
# if hoc_luc != 'gioi':
#     print("chua dat")
# else:
#     print("dat")
# print(10**3)
# def from pip import main
def cToFConvert():
    cTemp = input("C: ")
    if cTemp:
        cTemp = float(cTemp)
        fTemp = 9*cTemp/5 + 32

        print(f"{cTemp}C is converted to {fTemp}F")
def main():
    # print("hello world")
    cToFConvert()
if __name__ == "__main__":
    main()