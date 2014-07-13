import glob

class Highscore:

    def __init__(self):
        self.list1 = []
        #if the file doesn't exist
        if not glob.glob("score.csv"):
            return
        d=open("score.csv")
        line=d.readline()
        while(line):
            part = line.split(";")
            name = part[0]
            time = part[1][0:len(part[1])-1]
            time = time.replace(",",".")
            self.list1.append([name,float(time)])
            line = d.readline()
        d.close()


    

    def change(self,name,time):
            
        found = False
            
                             
        for i in range(len(self.list1)):
                
            if time < self.list1[i][1]:
                
                self.list1.insert(i,[name, time])
                found = True
                break

        if not found:
            self.list1.append([name,time])
 


    def save(self,name,time):

        self.change(name,time)
        d=open("score.csv","w")
        for element in self.list1:
            name = element[0]
            time = str(element[1]).replace(".",",")
            d.write(name + ";"+time+"\n")
        d.close()


    def __str__(self):
        
        if not self.list1:
            return "No highscore available"

        output ="P. Player      Time\n"
           
        for i in range(len(self.list1)):
            output += "{0:2d}. {1:10} {2:5.2f} sec\n".\
                    format(i+1,self.list1[i][0],self.list1[i][1])

            if i >= 9:
                break
        return output
