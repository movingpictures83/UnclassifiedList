import sys
import PyPluMA

class UnclassifiedListPlugin:
    def input(self, filename):
        self.kronafiles = []
        myfile = open(filename, 'r')
        for line in myfile:
            self.kronafiles.append(line.strip())

    def run(self):
       self.unclass = set()
       for mydir in self.kronafiles:
         infile = open(PyPluMA.prefix()+"/"+mydir)
         for line in infile:
           contents = line.strip().split('\t')
           for i in range(len(contents)):
               if ("unclassified" in contents[i] or "Sedis" in contents[i] or "sedis" in contents[i]):
                   self.unclass.add(contents[i])

    def output(self, filename):
       txtfile = open(filename, 'w')
       for unc in self.unclass:
          txtfile.write(unc+"\n")
