
    <code>
    def computepay(h,r):

        if h<=40 :

            p = h*r

        else :

            p = (h-40)*1.5*r + 40*r

        return p

    hrs = input("Enter Hours:")

    hours = float(hrs)

    r = input("Enter rate:")   

    rate = float(r)


    p = computepay(hours,rate)

    print(p)
    </code>
