url = input("saisir une adresse url: ")
test_lien = input("saisir le text de lien ")
lien = "<a href= =" +url + ">" + test_lien + "</a>"

htmlfile =open("test.html", "w")
htmlfile.write(lien)
htmlfile.close()
print(lien)
