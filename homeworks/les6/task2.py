class Road_M16:

    name_road = 'M16'
    _length = 5000
    _width = 20


    def top_layer_road_mass(self, thickness=0.05, density=1200, info_print=False):
        top_layer_mass = ((Road_M16._length * Road_M16._width * thickness) * density) / 1000
        if info_print:
            print(f'Масса верхнего слоя дороги {self.name_road} составит {top_layer_mass} тонн.\n'
                  f'Но при условии следующих параметров:\n'
                  f'Длина дороги - {self._length} м;\n'
                  f'Ширина дороги - {self._width} м;\n'
                  f'Толщина верхнего слоя - {thickness} м;\n'
                  f'Усредненная плотность асфальтобетона - {density} кг/м3.\n')
        return top_layer_mass


road_m16 = Road_M16()

road_m16.top_layer_road_mass(info_print=True)

test_mass = road_m16.top_layer_road_mass()
print(test_mass)