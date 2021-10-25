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
            #try:
            #    d = int(input("dråber per minut = "))
            #except ValueError:
            #    d = 0
            
            v = v_to_microliter(v)
            tm = htoMin(t)
            res = v / tm
            
            print(f"\ninfusionshastigheden = {round(res,2)}μl/minut\n===========\n")
            
    main()
except KeyboardInterrupt:
    print("\nGoodbye!")