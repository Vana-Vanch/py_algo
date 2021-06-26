def tower_of_hanoi(numberOfDisk,StartPeg=1,EndPeg=3):
    if numberOfDisk:
        tower_of_hanoi(numberOfDisk-1,StartPeg,6-StartPeg-EndPeg)
        print(f"Move Disc {numberOfDisk} from Peg {StartPeg} to Peg {EndPeg}")
        tower_of_hanoi(numberOfDisk-1,6-StartPeg-EndPeg,EndPeg)
tower_of_hanoi(4)        

