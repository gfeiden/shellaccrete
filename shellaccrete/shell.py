
class Shell(object)
    """ """
    def __init__(self, inner_radius, thickness, expansion_velocity, angular_size=0.5, 
                 angular_res=0.1, geometry='cylindrical'):
        """ """
        self.thickness = thickness
        self.expansion_velocity = expansion_velocity

        # protect against negative thicknesses
        if self.thickness < 0.0:
            self.outer_radius = inner_radius
            self.inner_radius = self.outer_radius + thickness
        else:
            self.inner_radius = inner_radius
            self.outer_radius = self.inner_radius + thickness

        self.angle = np.pi*angular_size
        self.angular_res = angular_res
        self.coordinate_angles = np.arange(-angle, angle + angular_res, angular_res) 

    def update(self):
        """ """
         
