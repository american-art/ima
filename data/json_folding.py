__author__ = 'nilay'

import json

class JF(object):
    def __init__(self):
        self.name = "JSON Folding"
        self.threshold = 20
        
    @staticmethod
    def preprocess(self,jsonobject):
        """Check if JSON level 2 objects and below contain more dictionaries than threshold.
        Fold them as an array by adding new key value pair: "key":<actual key from unfolded json>."""
        
        foldedJson = {}
        
        for key in jsonobject.keys():
            # Process only if dictionary value is also json 
            if type(jsonobject[key]) == dict:
                # Process only if there are more than threshold objects
                if len(jsonobject[key].keys()) > self.threshold:
                    #print len(jsonobject[key].keys())
                    foldedData = []
                    # Create array out of long dictionary object
                    for innerkey in jsonobject[key].keys():
                        innerdict = jsonobject[key][innerkey]
                        innerdict.update({"unfoldedKey":innerkey})
                        foldedData.append(innerdict)
                    foldedJson[key] = foldedData
                else:
                    foldedJson[key] = jsonobject[key]
            else:
                foldedJson[key] = jsonobject[key]
        return foldedJson

def main():

    jsonfilename = "aac-objects"
    jsonobject = json.load(open(jsonfilename+'.json','r'))
    jppInstance = JF()
    jsondata = JF.preprocess(jppInstance,jsonobject)
    json.dump(jsondata, open(jsonfilename+'_folded.json','w'),indent=4)
    
if __name__ == "__main__":
    main()