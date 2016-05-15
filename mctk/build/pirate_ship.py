from mcpi2.minecraft import Minecraft
from mcpi2 import block
mc = Minecraft.create()
import pickle


###-----------------------Selectively Replace Sections of Blocks----------------------###

def SelRep(x1,y1,z1):
    x,y,z = mc.player.getPos()
    for x in range(x1):
        print("X is: ",x)
        for y in range(y1):
            print("Y is: ",y)
            for z in range(z1):
                print("Z is: ",z)
                print("Block type is: ", mc.getBlock(x+x1,y+y1,z+z1))
                if mc.getBlock(x+x1,y+y1,z+z1) == 9:
                    mc.setBlock(x, y, z, 0)

###------------------------------------------------Make/Delete Boxes--------------------------------------------###

def box (posx, posy, posz, sizex, sizey, sizez, block):
    #total size is given and needs to be divided to get the size from the center
    sizex = sizex/2
    sizey = sizey/2
    sizez = sizez/2
    #this part finds the two opposite corners to make the box
    pt1x = posx-sizex
    pt1y = posy-sizey
    pt1z = posz-sizez
    pt2x = posx+sizex
    pt2y = posy+sizey
    pt2z = posz+sizez
    #makes the box
    mc.setBlocks(pt1x, pt1y, pt1z, pt2x, pt2y, pt2z, block)

def cutbox(posx, posy, posz, sizex, sizey, sizez):
    #total size is given and needs to be divided to get the size from the center
    sizex = sizex/2
    sizey = sizey/2
    sizez = sizez/2
    #this part finds the two opposite corners to make the box
    pt1x = posx-sizex
    pt1y = posy-sizey
    pt1z = posz-sizez
    pt2x = posx+sizex
    pt2y = posy+sizey
    pt2z = posz+sizez
    #sets a box of air the same size as the box o erase it
    mc.setBlocks(pt1x, pt1y, pt1z, pt2x, pt2y, pt2z, 0)

###----------------------Copy/Paste Functions------------------------###

class CopyPaste:
    def copyStructure(self, posx, posy, posz, sizex, sizey, sizez):

        #this part finds the two opposite corners to make the box
        x1 = posx-sizex/2
        y1 = posy-sizey/2
        z1 = posz-sizez/2

        #creates list
        self.structure = []

        # Copy the structure
        for row in range(sizex):
            self.structure.append([])
            for column in range(sizey):
                self.structure[row].append([])
                for depth in range(sizez):
                    block = mc.getBlock(x1 + column, y1 + row, z1 + depth)
                    self.structure[row][column].append(block)

    def pasteStructure(self, posx, posy, posz, sizex, sizey, sizez):

        #this part finds the two opposite corners to make the box
        x1 = posx-sizex/2
        y1 = posy-sizey/2
        z1 = posz-sizez/2


        # Paste the structure
        for row in range(sizex):
            for column in range(sizey):
                for depth in range(sizez):
                    #gets block ID
                    BlockID = self.structure[row][column][depth]
                    mc.setBlock(x1 + column, y1 + row, z1 + depth, BlockID)
###------------------------------Pirate Ship Stuff-----------------------------###

def pirateShipGen(px,py,pz,block,block2,block3):

    box(px-23, py, pz, 10, 2, 2, block) #Box 1
    box(px-18, py, pz, 8, 8, 6, block) #Box 2
    box(px-14, py, pz, 8, 8, 10, block) #Box 3
    box(px-9, py, pz, 10, 8, 12, block) #Box 4
    box(px, py, pz, 10, 8, 12, block) #Box 6 (No box 5, already defined)
    box(px+10, py, pz, 10, 2, 2, block) #Box 7
    box(px, py, pz, 2, 20, 2, block2) #Box 8
    box(px, py, pz, 10, 8, 2, block3) #Box 9
