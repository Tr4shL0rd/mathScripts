try:
    # converts Volume to microliter
    def v_to_microliter(v:int):
        return v*1000

    # converts Time(hours) to mins
    def htoMin(t:int):
        return 60*t

    # calulates Volume and dropsPerMin 
    def drmin(v:int, d:int):
        return v*20

    def drm_to_mlm():
        return 10/20
        
    def main():
        while True:
            v = int(input("ml = "))    
            
            try:
                t = int(input("tid = "))
            except ValueError:
                t = 0
            try:
                d = int(input("dråber per minut = "))
            except ValueError:
                d = 0
            tm = htoMin(t)
            dr = drmin(v,d)
            res = dr/tm
            print(f"\ninfusionshastigheden = {res}dr/min\n===========\n")
    main()
except KeyboardInterrupt:
    print("\nGoodbye!")