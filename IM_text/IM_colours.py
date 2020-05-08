from matplotlib.colors import LinearSegmentedColormap

clist_1 = [(0, (228/256,183/256,60/256)),
         (0.5, (138/256, 162/256,154/256)),
         (1, (65/256,97/256,95/256))]

clist_2 = [(0, (137/256,62/256,69/256)),
         (0.5, (225/256, 188/256,167/256)),
         (1, (138/256,162/256,154/256))]

clist_3 = [(0, (225/256,188/256,167/256)),
         (0.33, (228/256, 183/256,60/256)),
         (0.66, (138/256,162/256,154/256)),
         (1, (65/256,97/256,95/256))]

clist_4 = [(0, (48/256,55/256,59/256)),
           (0.142, (137/256, 62/256,69/256)),
           (0.286, (225/256,188/256,167/256)),
           (0.429, (228/256, 183/256,60/256)),
           (0.571, (65/256, 97/256,95/256)),
           (0.714, (138/256, 162/256,154/256)),
           (0.857, (226/256, 222/256,217/256)),
           (1, (248/256, 245/256,231/256))]

im_tricolour_a = LinearSegmentedColormap.from_list(name="implement_tri_a", colors=clist_1)
im_tricolour_b = LinearSegmentedColormap.from_list(name="implement_tri_b", colors=clist_2)
im_four_colour = LinearSegmentedColormap.from_list(name="implement_four_colour", colors=clist_3)
im_multicolour = LinearSegmentedColormap.from_list(name="implement_multicolour", colors=clist_4)