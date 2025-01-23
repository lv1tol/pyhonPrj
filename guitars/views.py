from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

gtr = [
    { "id": 1, "name": "IBANEZ GRG121DX BKF", "strings": 6, "price": 199.99, "image": "https://www.musicstore.com/on/demandware.static/-/Sites-masterCatalog_MusicStore/default/dw4f8b6f3b/images/hi-res/IBA_GRG121DX_BKF_1.jpg" },
    { "id": 2, "name": "YAMAHA PACIFICA 012 BL", "strings": 6, "price": 199.99, "image": "https://www.musicstore.com/on/demandware.static/-/Sites-masterCatalog_MusicStore/default/dw7b7f4c8b/images/hi-res/YAM_PACIFICA_012_BL_1.jpg" },
    { "id": 3, "name": "EPIPHONE LES PAUL SL EBONY", "strings": 6, "price": 99.99, "image": "https://www.musicstore.com/on/demandware.static/-/Sites-masterCatalog_MusicStore/default/dw7b7f4c8b/images/hi-res/EPI_LPSL_EB_1.jpg" },
    { "id": 4, "name": "FENDER SQUIER BULLET STRAT RW BSB", "strings": 6, "price": 119.99, "image": "https://www.musicstore.com/on/demandware.static/-/Sites-masterCatalog_MusicStore/default/dw7b7f4c8b/images/hi-res/FEN_SQ_BULLET_STRAT_RWB_1.jpg" },
    { "id": 5, "name": "EPIPHONE SG SPECIAL VE VINTAGE SUNBURST", "strings": 6, "price": 139.99, "image": "https://www.musicstore.com/on/demandware.static/-/Sites-masterCatalog_MusicStore/default/dw7b7f4c8b/images/hi-res/EPI_SGSPECIAL_VE_VSB_1.jpg" },
    { "id": 6, "name": "FENDER SQUIER AFFINITY STRAT HSS RW BSB", "strings": 6, "price": 219.99, "image": "https://www.musicstore.com/on/demandware.static/-/Sites-masterCatalog_MusicStore/default/dw7b7f4c8b/images/hi-res/FEN_SQ" } 

]

def home(request):
    return render(request, "index.html", {"guitars": gtr})

def list(request):
    html = "<h1>Guitars</h1> <ul>"
    for guitar in gtr:
        html += f"<li>{guitar['name']}</li>"
    html += "</ul>"
    return HttpResponse(html)

def details(request, id):
    return HttpResponse(f"Guitar: {gtr[id-1]['id']} | {gtr[id-1]['name']} | {gtr[id-1]['strings']} | {gtr[id-1]['price']}")

def listDetailed(request):
    html = "<h1>Guitars: </h1> <ul>"
    for guitar in gtr:
        html += f"<li>{guitar['id']} | {guitar['name']} | {guitar['strings']} | {guitar['price']}$</li>"
    html += "</ul>"
    return HttpResponse(html)