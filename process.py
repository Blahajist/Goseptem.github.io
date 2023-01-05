with open("1.txt", "r") as f:
    for i in f.readlines():
        k = "<tr><td>"
        for j in i:
            if j != ",":
                k += j
            else:
                k += "</td><td>"
        k+="</td><td>10.00</td></tr>"
        print(k)
