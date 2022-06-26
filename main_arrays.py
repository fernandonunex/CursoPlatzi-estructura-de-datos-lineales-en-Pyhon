from cube import Cube

def run():
    cube = Cube(3,3,3, 1)
    print(cube.get_height())
    print(cube.get_width())
    print(cube.get_deep())
    print(cube)
    
    print(cube.__getitem__(0,0,0))
    cube.__fillRandom__()
    print(cube.__getitem__(2,2,2))

    print(cube)

if __name__ == "__main__":
        run()