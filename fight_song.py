def singV(): 
    print("Go, team, go!")
    print("Defeat your foe.")

def singC():
    print("Go, team, go!")
    print("Defeat your foe.")
    print("Simply the best,")
    print("Better than the rest.")
    print("Go, team, go!")
    print("Defeat your foe.")
 
def sing_fight_song():
    singV()
    print()
    singC()
    print()
    
    for repetitions in range (1):
        singC()
        print()
        singV()
        print()
        
def main():
    sing_fight_song()
    
main()