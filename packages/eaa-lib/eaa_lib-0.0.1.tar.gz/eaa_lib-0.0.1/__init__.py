def divisori (num_div):
    num_div=int(num_div)
    div=[]
    for n_div in range (1, num_div+1):
        if num_div % n_div == 0:
            div.append(n_div)
    return div

print(divisori(input()))