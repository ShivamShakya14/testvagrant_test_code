# name = Shivam Shakya
# college = Lovely Professional University
# year_of_passing = 2023
# phone_number = 6395263422
# email_address = shivam0214shakya@gmail.com

def gprice(pd):
    if (pd[0]>=500):
        pd[0]=pd[0]*0.95
    return (pd[0]*pd[1]*pd[2])/100


lt = [1100,18,1]
um = [900,12,2]
ci = [200,28,3]
hn = [100,0,4]

prc_lt = gprice(lt) + lt[0]*lt[2]
prc_um = gprice(um) + um[0]*um[2]
prc_ci = gprice(ci) + ci[0]*ci[2]
prc_hn = gprice(hn) + hn[0]*hn[2]

total_price = prc_lt + prc_um + prc_ci + prc_hn
print(f"Total amount to be paid to the shop-keeper is {total_price}")

glst = [gprice(lt),gprice(um),gprice(ci),gprice(hn)]
sort_glst = sorted(glst)

print(f"Maximum GST is {sort_glst[-1]}")


