import c4d

def main():
    doc.StartUndo()
    objects = doc.GetActiveObjects(0)
    for obj in objects:
        print "instancing ",obj.GetName()
        instance = c4d.BaseObject(c4d.Oinstance)           # create a new instance object
        instance.SetName(obj.GetName() + '_instance')      # set it's name to the object's name + "_instance"
        instance.SetRelPos(obj.GetRelPos())         # set it's Relative Position to the object's Relative Position
        instance.SetRelScale(obj.GetRelScale())     # set it's Relative Scale to the object's Relative Scale
        instance.SetRelRot(obj.GetRelRot())
        instance[c4d.INSTANCEOBJECT_LINK] = obj            # set the instance's source object
        instance.InsertBefore(obj)                         # insert the instance object in the object manager,
                                                           # right before the source object. You can use other options.
                                                           # Like .InsertAfter(obj), if you want it after the source object.
        doc.AddUndo(c4d.UNDOTYPE_NEW, instance)
    doc.EndUndo()

if __name__ == '__main__':
    main()
    c4d.EventAdd()
