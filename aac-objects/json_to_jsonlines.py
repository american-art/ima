__author__ = 'nilay'

import json

class JL(object):
    def __init__(self):
        self.name = "Coverting from Json to JsonLines"
        
    @staticmethod
    def convert(self,jsonobject,jsonfilename):
        """Find data array and iterate one by one and dump it to new json lines file"""
        
        out = open(jsonfilename+'_jsonlines.json','w')
        
        for datasample in jsonobject['data']:
            temp = {"count":1, "data":[datasample]}
            out.write(json.dumps(temp))
            out.write("\n")

def main():

    jsonfilename = "aac-objects_folded"
    jsonobject = json.load(open(jsonfilename+'.json','r'))
    jlInstance = JL()
    JL.convert(jlInstance,jsonobject,jsonfilename)
    
if __name__ == "__main__":
    main()