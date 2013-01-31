#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kevin
#
# Created:     14/01/2013
#-------------------------------------------------------------------------------
#!/usr/bin/env python

class Record(object):
    #pre: 6 variables are passed
    #post: a record with 6 categories are created
    #purpose: create a record
    def __init__(self, **kwargs ):
        #with(self):
            self.fname= kwargs.pop('fname', "")
            self.lname= kwargs.pop('lname', "")
            self.position= kwargs.pop('position', "")
            self.salary= kwargs.pop('salary', "")
            self.credit= kwargs.pop('credit', "")
            self.id= kwargs.pop('id', -1)
            self._extra = kwargs


class Data(object):

    _recs = []

    #pre: a record is passed
    #post: a recod is added to the
    #purpose: to create a new record
    def add(self,r):
        self._recs.append(r)




    #pre: a key and a value are passed and must be valid
    #post: a certain record is deleted from the list
    #purpose: to delete a record
    def delete(self, key, value):
        index=self.search(key, value)
        del self._recs[index]


    #pre: a key and a value are passed and must be valid
    #post: return the index of the record in the list
    #purpose: to search for a certain record
    def search(self, key, value):
        for i in range(0, len(self._recs), 1):
            #hasattr(obj, attr_name)
            #getattr(obj, attr_name)
            #if key in dictionary
            if key=="fname" and self._recs[i].fname==value:
                return i
            elif(key=="lname" and self._recs[i].lname==value):
                return i
            elif(key=="position" and self._recs[i].position==value):
                return i
            elif(key=="salary" and self._recs[i].salary==value):
                return i
            elif(key=="credit" and self._recs[i].credit==value):
                return i
            elif(key=="id" and self._recs[i].id==value):
                return i



    #pre: no pre condition
    #post: print all records
    #purpose: to show all records
    def showall(self):
        for i in range(0, len(self._recs), 1):
            index=i
            s= self._recs[index].fname,self._recs[index].lname,self._recs[index].position,self._recs[index].salary,self._recs[index].credit,self._recs[index].id,self._recs[index]._extra
            print s


    #pre:
    #post:
    #purpose:
    def splice(self):
        pass

    # pre: a key and a value are passed and must be valid
    # post: return a string that represent the record
    # purpose: to convert the a record to string
    def serialize(self, key, value):
        index=self.search(key, value)
        s= self._recs[index].fname,self._recs[index].lname,self._recs[index].position,self._recs[index].salary,self._recs[index].credit,self._recs[index].id,self._recs[index]._extra
        return s


    #pre: a key and a value are passed and must be valid
    #post: return the idnumber of that record
    #purpose: to find a id number of a certain record
    def getid(self, key, value):
        index=self.search(key, value)
        return self._recs[index].id
