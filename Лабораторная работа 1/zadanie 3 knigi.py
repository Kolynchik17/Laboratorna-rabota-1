# TODO Найдите количество книг, которое можно разместить на дискете
obiom=(2**20)*1.44
stranic=100
strok=50
simvstrok=25
obsim=4
kniga=obsim*simvstrok*strok*stranic
vsego=obiom//kniga
print("Количество книг, помещающихся на дискету:", vsego)
