def main(filename, outname):
    comma = 0
    s = ""
    out = open(outname, "w+")
    for line in open(filename):
        for c in line:
            if(c == "," and comma%2 == 0):
                s += "."
                comma += 1
            elif(c == ","):
                s += ","
                comma += 1
            else:
                s += c

        out.write(s)
        s = ""
        comma = 0
        
main("TiagoCte1.csv", "a.csv")
main("TiagoCte2.csv", "b.csv")
main("TiagoCte3.csv", "c.csv")
