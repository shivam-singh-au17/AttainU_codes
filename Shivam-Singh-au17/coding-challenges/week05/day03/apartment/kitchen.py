# 1. The Kitchen has the following attributes:

# length: length of the bed in feet
# breadth: breadth of the bed in feet
# slab_material: whether the slab is granite, wood, marble and so on.
# has_sink: True or False depending on whether the kitchen has a sink or not
# has_slab: True or False depending on whether the kitchen has a slab or not
# furnishing_material: whether the material is wood, steel, plywood and so on.
# lpg_pipeline: True or False depending on whether the kitchen has an LPG pipeline or not

# 2. The Kitchen Object supports the following methods:

# cook(): Checks if lpg connection, slab and sink exist and returns “Kitchen can
# be used for cooking” . If these connections donot exist, returns “Kitchen
# unsuitable for cooking”



class Kitchen:
    def __init__(self,slab_material, length,breadth,has_sink,has_slab, furnishing_material, lpg_pipeline):
        self.length = length
        self.breadth = breadth
        self.has_sink = has_sink
        self.has_slab = has_slab
        self.furnishing_material = furnishing_material
        self.lpg_pipeline = lpg_pipeline
        self.slab_material = slab_material


    def cook(self):
        if (self.lpg_pipeline and self.has_sink and self.has_slab) == True:
            return('Kitchen can be used for cooking')
        else:
            return('Kitchen unsuitable for cooking')


# kitch = Kitchen(10, 10, 'marble', True, True, 'plywood', True)
# ans = kitch.cook()     
# print(ans)


