import c4d

def main():
    def tool():
        return plugins.FindPlugin(doc.GetAction(), c4d.PLUGINTYPE_TOOL)

    def object(i=0):
        return doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN | c4d.GETACTIVEOBJECTFLAGS_SELECTIONORDER)

    def tag():
        return doc.GetActiveTag()

    def renderdata():
        return doc.GetActiveRenderData()

    def prefs(id):
        return plugins.FindPlugin(id, c4d.PLUGINTYPE_PREFS)
    
    def clearSelection(selection):
        for i in xrange(len(selection)):
            selection[i].DelBit(c4d.BIT_ACTIVE)
    
    selection = object()
    for i in xrange(len(selection)):
        clearSelection(object())
        doc.AddUndo(c4d.UNDOTYPE_CHANGE_SMALL, selection[i])
        print ("Making duplicate of object: {}".format(selection[i][c4d.ID_BASELIST_NAME]))
        selection[i].SetBit(c4d.BIT_ACTIVE)
        c4d.CallCommand(5126) # Instance
        
        
if __name__ == '__main__':
    main()
    c4d.EventAdd()