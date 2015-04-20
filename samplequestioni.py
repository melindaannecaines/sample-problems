#Python 3.1.2
#Goal:Print a  list of phone numbers from an XML file


for line in open('contacts.xml').readlines():
    if "phone" in line:
        
        new = line.split('<phone>')
        
        newnew = new[1].split('</phone>')
        print (newnew[0])
