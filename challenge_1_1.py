# Challenge 1.1
def solution(area):
    list = []
    def square(area):
        if area != 0:
            whole = int(area**0.5)
            list.append(whole**2)
            new_area = area - whole**2
            square(new_area)
        else:
             print(", ".join(map(str, list)))
    square(area)