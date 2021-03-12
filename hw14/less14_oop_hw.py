class Oxygen:

    t_soild = -218
    t_gas = -182

    def _convert_cels_to_far(self, t, scale):
        if scale == 'K':
            t = t - 273,15
            return t
        elif scale == 'F':
            t = (t - 32) * (5/9)
            return t
        elif scale == 'C':
            return t

    def agg_state(self, t, scale):
        t = self._convert_cels_to_far(t, scale)
        print(t)

        if t < self.t_soild:
            return 'I am soild'
        if self.t_soild < t < self.t_gas:
            return 'I am liquid'
        if t > self.t_gas:
            return 'I am steam'

o = Oxygen()
print(o.agg_state(-500, 'C'))