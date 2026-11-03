#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import urllib.parse
import os

DB_PATH = '/home/joe/Bureau/saveurs-d-agojie/backend/db.sqlite3'
PROD_IMG_DIR = '/home/joe/saveurs-dagojie-web/img/produits'
WEB_ROOT = '/home/joe/saveurs-dagojie-web'

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

def get_img(slug, fallback="plat-default.jpg"):
    target = f"{slug}.jpg"
    if os.path.exists(os.path.join(PROD_IMG_DIR, target)):
        return f"img/produits/{target}"
    if os.path.exists(os.path.join(WEB_ROOT, "img", target)):
        return f"img/{target}"
    return f"img/{fallback}"

def wa_link(item_name, price, unit=None):
    item_name = item_name.replace("d'Agojie", "d'Agojiés").replace("d'Agojié", "d'Agojiés")
    p_str = f"{price:,} FCFA".replace(",", " ")
    if unit:
        text = f"Bonjour Saveurs d'Agojiés, je souhaite commander : {item_name} ({p_str} / {unit})."
    else:
        text = f"Bonjour Saveurs d'Agojiés, je souhaite commander : {item_name} ({p_str})."
    return "https://wa.me/22901000000?text=" + urllib.parse.quote(text)

def format_price(price, unit=None):
    formatted = f"{price:,} FCFA".replace(",", " ")
    if unit and unit not in ("portion", "plat"):
        return f"{formatted} <small class='text-muted fs-6'>/ {unit}</small>"
    return formatted

def html_head(title, description="Saveurs d'Agojiés - De Notre Ferme à Votre Table. Gastronomie Béninoise authentique et produits frais à Porto-Novo."):
    return """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <title>""" + title + """ | Saveurs d'Agojiés</title>
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <meta content="Saveurs d'Agojiés, restaurant Porto-Novo, cuisine béninoise, traiteur, ferme bio, grillades, méchoui, produits frais, Amiwo, miel pur" name="keywords">
    <meta content='""" + description + """' name="description">

    <!-- Favicon -->
    <link href="img/logo-opt.png" rel="icon" type="image/png">

    <!-- Google Web Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;600;700&family=Nunito:wght@600;700;800;900&family=Pacifico&display=swap" rel="stylesheet">

    <!-- Icon Font Stylesheet -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.1/font/bootstrap-icons.css" rel="stylesheet">

    <!-- Libraries Stylesheet -->
    <link href="lib/animate/animate.min.css" rel="stylesheet">
    <link href="lib/owlcarousel/assets/owl.carousel.min.css" rel="stylesheet">
    <link href="lib/tempusdominus/css/tempusdominus-bootstrap-4.min.css" rel="stylesheet" />

    <!-- Customized Bootstrap Stylesheet -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Template Stylesheet -->
    <link href="css/style.css" rel="stylesheet">
</head>
<body>
    <div class="container-fluid bg-white p-0">
        <!-- Spinner Start -->
        <div id="spinner" class="show bg-white position-fixed translate-middle w-100 vh-100 top-50 start-50 d-flex align-items-center justify-content-center">
            <div class="spinner-border text-primary" style="width: 3rem; height: 3rem;" role="status">
                <span class="sr-only">Chargement...</span>
            </div>
        </div>
        <!-- Spinner End -->
"""

def html_nav(active_page="home"):
    act = {
        'home': ' active' if active_page == 'home' else '',
        'about': ' active' if active_page == 'about' else '',
        'service': ' active' if active_page == 'service' else '',
        'menu': ' active' if active_page == 'menu' else '',
        'ferme': ' active' if active_page == 'ferme' else '',
        'pages': ' active' if active_page in ('booking', 'team', 'testimonial') else '',
        'booking': ' active' if active_page == 'booking' else '',
        'team': ' active' if active_page == 'team' else '',
        'testimonial': ' active' if active_page == 'testimonial' else '',
        'contact': ' active' if active_page == 'contact' else '',
    }
    return """
        <!-- Navbar Start -->
        <div class="container-fluid position-relative p-0">
            <nav class="navbar navbar-expand-lg navbar-dark bg-dark px-4 px-lg-5 py-3 py-lg-0">
                <a href="index.html" class="navbar-brand p-0">
                    <h1 class="text-primary m-0"><i class="fa fa-utensils me-3"></i>Saveurs d'Agojiés</h1>
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse">
                    <span class="fa fa-bars"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarCollapse">
                    <div class="navbar-nav ms-auto py-0 pe-4">
                        <a href="index.html" class="nav-item nav-link""" + act['home'] + """">Accueil</a>
                        <a href="about.html" class="nav-item nav-link""" + act['about'] + """">À Propos</a>
                        <a href="service.html" class="nav-item nav-link""" + act['service'] + """">Services</a>
                        <a href="menu.html" class="nav-item nav-link""" + act['menu'] + """">Notre Carte</a>
                        <a href="ferme.html" class="nav-item nav-link""" + act['ferme'] + """">La Ferme</a>
                        <div class="nav-item dropdown">
                            <a href="#" class="nav-link dropdown-toggle""" + act['pages'] + """" data-bs-toggle="dropdown">Plus</a>
                            <div class="dropdown-menu m-0">
                                <a href="booking.html" class="dropdown-item""" + act['booking'] + """">Réservation & Devis</a>
                                <a href="team.html" class="dropdown-item""" + act['team'] + """">Notre Équipe</a>
                                <a href="testimonial.html" class="dropdown-item""" + act['testimonial'] + """">Témoignages</a>
                            </div>
                        </div>
                        <a href="contact.html" class="nav-item nav-link""" + act['contact'] + """">Contact</a>
                    </div>
                    <a href="booking.html" class="btn btn-primary py-2 px-4">Réserver Une Table</a>
                </div>
            </nav>
"""

def html_page_header(title, breadcrumb):
    return """
            <div class="container-fluid py-5 bg-dark hero-header mb-5">
                <div class="container text-center my-5 pt-5 pb-4">
                    <h1 class="display-3 text-white mb-3 animated slideInDown">""" + title + """</h1>
                    <nav aria-label="breadcrumb">
                        <ol class="breadcrumb justify-content-center text-uppercase">
                            <li class="breadcrumb-item"><a href="index.html" class="text-primary">Accueil</a></li>
                            <li class="breadcrumb-item text-white active" aria-current="page">""" + breadcrumb + """</li>
                        </ol>
                    </nav>
                </div>
            </div>
        </div>
        <!-- Navbar End -->
"""

def html_footer():
    return """
        <!-- Footer Start -->
        <div class="container-fluid bg-dark text-light footer pt-5 mt-5 wow fadeIn" data-wow-delay="0.1s">
            <div class="container py-5">
                <div class="row g-5">
                    <div class="col-lg-3 col-md-6">
                        <h4 class="section-title ff-secondary text-start text-primary fw-normal mb-4">Saveurs d'Agojiés</h4>
                        <p class="mb-3">De notre ferme à votre table. Gastronomie béninoise raffinée, viandes nobles d'élevage plein air et produits 100% frais du terroir à Porto-Novo.</p>
                        <div class="d-flex pt-2">
                            <a class="btn btn-outline-light btn-social" href="https://wa.me/22901000000" target="_blank"><i class="fab fa-whatsapp"></i></a>
                            <a class="btn btn-outline-light btn-social" href="https://facebook.com" target="_blank"><i class="fab fa-facebook-f"></i></a>
                            <a class="btn btn-outline-light btn-social" href="https://instagram.com" target="_blank"><i class="fab fa-instagram"></i></a>
                            <a class="btn btn-outline-light btn-social" href="tel:+22901000000"><i class="fa fa-phone"></i></a>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6">
                        <h4 class="section-title ff-secondary text-start text-primary fw-normal mb-4">Coordonnées</h4>
                        <p class="mb-2"><i class="fa fa-map-marker-alt me-3 text-primary"></i>Porto-Novo, Bénin</p>
                        <p class="mb-2"><i class="fa fa-phone-alt me-3 text-primary"></i>+229 01 00 00 00</p>
                        <p class="mb-2"><i class="fab fa-whatsapp me-3 text-primary"></i>+229 01 00 00 00</p>
                        <p class="mb-2"><i class="fa fa-envelope me-3 text-primary"></i>contact@saveurs-dagojies.com</p>
                    </div>
                    <div class="col-lg-3 col-md-6">
                        <h4 class="section-title ff-secondary text-start text-primary fw-normal mb-4">Horaires</h4>
                        <h5 class="text-light fw-normal">Lundi - Samedi</h5>
                        <p>08h00 - 22h00</p>
                        <h5 class="text-light fw-normal">Dimanche & Fériés</h5>
                        <p>09h00 - 21h00</p>
                        <p class="small text-muted mb-0"><i class="fa fa-info-circle me-1"></i>Service Traiteur sur réservation 24h/24</p>
                    </div>
                    <div class="col-lg-3 col-md-6">
                        <h4 class="section-title ff-secondary text-start text-primary fw-normal mb-4">Navigation Rapide</h4>
                        <a class="btn btn-link" href="about.html">Notre Histoire & Terroir</a>
                        <a class="btn btn-link" href="menu.html">Carte & Spécialités</a>
                        <a class="btn btn-link" href="ferme.html">Produits de la Ferme</a>
                        <a class="btn btn-link" href="service.html">Services & Traiteur</a>
                        <a class="btn btn-link" href="booking.html">Réservation & Devis</a>
                        <a class="btn btn-link" href="contact.html">Contact & Accès</a>
                    </div>
                </div>
            </div>
            <div class="container">
                <div class="copyright">
                    <div class="row">
                        <div class="col-md-6 text-center text-md-start mb-3 mb-md-0">
                            &copy; <a class="border-bottom" href="index.html">Saveurs d'Agojiés</a>, Tous droits réservés. L'Excellence du terroir béninois.
                        </div>
                        <div class="col-md-6 text-center text-md-end">
                            <div class="footer-menu">
                                <a href="index.html">Accueil</a>
                                <a href="menu.html">Carte</a>
                                <a href="ferme.html">Ferme</a>
                                <a href="contact.html">Contact</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Footer End -->

        <!-- Floating WhatsApp Button -->
        <a href="https://wa.me/22901000000?text=Bonjour%20Saveurs%20d%27Agoji%C3%A9%2C%20je%20souhaite%20passer%20une%20commande." target="_blank" class="floating-whatsapp" title="Commander via WhatsApp">
            <i class="fab fa-whatsapp"></i>
        </a>

        <!-- Back to Top -->
        <a href="#" class="btn btn-lg btn-primary btn-lg-square back-to-top"><i class="bi bi-arrow-up"></i></a>
    </div>

    <!-- JavaScript Libraries -->
    <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="lib/wow/wow.min.js"></script>
    <script src="lib/easing/easing.min.js"></script>
    <script src="lib/waypoints/waypoints.min.js"></script>
    <script src="lib/counterup/counterup.min.js"></script>
    <script src="lib/owlcarousel/owl.carousel.min.js"></script>
    <script src="lib/tempusdominus/js/moment.min.js"></script>
    <script src="lib/tempusdominus/js/moment-timezone.min.js"></script>
    <script src="lib/tempusdominus/js/tempusdominus-bootstrap-4.min.js"></script>

    <!-- Template Javascript -->
    <script src="js/main.js"></script>
</body>
</html>
"""

# Query Data
all_plats = cur.execute("SELECT * FROM menu_plat ORDER BY categorie_id, id").fetchall()
all_boissons = cur.execute("SELECT * FROM menu_boisson ORDER BY id").fetchall()
all_ferme = cur.execute("SELECT * FROM ferme_produitferme ORDER BY categorie_id, id").fetchall()
cat_menu = cur.execute("SELECT * FROM menu_categoriemenu ORDER BY `order`").fetchall()
cat_ferme = cur.execute("SELECT * FROM ferme_categorieferme ORDER BY `order`").fetchall()

print("Base setup ready.")



# ==============================================================================
# Helper to render a grid of menu items
# ==============================================================================
def render_dish_grid(items):
    out = '<div class="row g-4">'
    for it in items:
        img_src = get_img(it['slug'])
        p_formatted = format_price(it['price'])
        w_link = wa_link(it['name'], it['price'])
        desc = it['description'] if it['description'] else "Préparé avec les ingrédients frais de notre ferme."
        
        # Options tags if any
        opts_badge = ""
        if 'options_disponibles' in it.keys() and it['options_disponibles']:
            try:
                import json
                opts_data = json.loads(it['options_disponibles'])
                if opts_data:
                    k = list(opts_data.keys())[0]
                    opts_badge = f'<span class="badge bg-secondary text-white ms-2" style="font-size: 0.7rem;">Choix {k}</span>'
            except:
                pass

        out += f"""
            <div class="col-lg-6">
                <div class="d-flex align-items-center bg-light rounded p-3 h-100 shadow-sm border border-1">
                    <img class="flex-shrink-0 img-fluid rounded" src="{img_src}" alt="{it['name'].replace("d'Agojie", "d'Agojiés").replace("d'Agojié", "d'Agojiés")}" style="width: 85px; height: 85px; object-fit: cover;">
                    <div class="w-100 d-flex flex-column text-start ps-3">
                        <h5 class="d-flex justify-content-between border-bottom pb-2 mb-1">
                            <span class="fw-bold">{it['name'].replace("d'Agojie", "d'Agojiés").replace("d'Agojié", "d'Agojiés")} {opts_badge}</span>
                            <span class="text-primary fw-bold flex-shrink-0 ms-2">{p_formatted}</span>
                        </h5>
                        <div class="d-flex justify-content-between align-items-center">
                            <small class="text-muted fst-italic">{desc}</small>
                            <a href="{w_link}" target="_blank" class="btn btn-sm btn-whatsapp ms-2 flex-shrink-0 rounded-circle" style="width: 34px; height: 34px; display: flex; align-items: center; justify-content: center;" title="Commander sur WhatsApp">
                                <i class="fab fa-whatsapp"></i>
                            </a>
                        </div>
                    </div>
                </div>
            </div>"""
    out += '</div>'
    return out

# ==============================================================================
# 1. INDEX.HTML
# ==============================================================================
def gen_index():
    grillades = [p for p in all_plats if p['categorie_id'] == 2][:8]
    traditionnels = [p for p in all_plats if p['categorie_id'] in (3, 4)][:8]
    ferme_boissons = []
    for b in all_boissons[:4]:
        ferme_boissons.append({'name': b['name'], 'slug': b['slug'], 'description': b['description'], 'price': b['price']})
    for f in all_ferme[:4]:
        ferme_boissons.append({'name': f['name'], 'slug': f['slug'], 'description': f['description'], 'price': f['price']})

    html = html_head("Accueil | De Notre Ferme à Votre Table", "Saveurs d'Agojiés : Restaurant gastronomique béninois, viandes nobles d'élevage, méchouis et produits frais à Porto-Novo.")
    html += html_nav("home")
    html += """
            <div class="container-fluid py-5 bg-dark hero-header mb-5">
                <div class="container my-5 py-5">
                    <div class="row align-items-center g-5">
                        <div class="col-lg-6 text-center text-lg-start">
                            <h1 class="display-3 text-white animated slideInLeft">Savourez Nos<br>Plats d'Exception</h1>
                            <p class="text-white animated slideInLeft mb-4 pb-2">De notre ferme à votre table : découvrez l'excellence du terroir béninois avec nos viandes nobles d'élevage en plein air, méchouis au feu de bois, poissons frais et spécialités authentiques cuisinées avec les récoltes du jour à Porto-Novo.</p>
                            <a href="booking.html" class="btn btn-primary py-sm-3 px-sm-5 me-3 animated slideInLeft">Réserver Une Table</a>
                        </div>
                        <div class="col-lg-6 text-center text-lg-end overflow-hidden">
                            <img class="img-fluid" src="img/hero.png" alt="">
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Navbar End -->

        <!-- Service Start -->
        <div class="container-fluid py-5">
            <div class="container">
                <div class="text-center wow fadeInUp" data-wow-delay="0.1s">
                    <h5 class="section-title ff-secondary text-center text-primary fw-normal">Nos Pôles d'Excellence</h5>
                    <h1 class="mb-5">Tout l'Univers Saveurs d'Agojiés</h1>
                </div>
                <div class="row g-4">
                    <div class="col-lg-3 col-sm-6 wow fadeInUp" data-wow-delay="0.1s">
                        <div class="service-item rounded pt-3 h-100 shadow-sm border border-1">
                            <div class="p-4 text-center">
                                <i class="fa fa-3x fa-egg text-primary mb-4"></i>
                                <h5 class="fw-bold">Élevage & Ferme Bio</h5>
                                <p class="text-muted">Volailles nobles (oies, dindes, goliath, pintades), moutons peulhs de race, lapins et alevins certifiés.</p>
                                <a href="ferme.html" class="btn btn-link text-primary p-0">En savoir plus <i class="fa fa-arrow-right ms-1"></i></a>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-sm-6 wow fadeInUp" data-wow-delay="0.3s">
                        <div class="service-item rounded pt-3 h-100 shadow-sm border border-1">
                            <div class="p-4 text-center">
                                <i class="fa fa-3x fa-utensils text-primary mb-4"></i>
                                <h5 class="fw-bold">Restauration & Grillades</h5>
                                <p class="text-muted">Méchouis d'exception, poissons braisés, sauces feuilles fraîches (Moringa, Noni) et authentique Amiwo.</p>
                                <a href="menu.html" class="btn btn-link text-primary p-0">Voir la carte <i class="fa fa-arrow-right ms-1"></i></a>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-sm-6 wow fadeInUp" data-wow-delay="0.5s">
                        <div class="service-item rounded pt-3 h-100 shadow-sm border border-1">
                            <div class="p-4 text-center">
                                <i class="fa fa-3x fa-concierge-bell text-primary mb-4"></i>
                                <h5 class="fw-bold">Service Traiteur</h5>
                                <p class="text-muted">Banquets de mariages, anniversaires, réceptions d'entreprise et livraison soignée à Porto-Novo et ses environs.</p>
                                <a href="service.html" class="btn btn-link text-primary p-0">Nos formules <i class="fa fa-arrow-right ms-1"></i></a>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-sm-6 wow fadeInUp" data-wow-delay="0.7s">
                        <div class="service-item rounded pt-3 h-100 shadow-sm border border-1">
                            <div class="p-4 text-center">
                                <i class="fa fa-3x fa-graduation-cap text-primary mb-4"></i>
                                <h5 class="fw-bold">Formations & Conseil</h5>
                                <p class="text-muted">Transmission du savoir-faire en élevage plein air, pisciculture, maraîchage agro-écologique et cuisine traiteur.</p>
                                <a href="service.html#formations" class="btn btn-link text-primary p-0">Nos ateliers <i class="fa fa-arrow-right ms-1"></i></a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Service End -->

        <!-- About Start -->
        <div class="container-fluid py-5">
            <div class="container">
                <div class="row g-5 align-items-center">
                    <div class="col-lg-6">
                        <div class="row g-3">
                            <div class="col-6 text-start">
                                <img class="img-fluid rounded w-100 wow zoomIn shadow" data-wow-delay="0.1s" src="img/about-1.jpg" alt="Ferme Saveurs d'Agojiés">
                            </div>
                            <div class="col-6 text-start">
                                <img class="img-fluid rounded w-75 wow zoomIn shadow" data-wow-delay="0.3s" src="img/about-2.jpg" style="margin-top: 25%;" alt="Chef en cuisine">
                            </div>
                            <div class="col-6 text-end">
                                <img class="img-fluid rounded w-75 wow zoomIn shadow" data-wow-delay="0.5s" src="img/about-3.jpg" alt="Plat traditionnel">
                            </div>
                            <div class="col-6 text-end">
                                <img class="img-fluid rounded w-100 wow zoomIn shadow" data-wow-delay="0.7s" src="img/about-4.jpg" alt="Salle et dégustation">
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <h5 class="section-title ff-secondary text-start text-primary fw-normal">À Propos de Nous</h5>
                        <h1 class="mb-4">Bienvenue chez <span class="text-primary">Saveurs d'Agojiés</span></h1>
                        <p class="mb-4">
                            Implantée au cœur de Porto-Novo, <strong>Saveurs d'Agojiés</strong> est née d'une vision forte : reconnecter la gastronomie béninoise à la terre. Nous maîtrisons chaque maillon de la chaîne, du grain semé et de l'animal choyé jusqu'au dressage final dans votre assiette.
                        </p>
                        <p class="mb-4">
                            Nos viandes proviennent exclusivement de nos élevages en plein air sans antibiotiques chimiques, nos poissons sont pêchés dans nos viviers, et nos légumes et aromates sont cueillis chaque matin à la rosée. Cuisiner vrai, servir avec cœur et célébrer nos racines : telle est notre promesse quotidienne.
                        </p>
                        <div class="row g-4 mb-4">
                            <div class="col-sm-6">
                                <div class="d-flex align-items-center border-start border-5 border-primary px-3">
                                    <h1 class="flex-shrink-0 display-5 text-primary mb-0" data-toggle="counter-up">100</h1>
                                    <span class="fs-4 text-primary fw-bold me-2">%</span>
                                    <div class="ps-3">
                                        <p class="mb-0">Produits Frais</p>
                                        <h6 class="text-uppercase mb-0 fw-bold">& Bio Terroir</h6>
                                    </div>
                                </div>
                            </div>
                            <div class="col-sm-6">
                                <div class="d-flex align-items-center border-start border-5 border-primary px-3">
                                    <h1 class="flex-shrink-0 display-5 text-primary mb-0" data-toggle="counter-up">45</h1>
                                    <span class="fs-4 text-primary fw-bold me-2">+</span>
                                    <div class="ps-3">
                                        <p class="mb-0">Spécialités</p>
                                        <h6 class="text-uppercase mb-0 fw-bold">& Recettes Nobles</h6>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <a class="btn btn-primary py-3 px-5 mt-2" href="about.html">Découvrir Notre Histoire</a>
                    </div>
                </div>
            </div>
        </div>
        <!-- About End -->

        <!-- Menu Start -->
        <div class="container-fluid py-5" id="menu">
            <div class="container">
                <div class="text-center wow fadeInUp" data-wow-delay="0.1s">
                    <h5 class="section-title ff-secondary text-center text-primary fw-normal">Carte & Spécialités</h5>
                    <h1 class="mb-5">Nos Plats les Plus Plébiscités</h1>
                </div>
                <div class="tab-class text-center wow fadeInUp" data-wow-delay="0.1s">
                    <ul class="nav nav-pills d-inline-flex justify-content-center border-bottom mb-5">
                        <li class="nav-item">
                            <a class="d-flex align-items-center text-start mx-3 ms-0 pb-3 active" data-bs-toggle="pill" href="#tab-1">
                                <i class="fa fa-fire fa-2x text-primary"></i>
                                <div class="ps-3">
                                    <small class="text-body">Les Incontournables</small>
                                    <h6 class="mt-n1 mb-0">Grillades & Méchouis</h6>
                                </div>
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="d-flex align-items-center text-start mx-3 pb-3" data-bs-toggle="pill" href="#tab-2">
                                <i class="fa fa-utensils fa-2x text-primary"></i>
                                <div class="ps-3">
                                    <small class="text-body">L'Authentique</small>
                                    <h6 class="mt-n1 mb-0">Pâtes & Plats Locaux</h6>
                                </div>
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="d-flex align-items-center text-start mx-3 me-0 pb-3" data-bs-toggle="pill" href="#tab-3">
                                <i class="fa fa-leaf fa-2x text-primary"></i>
                                <div class="ps-3">
                                    <small class="text-body">Fraîcheur & Douceurs</small>
                                    <h6 class="mt-n1 mb-0">Ferme, Jus & Miel</h6>
                                </div>
                            </a>
                        </li>
                    </ul>
                    <div class="tab-content">
                        <div id="tab-1" class="tab-pane fade show p-0 active">
                            """ + render_dish_grid(grillades) + """
                        </div>
                        <div id="tab-2" class="tab-pane fade show p-0">
                            """ + render_dish_grid(traditionnels) + """
                        </div>
                        <div id="tab-3" class="tab-pane fade show p-0">
                            """ + render_dish_grid(ferme_boissons) + """
                        </div>
                    </div>
                    <div class="text-center mt-5">
                        <a href="menu.html" class="btn btn-primary py-3 px-5 shadow">
                            <i class="fa fa-book-open me-2"></i>Consulter Notre Carte Complète (75+ Plats & Produits)
                        </a>
                    </div>
                </div>
            </div>
        </div>
        <!-- Menu End -->

        <!-- Reservation Start -->
        <div class="container-fluid py-5 px-0 wow fadeInUp" data-wow-delay="0.1s">
            <div class="row g-0">
                <div class="col-md-6">
                    <div class="video position-relative h-100 d-flex align-items-center justify-content-center" style="background: linear-gradient(rgba(15, 23, 43, .4), rgba(15, 23, 43, .4)), url('img/video.jpg') center center/cover no-repeat; min-height: 400px;">
                        <a href="https://wa.me/22901000000?text=Bonjour%20Saveurs%20d%27Agoji%C3%A9%2C%20je%20souhaite%20r%C3%A9server%20une%20table%20ou%20un%20m%C3%A9choui." target="_blank" class="btn-play">
                            <span></span>
                        </a>
                    </div>
                </div>
                <div class="col-md-6 bg-dark d-flex align-items-center">
                    <div class="p-5 wow fadeInUp w-100" data-wow-delay="0.2s">
                        <h5 class="section-title ff-secondary text-start text-primary fw-normal">Réservation & Commande</h5>
                        <h1 class="text-white mb-4">Réservez Votre Déjeuner ou Événement</h1>
                        <form id="reservationForm" onsubmit="event.preventDefault(); submitRes();">
                            <div class="row g-3">
                                <div class="col-md-6">
                                    <div class="form-floating">
                                        <input type="text" class="form-control" id="resName" placeholder="Votre Nom" required>
                                        <label for="resName">Votre Nom</label>
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="form-floating">
                                        <input type="tel" class="form-control" id="resPhone" placeholder="Téléphone / WhatsApp" required>
                                        <label for="resPhone">Téléphone / WhatsApp</label>
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="form-floating">
                                        <input type="datetime-local" class="form-control" id="resDatetime" required>
                                        <label for="resDatetime">Date & Heure Souhaitée</label>
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="form-floating">
                                        <select class="form-select" id="resGuests">
                                            <option value="1 à 2 personnes">1 à 2 personnes</option>
                                            <option value="3 à 5 personnes">3 à 5 personnes</option>
                                            <option value="6 à 10 personnes">6 à 10 personnes</option>
                                            <option value="Groupe / Événement (+10 personnes)">Groupe (+10 personnes)</option>
                                        </select>
                                        <label for="resGuests">Nombre de Personnes</label>
                                    </div>
                                </div>
                                <div class="col-12">
                                    <div class="form-floating">
                                        <select class="form-select" id="resService">
                                            <option value="Table au Restaurant">Repas au restaurant</option>
                                            <option value="Livraison Express Bureau/Domicile">Livraison à domicile / bureau</option>
                                            <option value="Commande de Méchoui Entier (Dinde/Mouton)">Commande de Méchoui entier</option>
                                            <option value="Service Traiteur & Réception">Service Traiteur / Événement</option>
                                        </select>
                                        <label for="resService">Prestation Souhaitée</label>
                                    </div>
                                </div>
                                <div class="col-12">
                                    <div class="form-floating">
                                        <textarea class="form-control" placeholder="Demande particulière ou plat préféré" id="resMessage" style="height: 100px"></textarea>
                                        <label for="resMessage">Précisions (plats souhaités, adresse...)</label>
                                    </div>
                                </div>
                                <div class="col-12">
                                    <button class="btn btn-whatsapp w-100 py-3 fs-6" type="submit">
                                        <i class="fab fa-whatsapp me-2"></i>Confirmer via WhatsApp Express
                                    </button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        <!-- Reservation End -->

        <!-- Team Start -->
        <div class="container-fluid pt-5 pb-3">
            <div class="container">
                <div class="text-center wow fadeInUp" data-wow-delay="0.1s">
                    <h5 class="section-title ff-secondary text-center text-primary fw-normal">Notre Brigade & Experts</h5>
                    <h1 class="mb-5">Des Passionnés du Terroir</h1>
                </div>
                <div class="row g-4">
                    <div class="col-lg-3 col-md-6 wow fadeInUp" data-wow-delay="0.1s">
                        <div class="team-item text-center rounded overflow-hidden shadow-sm border">
                            <div class="rounded-circle overflow-hidden m-4">
                                <img class="img-fluid" src="img/team-1.jpg" alt="Chef Cuisinier" style="width: 200px; height: 200px; object-fit: cover;">
                            </div>
                            <h5 class="mb-0 fw-bold">Chef Joseph D.</h5>
                            <small class="text-muted">Chef Cuisinier & Maître Sauces</small>
                            <div class="d-flex justify-content-center mt-3 mb-4">
                                <a class="btn btn-square btn-primary mx-1" href="https://wa.me/22901000000" target="_blank"><i class="fab fa-whatsapp"></i></a>
                                <a class="btn btn-square btn-primary mx-1" href="#"><i class="fab fa-facebook-f"></i></a>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 wow fadeInUp" data-wow-delay="0.3s">
                        <div class="team-item text-center rounded overflow-hidden shadow-sm border">
                            <div class="rounded-circle overflow-hidden m-4">
                                <img class="img-fluid" src="img/team-2.jpg" alt="Responsable Élevage" style="width: 200px; height: 200px; object-fit: cover;">
                            </div>
                            <h5 class="mb-0 fw-bold">Dah Agodjié</h5>
                            <small class="text-muted">Directeur Ferme & Élevage</small>
                            <div class="d-flex justify-content-center mt-3 mb-4">
                                <a class="btn btn-square btn-primary mx-1" href="https://wa.me/22901000000" target="_blank"><i class="fab fa-whatsapp"></i></a>
                                <a class="btn btn-square btn-primary mx-1" href="#"><i class="fab fa-facebook-f"></i></a>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 wow fadeInUp" data-wow-delay="0.5s">
                        <div class="team-item text-center rounded overflow-hidden shadow-sm border">
                            <div class="rounded-circle overflow-hidden m-4">
                                <img class="img-fluid" src="img/team-3.jpg" alt="Maître Rôtisseur" style="width: 200px; height: 200px; object-fit: cover;">
                            </div>
                            <h5 class="mb-0 fw-bold">Maître Paulin S.</h5>
                            <small class="text-muted">Spécialiste Méchouis & Braisés</small>
                            <div class="d-flex justify-content-center mt-3 mb-4">
                                <a class="btn btn-square btn-primary mx-1" href="https://wa.me/22901000000" target="_blank"><i class="fab fa-whatsapp"></i></a>
                                <a class="btn btn-square btn-primary mx-1" href="#"><i class="fab fa-facebook-f"></i></a>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 wow fadeInUp" data-wow-delay="0.7s">
                        <div class="team-item text-center rounded overflow-hidden shadow-sm border">
                            <div class="rounded-circle overflow-hidden m-4">
                                <img class="img-fluid" src="img/team-4.jpg" alt="Responsable Traiteur" style="width: 200px; height: 200px; object-fit: cover;">
                            </div>
                            <h5 class="mb-0 fw-bold">Awa Mensah</h5>
                            <small class="text-muted">Responsable Service & Réceptions</small>
                            <div class="d-flex justify-content-center mt-3 mb-4">
                                <a class="btn btn-square btn-primary mx-1" href="https://wa.me/22901000000" target="_blank"><i class="fab fa-whatsapp"></i></a>
                                <a class="btn btn-square btn-primary mx-1" href="#"><i class="fab fa-facebook-f"></i></a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Team End -->

        <!-- Testimonial Start -->
        <div class="container-fluid py-5 wow fadeInUp" data-wow-delay="0.1s">
            <div class="container">
                <div class="text-center">
                    <h5 class="section-title ff-secondary text-center text-primary fw-normal">Livre d'Or</h5>
                    <h1 class="mb-5">Ce Que Disent Nos Clients !</h1>
                </div>
                <div class="owl-carousel testimonial-carousel">
                    <div class="testimonial-item bg-transparent border rounded p-4 shadow-sm">
                        <i class="fa fa-quote-left fa-2x text-primary mb-3"></i>
                        <p class="fst-italic text-muted">« L'Amiwo au poulet fermier est une véritable madeleine de Proust. La viande est tendre, parfumée et les sauces ont ce goût authentique inimitable. Service très soigné ! »</p>
                        <div class="d-flex align-items-center">
                            <img class="img-fluid flex-shrink-0 rounded-circle" src="img/testimonial-1.jpg" style="width: 50px; height: 50px; object-fit: cover;">
                            <div class="ps-3">
                                <h5 class="mb-1 fw-bold">Séverin K.</h5>
                                <small>Cadre Bancaire, Porto-Novo</small>
                            </div>
                        </div>
                    </div>
                    <div class="testimonial-item bg-transparent border rounded p-4 shadow-sm">
                        <i class="fa fa-quote-left fa-2x text-primary mb-3"></i>
                        <p class="fst-italic text-muted">« Pour le mariage de notre fille (180 personnes), Saveurs d'Agojiés a assuré un méchoui de mouton et des poissons braisés spectaculaires. Tout le monde en parle encore. Bravo ! »</p>
                        <div class="d-flex align-items-center">
                            <img class="img-fluid flex-shrink-0 rounded-circle" src="img/testimonial-2.jpg" style="width: 50px; height: 50px; object-fit: cover;">
                            <div class="ps-3">
                                <h5 class="mb-1 fw-bold">Béatrice H.</h5>
                                <small>Organisatrice d'Événements</small>
                            </div>
                        </div>
                    </div>
                    <div class="testimonial-item bg-transparent border rounded p-4 shadow-sm">
                        <i class="fa fa-quote-left fa-2x text-primary mb-3"></i>
                        <p class="fst-italic text-muted">« Leurs jus pressés à froid sans sucre ajouté et leur miel pur de bambousier sont incomparables. On sent immédiatement la fraîcheur de la ferme. »</p>
                        <div class="d-flex align-items-center">
                            <img class="img-fluid flex-shrink-0 rounded-circle" src="img/testimonial-3.jpg" style="width: 50px; height: 50px; object-fit: cover;">
                            <div class="ps-3">
                                <h5 class="mb-1 fw-bold">Dr. Marc G.</h5>
                                <small>Médecin Nutritionniste</small>
                            </div>
                        </div>
                    </div>
                    <div class="testimonial-item bg-transparent border rounded p-4 shadow-sm">
                        <i class="fa fa-quote-left fa-2x text-primary mb-3"></i>
                        <p class="fst-italic text-muted">« Livraison express et plats toujours bien chauds au bureau. Le sauté de crabe et le riz gras garni à la viande de lapin sont une pure merveille culinaire. »</p>
                        <div class="d-flex align-items-center">
                            <img class="img-fluid flex-shrink-0 rounded-circle" src="img/testimonial-4.jpg" style="width: 50px; height: 50px; object-fit: cover;">
                            <div class="ps-3">
                                <h5 class="mb-1 fw-bold">Fatou D.</h5>
                                <small>Directrice d'Agence, Cotonou</small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Testimonial End -->

        <script>
        function submitRes() {
            var n = document.getElementById('resName').value;
            var p = document.getElementById('resPhone').value;
            var d = document.getElementById('resDatetime').value;
            var g = document.getElementById('resGuests').value;
            var s = document.getElementById('resService').value;
            var m = document.getElementById('resMessage').value;
            var txt = "*Réservation Saveurs d'Agojiés*%0A%0A" +
                      "👤 *Nom :* " + encodeURIComponent(n) + "%0A" +
                      "📞 *Tél :* " + encodeURIComponent(p) + "%0A" +
                      "📅 *Date :* " + encodeURIComponent(d) + "%0A" +
                      "👥 *Personnes :* " + encodeURIComponent(g) + "%0A" +
                      "🍽️ *Prestation :* " + encodeURIComponent(s) + "%0A" +
                      (m ? "📝 *Notes :* " + encodeURIComponent(m) + "%0A" : "");
            window.open("https://wa.me/22901000000?text=" + txt, "_blank");
        }
        </script>
    """
    html += html_footer()
    with open(os.path.join(WEB_ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("✓ index.html written.")

gen_index()


# ==============================================================================
# 2. ABOUT.HTML
# ==============================================================================
def gen_about():
    html = html_head("À Propos | Saveurs d'Agojiés", "Découvrez l'histoire, la vision et les valeurs de Saveurs d'Agojiés : de la terre à votre table à Porto-Novo.")
    html += html_nav("about")
    html += html_page_header("À Propos de Nous", "À Propos")
    html += """
        <!-- About Start -->
        <div class="container-fluid py-5">
            <div class="container">
                <div class="row g-5 align-items-center">
                    <div class="col-lg-6">
                        <div class="row g-3">
                            <div class="col-6 text-start">
                                <img class="img-fluid rounded w-100 wow zoomIn shadow" data-wow-delay="0.1s" src="img/about-1.jpg" alt="Ferme agro-écologique">
                            </div>
                            <div class="col-6 text-start">
                                <img class="img-fluid rounded w-75 wow zoomIn shadow" data-wow-delay="0.3s" src="img/about-2.jpg" style="margin-top: 25%;" alt="Cuisine béninoise de terroir">
                            </div>
                            <div class="col-6 text-end">
                                <img class="img-fluid rounded w-75 wow zoomIn shadow" data-wow-delay="0.5s" src="img/about-3.jpg" alt="Plat traditionnel">
                            </div>
                            <div class="col-6 text-end">
                                <img class="img-fluid rounded w-100 wow zoomIn shadow" data-wow-delay="0.7s" src="img/about-4.jpg" alt="Accueil et convivialité">
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <h5 class="section-title ff-secondary text-start text-primary fw-normal">Notre Histoire & Terroir</h5>
                        <h1 class="mb-4">De Notre Ferme à Votre Table : <span class="text-primary">L'Art Culinaire Béninois</span></h1>
                        <p class="mb-4">
                            Saveurs d'Agojiés est une aventure passionnée née à Porto-Novo. Face à la standardisation de l'alimentation urbaine, nous avons fait le choix radical de l'authenticité : créer un écosystème intégré combinant une <strong>ferme agro-pastorale biologique</strong> et un <strong>restaurant gastronomique béninois</strong>.
                        </p>
                        <p class="mb-4">
                            Chez nous, pas d'intermédiaire ni de chaîne du froid industrielle : les oies, dindes, poulets goliath et moutons grandissent en liberté, nourris avec des céréales et herbes saines. Les alevins et poissons prospèrent dans des viviers d'eau claire. Chaque matin, le chef sélectionne les légumes, le basilic frais, le moringa et les herbes aromatiques pour mijoter vos plats du midi et du soir.
                        </p>
                        <div class="row g-4 mb-4">
                            <div class="col-sm-6">
                                <div class="d-flex align-items-center border-start border-5 border-primary px-3">
                                    <h1 class="flex-shrink-0 display-5 text-primary mb-0" data-toggle="counter-up">100</h1>
                                    <span class="fs-4 text-primary fw-bold me-2">%</span>
                                    <div class="ps-3">
                                        <p class="mb-0">Fraîcheur & Bio</p>
                                        <h6 class="text-uppercase mb-0 fw-bold">Sans intrants chimiques</h6>
                                    </div>
                                </div>
                            </div>
                            <div class="col-sm-6">
                                <div class="d-flex align-items-center border-start border-5 border-primary px-3">
                                    <h1 class="flex-shrink-0 display-5 text-primary mb-0" data-toggle="counter-up">4</h1>
                                    <div class="ps-3">
                                        <p class="mb-0">Pôles Majeurs</p>
                                        <h6 class="text-uppercase mb-0 fw-bold">Ferme, Resto, Traiteur, Formation</h6>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="d-flex gap-3">
                            <a class="btn btn-primary py-3 px-4" href="menu.html"><i class="fa fa-utensils me-2"></i>Découvrir le Menu</a>
                            <a class="btn btn-whatsapp py-3 px-4" href="https://wa.me/22901000000" target="_blank"><i class="fab fa-whatsapp me-2"></i>Échanger avec Nous</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- About End -->

        <!-- Values Section -->
        <div class="container-fluid py-5 bg-light">
            <div class="container">
                <div class="text-center wow fadeInUp" data-wow-delay="0.1s">
                    <h5 class="section-title ff-secondary text-center text-primary fw-normal">Nos Engagements</h5>
                    <h1 class="mb-5">Pourquoi Choisir Saveurs d'Agojiés ?</h1>
                </div>
                <div class="row g-4 text-center">
                    <div class="col-lg-3 col-md-6 wow fadeInUp" data-wow-delay="0.1s">
                        <div class="bg-white rounded p-4 shadow-sm h-100">
                            <div class="btn-square bg-primary text-white rounded-circle mx-auto mb-4" style="width: 64px; height: 64px;">
                                <i class="fa fa-seedling fa-2x"></i>
                            </div>
                            <h5 class="fw-bold">100% Circuit Court</h5>
                            <p class="text-muted small">Les récoltes du matin passent directement de nos champs et viviers à la casserole du chef.</p>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 wow fadeInUp" data-wow-delay="0.3s">
                        <div class="bg-white rounded p-4 shadow-sm h-100">
                            <div class="btn-square bg-primary text-white rounded-circle mx-auto mb-4" style="width: 64px; height: 64px;">
                                <i class="fa fa-drumstick-bite fa-2x"></i>
                            </div>
                            <h5 class="fw-bold">Viandes Nobles</h5>
                            <p class="text-muted small">Élevage fermier éthique : volailles en plein air, moutons de race peulh (Bali-Bali) et poissons nourris sainement.</p>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 wow fadeInUp" data-wow-delay="0.5s">
                        <div class="bg-white rounded p-4 shadow-sm h-100">
                            <div class="btn-square bg-primary text-white rounded-circle mx-auto mb-4" style="width: 64px; height: 64px;">
                                <i class="fa fa-heartbeat fa-2x"></i>
                            </div>
                            <h5 class="fw-bold">Bien-Être & Santé</h5>
                            <p class="text-muted small">Sauces feuilles médicinales (Moringa, Noni, Gboma), huiles pures et jus de fruits pressés à froid sans sucre ajouté.</p>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 wow fadeInUp" data-wow-delay="0.7s">
                        <div class="bg-white rounded p-4 shadow-sm h-100">
                            <div class="btn-square bg-primary text-white rounded-circle mx-auto mb-4" style="width: 64px; height: 64px;">
                                <i class="fa fa-smile fa-2x"></i>
                            </div>
                            <h5 class="fw-bold">Service & Convivialité</h5>
                            <p class="text-muted small">Accueil chaleureux béninois, écoute attentive de vos envies et livraison express soignée à Porto-Novo.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Values End -->

        <!-- Team Start -->
        <div class="container-fluid pt-5 pb-3">
            <div class="container">
                <div class="text-center wow fadeInUp" data-wow-delay="0.1s">
                    <h5 class="section-title ff-secondary text-center text-primary fw-normal">Notre Brigade & Experts</h5>
                    <h1 class="mb-5">Des Hommes et des Femmes Passionnés</h1>
                </div>
                <div class="row g-4">
                    <div class="col-lg-3 col-md-6 wow fadeInUp" data-wow-delay="0.1s">
                        <div class="team-item text-center rounded overflow-hidden shadow-sm border">
                            <div class="rounded-circle overflow-hidden m-4">
                                <img class="img-fluid" src="img/team-1.jpg" alt="Chef Cuisinier" style="width: 200px; height: 200px; object-fit: cover;">
                            </div>
                            <h5 class="mb-0 fw-bold">Chef Joseph D.</h5>
                            <small class="text-muted">Chef Cuisinier & Maître Sauces</small>
                            <div class="d-flex justify-content-center mt-3 mb-4">
                                <a class="btn btn-square btn-primary mx-1" href="https://wa.me/22901000000" target="_blank"><i class="fab fa-whatsapp"></i></a>
                                <a class="btn btn-square btn-primary mx-1" href="#"><i class="fab fa-facebook-f"></i></a>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 wow fadeInUp" data-wow-delay="0.3s">
                        <div class="team-item text-center rounded overflow-hidden shadow-sm border">
                            <div class="rounded-circle overflow-hidden m-4">
                                <img class="img-fluid" src="img/team-2.jpg" alt="Responsable Élevage" style="width: 200px; height: 200px; object-fit: cover;">
                            </div>
                            <h5 class="mb-0 fw-bold">Dah Agodjié</h5>
                            <small class="text-muted">Directeur Ferme & Élevage</small>
                            <div class="d-flex justify-content-center mt-3 mb-4">
                                <a class="btn btn-square btn-primary mx-1" href="https://wa.me/22901000000" target="_blank"><i class="fab fa-whatsapp"></i></a>
                                <a class="btn btn-square btn-primary mx-1" href="#"><i class="fab fa-facebook-f"></i></a>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 wow fadeInUp" data-wow-delay="0.5s">
                        <div class="team-item text-center rounded overflow-hidden shadow-sm border">
                            <div class="rounded-circle overflow-hidden m-4">
                                <img class="img-fluid" src="img/team-3.jpg" alt="Maître Rôtisseur" style="width: 200px; height: 200px; object-fit: cover;">
                            </div>
                            <h5 class="mb-0 fw-bold">Maître Paulin S.</h5>
                            <small class="text-muted">Spécialiste Méchouis & Braisés</small>
                            <div class="d-flex justify-content-center mt-3 mb-4">
                                <a class="btn btn-square btn-primary mx-1" href="https://wa.me/22901000000" target="_blank"><i class="fab fa-whatsapp"></i></a>
                                <a class="btn btn-square btn-primary mx-1" href="#"><i class="fab fa-facebook-f"></i></a>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 wow fadeInUp" data-wow-delay="0.7s">
                        <div class="team-item text-center rounded overflow-hidden shadow-sm border">
                            <div class="rounded-circle overflow-hidden m-4">
                                <img class="img-fluid" src="img/team-4.jpg" alt="Responsable Traiteur" style="width: 200px; height: 200px; object-fit: cover;">
                            </div>
                            <h5 class="mb-0 fw-bold">Awa Mensah</h5>
                            <small class="text-muted">Responsable Service & Réceptions</small>
                            <div class="d-flex justify-content-center mt-3 mb-4">
                                <a class="btn btn-square btn-primary mx-1" href="https://wa.me/22901000000" target="_blank"><i class="fab fa-whatsapp"></i></a>
                                <a class="btn btn-square btn-primary mx-1" href="#"><i class="fab fa-facebook-f"></i></a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Team End -->
    """
    html += html_footer()
    with open(os.path.join(WEB_ROOT, "about.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("✓ about.html written.")

gen_about()

# ==============================================================================
# 3. SERVICE.HTML
# ==============================================================================
def gen_service():
    html = html_head("Nos Services | Saveurs d'Agojiés", "Découvrez nos 4 pôles : Élevage bio, Restauration & Grillades, Traiteur événements et Formations.")
    html += html_nav("service")
    html += html_page_header("Nos Services & Savoir-Faire", "Services")
    html += """
        <!-- Services Start -->
        <div class="container-fluid py-5">
            <div class="container">
                <div class="text-center wow fadeInUp" data-wow-delay="0.1s">
                    <h5 class="section-title ff-secondary text-center text-primary fw-normal">Savoir-Faire d'Excellence</h5>
                    <h1 class="mb-5">4 Métiers au Service du Bon et du Vrai</h1>
                </div>

                <!-- Service 1: Élevage -->
                <div class="row g-5 align-items-center mb-5">
                    <div class="col-lg-6 wow fadeIn" data-wow-delay="0.1s">
                        <img class="img-fluid rounded shadow" src="img/ferme-animaux.jpg" alt="Élevage fermier">
                    </div>
                    <div class="col-lg-6 wow fadeIn" data-wow-delay="0.3s">
                        <span class="badge-gold mb-2 d-inline-block">Pôle Agricole</span>
                        <h2 class="mb-3">Élevage Fermier & Pisciculture Durable</h2>
                        <p class="text-muted">
                            Nous élevons nos animaux dans le plus grand respect du bien-être animal, en plein air et au grand soleil. Volailles de souches nobles (Oies de Chine, Dindes bronzées d'Amérique, Goliath, Pintades), ovins de race peulh (Moutons Bali-Bali, Balami, Oudah) et viviers d'eau douce pour Tilapias, Clarias et alevins calibrés.
                        </p>
                        <ul class="list-unstyled mb-4">
                            <li><i class="fa fa-check text-primary me-2"></i>Nourriture 100% naturelle sans activateurs de croissance</li>
                            <li><i class="fa fa-check text-primary me-2"></i>Vente d'animaux vivants pour élevage ou préparés pour vos fêtes</li>
                            <li><i class="fa fa-check text-primary me-2"></i>Alevins vigoureux triés pour fermes piscicoles</li>
                        </ul>
                        <a href="ferme.html" class="btn btn-primary py-2 px-4"><i class="fa fa-egg me-2"></i>Consulter le Catalogue Ferme</a>
                    </div>
                </div>

                <!-- Service 2: Restauration -->
                <div class="row g-5 align-items-center mb-5 flex-lg-row-reverse">
                    <div class="col-lg-6 wow fadeIn" data-wow-delay="0.1s">
                        <img class="img-fluid rounded shadow" src="img/hero-grill.jpg" alt="Restauration & Grillades">
                    </div>
                    <div class="col-lg-6 wow fadeIn" data-wow-delay="0.3s">
                        <span class="badge-gold mb-2 d-inline-block">Pôle Gastronomie</span>
                        <h2 class="mb-3">Restaurant, Grillades & Rôtisserie au Feu de Bois</h2>
                        <p class="text-muted">
                            Dans une ambiance conviviale et soignée à Porto-Novo, notre table met à l'honneur les trésors culinaires du Bénin. Nos méchouis fondants sont rôtis lentement, nos poissons du vivier braisés à la commande, et nos sauces feuilles cuisinées selon les secrets des aïeules.
                        </p>
                        <ul class="list-unstyled mb-4">
                            <li><i class="fa fa-check text-primary me-2"></i>Plats signatures : Amiwo spécial, Sauté de crabe rouge, Thièpe Djène</li>
                            <li><i class="fa fa-check text-primary me-2"></i>Méchouis d'exception de dinde ou mouton entier sur commande</li>
                            <li><i class="fa fa-check text-primary me-2"></i>Jus de fruits frais pressés à froid sans sucre ajouté</li>
                        </ul>
                        <a href="menu.html" class="btn btn-primary py-2 px-4"><i class="fa fa-utensils me-2"></i>Découvrir la Carte Gourmande</a>
                    </div>
                </div>

                <!-- Service 3: Traiteur -->
                <div class="row g-5 align-items-center mb-5">
                    <div class="col-lg-6 wow fadeIn" data-wow-delay="0.1s">
                        <img class="img-fluid rounded shadow" src="img/traiteur.jpg" alt="Service Traiteur et Événements">
                    </div>
                    <div class="col-lg-6 wow fadeIn" data-wow-delay="0.3s">
                        <span class="badge-gold mb-2 d-inline-block">Pôle Réceptions</span>
                        <h2 class="mb-3">Service Traiteur & Organisation d'Événements</h2>
                        <p class="text-muted">
                            Faites de vos réceptions un moment inoubliable ! Mariages, baptêmes, anniversaires, banquets officiels ou repas d'entreprise : notre brigade traiteur prend tout en charge avec professionnalisme et raffinement.
                        </p>
                        <ul class="list-unstyled mb-4">
                            <li><i class="fa fa-check text-primary me-2"></i>Menus personnalisés adaptés à votre budget et au nombre d'invités</li>
                            <li><i class="fa fa-check text-primary me-2"></i>Animation méchoui en direct & découpe à la broche</li>
                            <li><i class="fa fa-check text-primary me-2"></i>Dressage élégant, vaisselle raffinée et service en salle impeccable</li>
                        </ul>
                        <a href="booking.html" class="btn btn-whatsapp py-2 px-4"><i class="fab fa-whatsapp me-2"></i>Demander un Devis Traiteur</a>
                    </div>
                </div>

                <!-- Service 4: Formation -->
                <div class="row g-5 align-items-center mb-5 flex-lg-row-reverse" id="formations">
                    <div class="col-lg-6 wow fadeIn" data-wow-delay="0.1s">
                        <img class="img-fluid rounded shadow" src="img/formation.jpg" alt="Formations et ateliers">
                    </div>
                    <div class="col-lg-6 wow fadeIn" data-wow-delay="0.3s">
                        <span class="badge-gold mb-2 d-inline-block">Pôle Transmission</span>
                        <h2 class="mb-3">Formations Pratiques & Conseil Agricole</h2>
                        <p class="text-muted">
                            Convaincus que l'agriculture et la cuisine sont des leviers majeurs d'autonomie pour notre jeunesse, nous animons des ateliers pratiques immersifs directement sur notre ferme et dans nos cuisines.
                        </p>
                        <ul class="list-unstyled mb-4">
                            <li><i class="fa fa-check text-primary me-2"></i>Élevage rentable de volailles Goliath et oies de race pure</li>
                            <li><i class="fa fa-check text-primary me-2"></i>Pisciculture moderne en bassins bétonnés et étangs</li>
                            <li><i class="fa fa-check text-primary me-2"></i>Art du service traiteur et maîtrise des sauces traditionnelles</li>
                        </ul>
                        <a href="https://wa.me/22901000000?text=Bonjour%2C%20je%20souhaite%20des%20informations%20sur%20vos%20prochaines%20formations." target="_blank" class="btn btn-primary py-2 px-4"><i class="fa fa-graduation-cap me-2"></i>S'inscrire à une Session</a>
                    </div>
                </div>
            </div>
        </div>
        <!-- Services End -->
    """
    html += html_footer()
    with open(os.path.join(WEB_ROOT, "service.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("✓ service.html written.")

gen_service()

# ==============================================================================
# 4. MENU.HTML
# ==============================================================================
def gen_menu():
    html = html_head("Notre Carte Complète | Saveurs d'Agojiés", "Consultez la carte intégrale de Saveurs d'Agojiés : grillades, méchouis, pâtes traditionnelles, sauces feuilles et boissons artisanales.")
    html += html_nav("menu")
    html += html_page_header("Notre Carte Gastronomique", "Notre Carte")
    
    # Categorize items
    cat1 = [p for p in all_plats if p['categorie_id'] == 1] # Entrées
    cat2 = [p for p in all_plats if p['categorie_id'] == 2] # Grillades
    cat3 = [p for p in all_plats if p['categorie_id'] == 3] # Riz & Couscous
    cat4 = [p for p in all_plats if p['categorie_id'] == 4] # Pâtes
    cat5 = [p for p in all_plats if p['categorie_id'] == 5] # Sauces & Soupes
    cat6 = [p for p in all_plats if p['categorie_id'] == 6] # Tubercules, Salades, Pizzas
    cat_boissons = all_boissons # Boissons & Desserts

    html += """
        <!-- Menu Start -->
        <div class="container-fluid py-5">
            <div class="container">
                <div class="text-center wow fadeInUp" data-wow-delay="0.1s">
                    <h5 class="section-title ff-secondary text-center text-primary fw-normal">Carte & Spécialités</h5>
                    <h1 class="mb-4">Toutes les Saveurs du Terroir Béninois</h1>
                    <p class="text-muted max-w-700 mx-auto mb-5">
                        Chaque plat est cuisiné à la commande avec des ingrédients issus directement de notre ferme et viviers. Commandez en ligne via WhatsApp pour une dégustation sur place ou une livraison express.
                    </p>
                </div>

                <div class="tab-class text-center wow fadeInUp" data-wow-delay="0.1s">
                    <ul class="nav nav-pills d-inline-flex justify-content-center border-bottom mb-5 flex-wrap">
                        <li class="nav-item">
                            <a class="nav-link active" data-bs-toggle="pill" href="#tab-m-grillades">
                                <i class="fa fa-fire me-2"></i>Grillades & Méchouis
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" data-bs-toggle="pill" href="#tab-m-pates">
                                <i class="fa fa-utensils me-2"></i>Pâtes Traditionnelles
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" data-bs-toggle="pill" href="#tab-m-riz">
                                <i class="fa fa-bowl-rice me-2"></i>Riz & Couscous
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" data-bs-toggle="pill" href="#tab-m-sauces">
                                <i class="fa fa-leaf me-2"></i>Sauces & Soupes
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" data-bs-toggle="pill" href="#tab-m-entrees">
                                <i class="fa fa-drumstick-bite me-2"></i>Entrées & Brochettes
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" data-bs-toggle="pill" href="#tab-m-divers">
                                <i class="fa fa-pizza-slice me-2"></i>Salades & Pizzas
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" data-bs-toggle="pill" href="#tab-m-boissons">
                                <i class="fa fa-glass-whiskey me-2"></i>Boissons & Desserts
                            </a>
                        </li>
                    </ul>

                    <div class="tab-content text-start">
                        <!-- Tab Grillades -->
                        <div id="tab-m-grillades" class="tab-pane fade show p-0 active">
                            <h4 class="mb-4 text-primary border-bottom pb-2"><i class="fa fa-fire me-2"></i>Spécialités, Grillades & Méchouis au Feu de Bois</h4>
                            """ + render_dish_grid(cat2) + """
                        </div>

                        <!-- Tab Pâtes -->
                        <div id="tab-m-pates" class="tab-pane fade show p-0">
                            <h4 class="mb-4 text-primary border-bottom pb-2"><i class="fa fa-utensils me-2"></i>Pâtes Béninoises & Plats Traditionnels</h4>
                            """ + render_dish_grid(cat4) + """
                        </div>

                        <!-- Tab Riz -->
                        <div id="tab-m-riz" class="tab-pane fade show p-0">
                            <h4 class="mb-4 text-primary border-bottom pb-2"><i class="fa fa-bowl-rice me-2"></i>Plats de Riz Gourmands & Couscous du Terroir</h4>
                            """ + render_dish_grid(cat3) + """
                        </div>

                        <!-- Tab Sauces -->
                        <div id="tab-m-sauces" class="tab-pane fade show p-0">
                            <h4 class="mb-4 text-primary border-bottom pb-2"><i class="fa fa-leaf me-2"></i>Sauces Feuilles Médicinales & Soupes Bienfaisantes</h4>
                            """ + render_dish_grid(cat5) + """
                        </div>

                        <!-- Tab Entrées -->
                        <div id="tab-m-entrees" class="tab-pane fade show p-0">
                            <h4 class="mb-4 text-primary border-bottom pb-2"><i class="fa fa-drumstick-bite me-2"></i>Entrées Gourmandes, Snacking & Brochettes</h4>
                            """ + render_dish_grid(cat1) + """
                        </div>

                        <!-- Tab Divers -->
                        <div id="tab-m-divers" class="tab-pane fade show p-0">
                            <h4 class="mb-4 text-primary border-bottom pb-2"><i class="fa fa-pizza-slice me-2"></i>Tubercules Sautés, Salades Fraîches & Pizzas Artisanales</h4>
                            """ + render_dish_grid(cat6) + """
                        </div>

                        <!-- Tab Boissons -->
                        <div id="tab-m-boissons" class="tab-pane fade show p-0">
                            <h4 class="mb-4 text-primary border-bottom pb-2"><i class="fa fa-glass-whiskey me-2"></i>Jus Pressés à Froid, Boissons Artisanales & Desserts</h4>
                            """ + render_dish_grid(cat_boissons) + """
                        </div>
                    </div>
                </div>

                <!-- Call to action info -->
                <div class="bg-dark text-white rounded p-5 mt-5 text-center wow fadeInUp" data-wow-delay="0.2s">
                    <h3 class="text-white mb-3">Une envie spécifique ou un événement sur-mesure ?</h3>
                    <p class="mb-4 text-light">Notre chef compose également vos menus traiteur selon vos envies et le nombre de convives.</p>
                    <a href="https://wa.me/22901000000?text=Bonjour%2C%20je%20souhaite%20composer%20un%20menu%20sp%C3%A9cial." target="_blank" class="btn btn-whatsapp py-3 px-5 fs-6">
                        <i class="fab fa-whatsapp me-2"></i>Discuter Directement avec le Chef
                    </a>
                </div>
            </div>
        </div>
        <!-- Menu End -->
    """
    html += html_footer()
    with open(os.path.join(WEB_ROOT, "menu.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("✓ menu.html written.")

gen_menu()

# ==============================================================================
# 5. FERME.HTML
# ==============================================================================
def gen_ferme():
    html = html_head("La Ferme & Produits Frais | Saveurs d'Agojiés", "Achetez les produits bio de notre ferme à Porto-Novo : volailles nobles, moutons peulhs, alevins, arbres fruitiers et miel pur.")
    html += html_nav("ferme")
    html += html_page_header("La Ferme Saveurs d'Agojiés", "La Ferme")

    def render_ferme_cards(items):
        out = '<div class="row g-4">'
        for it in items:
            img_src = get_img(it['slug'], fallback="ferme-animaux.jpg")
            p_formatted = format_price(it['price'], it['unit'])
            w_link = wa_link(it['name'], it['price'], it['unit'])
            out += f"""
                <div class="col-lg-4 col-md-6 wow fadeInUp" data-wow-delay="0.1s">
                    <div class="product-card rounded shadow-sm h-100 d-flex flex-column">
                        <div class="position-relative overflow-hidden">
                            <img class="img-fluid" src="{img_src}" alt="{it['name'].replace("d'Agojie", "d'Agojiés").replace("d'Agojié", "d'Agojiés")}">
                            <span class="badge-gold position-absolute top-0 end-0 m-3 shadow">Bio & Sain</span>
                        </div>
                        <div class="p-4 d-flex flex-column flex-grow-1">
                            <h5 class="fw-bold mb-2">{it['name'].replace("d'Agojie", "d'Agojiés").replace("d'Agojié", "d'Agojiés")}</h5>
                            <p class="text-muted small flex-grow-1 mb-3">{it['description']}</p>
                            <div class="d-flex justify-content-between align-items-center pt-2 border-top">
                                <span class="price-tag">{p_formatted}</span>
                                <a href="{w_link}" target="_blank" class="btn btn-sm btn-whatsapp px-3" title="Commander via WhatsApp">
                                    <i class="fab fa-whatsapp me-1"></i>Commander
                                </a>
                            </div>
                        </div>
                    </div>
                </div>"""
        out += '</div>'
        return out

    elevage = [p for p in all_ferme if p['categorie_id'] == 1]
    pisciculture = [p for p in all_ferme if p['categorie_id'] == 2]
    pepiniere = [p for p in all_ferme if p['categorie_id'] == 3]
    miel_plantes = [p for p in all_ferme if p['categorie_id'] == 4]

    html += """
        <!-- Ferme Start -->
        <div class="container-fluid py-5">
            <div class="container">
                <div class="text-center wow fadeInUp" data-wow-delay="0.1s">
                    <h5 class="section-title ff-secondary text-center text-primary fw-normal">Directement du Producteur</h5>
                    <h1 class="mb-4">Les Produits Frais de Notre Ferme</h1>
                    <p class="text-muted max-w-700 mx-auto mb-5">
                        Commandez directement vos animaux vivants pour l'élevage ou vos fêtes, vos alevins triés, vos plants d'arbres fruitiers greffés et notre miel pur d'abeilles sauvages récolté au cœur des bambousiers.
                    </p>
                </div>

                <div class="tab-class text-center wow fadeInUp" data-wow-delay="0.1s">
                    <ul class="nav nav-pills d-inline-flex justify-content-center border-bottom mb-5 flex-wrap">
                        <li class="nav-item">
                            <a class="nav-link active" data-bs-toggle="pill" href="#tab-f-elevage">
                                <i class="fa fa-egg me-2"></i>Élevage & Volailles Nobles
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" data-bs-toggle="pill" href="#tab-f-pisci">
                                <i class="fa fa-fish me-2"></i>Pisciculture & Alevins
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" data-bs-toggle="pill" href="#tab-f-pepi">
                                <i class="fa fa-seedling me-2"></i>Pépinière & Plants Fruitiers
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" data-bs-toggle="pill" href="#tab-f-miel">
                                <i class="fa fa-jar me-2"></i>Miel Pur & Plantes Bio
                            </a>
                        </li>
                    </ul>

                    <div class="tab-content text-start">
                        <!-- Tab Elevage -->
                        <div id="tab-f-elevage" class="tab-pane fade show p-0 active">
                            <h4 class="mb-4 text-primary border-bottom pb-2"><i class="fa fa-egg me-2"></i>Élevage plein air : Oies, Dindes, Goliath, Moutons Peulhs, Lapins</h4>
                            """ + render_ferme_cards(elevage) + """
                        </div>

                        <!-- Tab Pisci -->
                        <div id="tab-f-pisci" class="tab-pane fade show p-0">
                            <h4 class="mb-4 text-primary border-bottom pb-2"><i class="fa fa-fish me-2"></i>Aquaculture : Poissons marchands et alevins vigoureux</h4>
                            """ + render_ferme_cards(pisciculture) + """
                        </div>

                        <!-- Tab Pepi -->
                        <div id="tab-f-pepi" class="tab-pane fade show p-0">
                            <h4 class="mb-4 text-primary border-bottom pb-2"><i class="fa fa-seedling me-2"></i>Pépinière : Arbres fruitiers greffés et plants d'avenir</h4>
                            """ + render_ferme_cards(pepiniere) + """
                        </div>

                        <!-- Tab Miel -->
                        <div id="tab-f-miel" class="tab-pane fade show p-0">
                            <h4 class="mb-4 text-primary border-bottom pb-2"><i class="fa fa-leaf me-2"></i>Apiculture & Herbes aromatiques fraîches</h4>
                            """ + render_ferme_cards(miel_plantes) + """
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Ferme End -->
    """
    html += html_footer()
    with open(os.path.join(WEB_ROOT, "ferme.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("✓ ferme.html written.")

gen_ferme()

# ==============================================================================
# 6. BOOKING.HTML
# ==============================================================================
def gen_booking():
    html = html_head("Réservation & Devis | Saveurs d'Agojiés", "Réservez votre table, commandez un méchoui d'exception ou demandez un devis traiteur à Porto-Novo.")
    html += html_nav("booking")
    html += html_page_header("Réservation de Table & Commandes", "Réservation")
    html += """
        <!-- Booking Start -->
        <div class="container-fluid py-5">
            <div class="container">
                <div class="text-center wow fadeInUp" data-wow-delay="0.1s">
                    <h5 class="section-title ff-secondary text-center text-primary fw-normal">Service Réservation</h5>
                    <h1 class="mb-5">Planifiez Votre Déjeuner, Dîner ou Événement</h1>
                </div>

                <div class="row g-5">
                    <div class="col-lg-6 wow fadeInUp" data-wow-delay="0.1s">
                        <div class="bg-light rounded p-5 h-100 border">
                            <h3 class="mb-4 text-primary">Informations Pratiques</h3>
                            <div class="d-flex mb-4">
                                <div class="btn-square bg-primary text-white rounded-circle flex-shrink-0 me-3">
                                    <i class="fa fa-clock"></i>
                                </div>
                                <div>
                                    <h5 class="fw-bold mb-1">Horaires de Service</h5>
                                    <p class="text-muted mb-0">Restaurant ouvert 7j/7 de 08h00 à 22h00. Livraisons de 11h00 à 21h30.</p>
                                </div>
                            </div>
                            <div class="d-flex mb-4">
                                <div class="btn-square bg-primary text-white rounded-circle flex-shrink-0 me-3">
                                    <i class="fa fa-fire"></i>
                                </div>
                                <div>
                                    <h5 class="fw-bold mb-1">Méchouis & Grands Banquets</h5>
                                    <p class="text-muted mb-0">Pour un méchoui entier (dinde ou mouton de race peulh), merci de réserver 24h à l'avance afin de garantir un marinage et un rôtissage lents.</p>
                                </div>
                            </div>
                            <div class="d-flex mb-4">
                                <div class="btn-square bg-primary text-white rounded-circle flex-shrink-0 me-3">
                                    <i class="fa fa-truck"></i>
                                </div>
                                <div>
                                    <h5 class="fw-bold mb-1">Livraison Express</h5>
                                    <p class="text-muted mb-0">Livraison soignée à votre domicile ou bureau sur Porto-Novo et environs immédiats.</p>
                                </div>
                            </div>
                            <div class="d-flex">
                                <div class="btn-square bg-primary text-white rounded-circle flex-shrink-0 me-3">
                                    <i class="fab fa-whatsapp"></i>
                                </div>
                                <div>
                                    <h5 class="fw-bold mb-1">Ligne Directe WhatsApp</h5>
                                    <p class="text-muted mb-0">+229 01 00 00 00 (Réponse rapide assurée)</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-lg-6 wow fadeInUp" data-wow-delay="0.3s">
                        <div class="bg-dark text-white rounded p-5">
                            <h3 class="text-white mb-4">Formulaire de Réservation</h3>
                            <form onsubmit="event.preventDefault(); submitBook();">
                                <div class="row g-3">
                                    <div class="col-md-6">
                                        <div class="form-floating">
                                            <input type="text" class="form-control" id="bkName" placeholder="Votre Nom" required>
                                            <label for="bkName" class="text-dark">Votre Nom</label>
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div class="form-floating">
                                            <input type="tel" class="form-control" id="bkPhone" placeholder="Téléphone / WhatsApp" required>
                                            <label for="bkPhone" class="text-dark">Téléphone / WhatsApp</label>
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div class="form-floating">
                                            <input type="datetime-local" class="form-control" id="bkDatetime" required>
                                            <label for="bkDatetime" class="text-dark">Date & Heure</label>
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div class="form-floating">
                                            <select class="form-select" id="bkGuests">
                                                <option value="1 à 2 personnes">1 à 2 personnes</option>
                                                <option value="3 à 5 personnes">3 à 5 personnes</option>
                                                <option value="6 à 10 personnes">6 à 10 personnes</option>
                                                <option value="Événement (+10 personnes)">Événement (+10 personnes)</option>
                                            </select>
                                            <label for="bkGuests" class="text-dark">Nombre de Personnes</label>
                                        </div>
                                    </div>
                                    <div class="col-12">
                                        <div class="form-floating">
                                            <select class="form-select" id="bkService">
                                                <option value="Table Restaurant">Table au restaurant</option>
                                                <option value="Commande Méchoui Entier">Commande Méchoui Entier (Dinde/Mouton)</option>
                                                <option value="Livraison Express Déjeuner/Dîner">Livraison repas au bureau/domicile</option>
                                                <option value="Service Traiteur Événement">Prestation Traiteur (Mariage, Fête...)</option>
                                            </select>
                                            <label for="bkService" class="text-dark">Type de Prestation</label>
                                        </div>
                                    </div>
                                    <div class="col-12">
                                        <div class="form-floating">
                                            <textarea class="form-control" placeholder="Demande particulière" id="bkMessage" style="height: 100px"></textarea>
                                            <label for="bkMessage" class="text-dark">Précisions (plats préférés, adresse si livraison...)</label>
                                        </div>
                                    </div>
                                    <div class="col-12">
                                        <button class="btn btn-whatsapp w-100 py-3 fs-6" type="submit">
                                            <i class="fab fa-whatsapp me-2"></i>Envoyer la Réservation via WhatsApp
                                        </button>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <script>
        function submitBook() {
            var n = document.getElementById('bkName').value;
            var p = document.getElementById('bkPhone').value;
            var d = document.getElementById('bkDatetime').value;
            var g = document.getElementById('bkGuests').value;
            var s = document.getElementById('bkService').value;
            var m = document.getElementById('bkMessage').value;
            var txt = "*Réservation Saveurs d'Agojiés*%0A%0A" +
                      "👤 *Nom :* " + encodeURIComponent(n) + "%0A" +
                      "📞 *Tél :* " + encodeURIComponent(p) + "%0A" +
                      "📅 *Date :* " + encodeURIComponent(d) + "%0A" +
                      "👥 *Personnes :* " + encodeURIComponent(g) + "%0A" +
                      "🍽️ *Prestation :* " + encodeURIComponent(s) + "%0A" +
                      (m ? "📝 *Notes :* " + encodeURIComponent(m) + "%0A" : "");
            window.open("https://wa.me/22901000000?text=" + txt, "_blank");
        }
        </script>
        <!-- Booking End -->
    """
    html += html_footer()
    with open(os.path.join(WEB_ROOT, "booking.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("✓ booking.html written.")

gen_booking()

# ==============================================================================
# 7. TEAM.HTML
# ==============================================================================
def gen_team():
    html = html_head("Notre Équipe | Saveurs d'Agojiés", "Rencontrez la brigade et les experts passionnés de Saveurs d'Agojiés à Porto-Novo.")
    html += html_nav("team")
    html += html_page_header("Notre Brigade & Experts", "Notre Équipe")
    html += """
        <!-- Team Start -->
        <div class="container-fluid py-5">
            <div class="container">
                <div class="text-center wow fadeInUp" data-wow-delay="0.1s">
                    <h5 class="section-title ff-secondary text-center text-primary fw-normal">Maîtres Artisans</h5>
                    <h1 class="mb-5">La Passion du Goût et de la Terre</h1>
                </div>

                <div class="row g-4">
                    <div class="col-lg-3 col-md-6 wow fadeInUp" data-wow-delay="0.1s">
                        <div class="team-item text-center rounded overflow-hidden shadow-sm border h-100 d-flex flex-column">
                            <div class="rounded-circle overflow-hidden m-4 mx-auto" style="width: 200px; height: 200px;">
                                <img class="img-fluid w-100 h-100" src="img/team-1.jpg" alt="Chef Cuisinier" style="object-fit: cover;">
                            </div>
                            <div class="p-4 pt-0 d-flex flex-column flex-grow-1">
                                <h5 class="mb-1 fw-bold">Chef Joseph D.</h5>
                                <small class="text-primary fw-bold mb-3 d-block">Chef Exécutif & Maître Sauces</small>
                                <p class="text-muted small flex-grow-1">Fort de 15 années en gastronomie locale, le Chef Joseph magnifie les produits bruts de notre ferme en sauces onctueuses et pâtes traditionnelles parfaites.</p>
                                <div class="d-flex justify-content-center">
                                    <a class="btn btn-square btn-whatsapp mx-1" href="https://wa.me/22901000000" target="_blank"><i class="fab fa-whatsapp"></i></a>
                                    <a class="btn btn-square btn-primary mx-1" href="#"><i class="fab fa-facebook-f"></i></a>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-lg-3 col-md-6 wow fadeInUp" data-wow-delay="0.3s">
                        <div class="team-item text-center rounded overflow-hidden shadow-sm border h-100 d-flex flex-column">
                            <div class="rounded-circle overflow-hidden m-4 mx-auto" style="width: 200px; height: 200px;">
                                <img class="img-fluid w-100 h-100" src="img/team-2.jpg" alt="Directeur Élevage" style="object-fit: cover;">
                            </div>
                            <div class="p-4 pt-0 d-flex flex-column flex-grow-1">
                                <h5 class="mb-1 fw-bold">Dah Agodjié</h5>
                                <small class="text-primary fw-bold mb-3 d-block">Directeur Ferme & Aquaculture</small>
                                <p class="text-muted small flex-grow-1">Agro-pasteur chevronné, il veille au bien-être des troupeaux, à la pureté des souches de volailles et à la santé de nos bassins piscicoles.</p>
                                <div class="d-flex justify-content-center">
                                    <a class="btn btn-square btn-whatsapp mx-1" href="https://wa.me/22901000000" target="_blank"><i class="fab fa-whatsapp"></i></a>
                                    <a class="btn btn-square btn-primary mx-1" href="#"><i class="fab fa-facebook-f"></i></a>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-lg-3 col-md-6 wow fadeInUp" data-wow-delay="0.5s">
                        <div class="team-item text-center rounded overflow-hidden shadow-sm border h-100 d-flex flex-column">
                            <div class="rounded-circle overflow-hidden m-4 mx-auto" style="width: 200px; height: 200px;">
                                <img class="img-fluid w-100 h-100" src="img/team-3.jpg" alt="Maître Rôtisseur" style="object-fit: cover;">
                            </div>
                            <div class="p-4 pt-0 d-flex flex-column flex-grow-1">
                                <h5 class="mb-1 fw-bold">Maître Paulin S.</h5>
                                <small class="text-primary fw-bold mb-3 d-block">Chef Rôtisseur & Grillades</small>
                                <p class="text-muted small flex-grow-1">Le maître absolu du feu de bois et de la broche. Il maîtrise le temps de cuisson parfait pour des méchouis fondants à cœur et croustillants en surface.</p>
                                <div class="d-flex justify-content-center">
                                    <a class="btn btn-square btn-whatsapp mx-1" href="https://wa.me/22901000000" target="_blank"><i class="fab fa-whatsapp"></i></a>
                                    <a class="btn btn-square btn-primary mx-1" href="#"><i class="fab fa-facebook-f"></i></a>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-lg-3 col-md-6 wow fadeInUp" data-wow-delay="0.7s">
                        <div class="team-item text-center rounded overflow-hidden shadow-sm border h-100 d-flex flex-column">
                            <div class="rounded-circle overflow-hidden m-4 mx-auto" style="width: 200px; height: 200px;">
                                <img class="img-fluid w-100 h-100" src="img/team-4.jpg" alt="Responsable Traiteur" style="object-fit: cover;">
                            </div>
                            <div class="p-4 pt-0 d-flex flex-column flex-grow-1">
                                <h5 class="mb-1 fw-bold">Awa Mensah</h5>
                                <small class="text-primary fw-bold mb-3 d-block">Responsable Service & Réceptions</small>
                                <p class="text-muted small flex-grow-1">Avec une rigueur sans faille et un sens inné du détail, Awa coordonne nos équipes en salle et assure le succès de chaque cérémonie traiteur.</p>
                                <div class="d-flex justify-content-center">
                                    <a class="btn btn-square btn-whatsapp mx-1" href="https://wa.me/22901000000" target="_blank"><i class="fab fa-whatsapp"></i></a>
                                    <a class="btn btn-square btn-primary mx-1" href="#"><i class="fab fa-facebook-f"></i></a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Team End -->
    """
    html += html_footer()
    with open(os.path.join(WEB_ROOT, "team.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("✓ team.html written.")

gen_team()

# ==============================================================================
# 8. TESTIMONIAL.HTML
# ==============================================================================
def gen_testimonial():
    html = html_head("Témoignages & Livre d'Or | Saveurs d'Agojiés", "Consultez les retours d'expérience et avis authentiques de nos clients à Porto-Novo et Cotonou.")
    html += html_nav("testimonial")
    html += html_page_header("Ce Que Disent Nos Clients", "Témoignages")
    html += """
        <!-- Testimonial Start -->
        <div class="container-fluid py-5 wow fadeInUp" data-wow-delay="0.1s">
            <div class="container">
                <div class="text-center">
                    <h5 class="section-title ff-secondary text-center text-primary fw-normal">Livre d'Or</h5>
                    <h1 class="mb-5">Avis & Expériences Partagées</h1>
                </div>

                <!-- Carousel -->
                <div class="owl-carousel testimonial-carousel mb-5">
                    <div class="testimonial-item bg-transparent border rounded p-4 shadow-sm">
                        <i class="fa fa-quote-left fa-2x text-primary mb-3"></i>
                        <p class="fst-italic text-muted">« L'Amiwo au poulet fermier est une véritable madeleine de Proust. La viande est tendre, parfumée et les sauces ont ce goût authentique inimitable. Service très soigné ! »</p>
                        <div class="d-flex align-items-center">
                            <img class="img-fluid flex-shrink-0 rounded-circle" src="img/testimonial-1.jpg" style="width: 50px; height: 50px; object-fit: cover;">
                            <div class="ps-3">
                                <h5 class="mb-1 fw-bold">Séverin K.</h5>
                                <small>Cadre Bancaire, Porto-Novo</small>
                            </div>
                        </div>
                    </div>
                    <div class="testimonial-item bg-transparent border rounded p-4 shadow-sm">
                        <i class="fa fa-quote-left fa-2x text-primary mb-3"></i>
                        <p class="fst-italic text-muted">« Pour le mariage de notre fille (180 personnes), Saveurs d'Agojiés a assuré un méchoui de mouton et des poissons braisés spectaculaires. Tout le monde en parle encore. Bravo ! »</p>
                        <div class="d-flex align-items-center">
                            <img class="img-fluid flex-shrink-0 rounded-circle" src="img/testimonial-2.jpg" style="width: 50px; height: 50px; object-fit: cover;">
                            <div class="ps-3">
                                <h5 class="mb-1 fw-bold">Béatrice H.</h5>
                                <small>Organisatrice d'Événements</small>
                            </div>
                        </div>
                    </div>
                    <div class="testimonial-item bg-transparent border rounded p-4 shadow-sm">
                        <i class="fa fa-quote-left fa-2x text-primary mb-3"></i>
                        <p class="fst-italic text-muted">« Leurs jus pressés à froid sans sucre ajouté et leur miel pur de bambousier sont incomparables. On sent immédiatement la fraîcheur de la ferme. »</p>
                        <div class="d-flex align-items-center">
                            <img class="img-fluid flex-shrink-0 rounded-circle" src="img/testimonial-3.jpg" style="width: 50px; height: 50px; object-fit: cover;">
                            <div class="ps-3">
                                <h5 class="mb-1 fw-bold">Dr. Marc G.</h5>
                                <small>Médecin Nutritionniste</small>
                            </div>
                        </div>
                    </div>
                    <div class="testimonial-item bg-transparent border rounded p-4 shadow-sm">
                        <i class="fa fa-quote-left fa-2x text-primary mb-3"></i>
                        <p class="fst-italic text-muted">« Livraison express et plats toujours bien chauds au bureau. Le sauté de crabe et le riz gras garni à la viande de lapin sont une pure merveille culinaire. »</p>
                        <div class="d-flex align-items-center">
                            <img class="img-fluid flex-shrink-0 rounded-circle" src="img/testimonial-4.jpg" style="width: 50px; height: 50px; object-fit: cover;">
                            <div class="ps-3">
                                <h5 class="mb-1 fw-bold">Fatou D.</h5>
                                <small>Directrice d'Agence, Cotonou</small>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Additional Grid Reviews -->
                <div class="row g-4 pt-4">
                    <div class="col-md-6 wow fadeInUp" data-wow-delay="0.1s">
                        <div class="bg-light p-4 rounded border h-100">
                            <div class="d-flex text-warning mb-2">
                                <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                            </div>
                            <h5 class="fw-bold">« Les poissons braisés les plus frais de Porto-Novo »</h5>
                            <p class="text-muted fst-italic">« Pêchés directement dans leurs viviers et assaisonnés d'épices douces, c'est un vrai régal en famille chaque dimanche midi. »</p>
                            <small class="fw-bold text-dark">— Innocent A., Enseignant</small>
                        </div>
                    </div>
                    <div class="col-md-6 wow fadeInUp" data-wow-delay="0.3s">
                        <div class="bg-light p-4 rounded border h-100">
                            <div class="d-flex text-warning mb-2">
                                <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i>
                            </div>
                            <h5 class="fw-bold">« Des volailles nobles introuvables sur les marchés »</h5>
                            <p class="text-muted fst-italic">« J'ai commandé des oies de Chine et des pintades pour les fêtes de fin d'année. Poids généreux, santé irréprochable et conseils d'élevage très pros. »</p>
                            <small class="fw-bold text-dark">— Mireille T., Entrepreneure</small>
                        </div>
                    </div>
                </div>

                <div class="text-center mt-5">
                    <a href="https://wa.me/22901000000?text=Bonjour%20Saveurs%20d%27Agoji%C3%A9%2C%20je%20souhaite%20vous%20laisser%20un%20avis." target="_blank" class="btn btn-whatsapp py-3 px-4">
                        <i class="fab fa-whatsapp me-2"></i>Laisser Votre Témoignage
                    </a>
                </div>
            </div>
        </div>
        <!-- Testimonial End -->
    """
    html += html_footer()
    with open(os.path.join(WEB_ROOT, "testimonial.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("✓ testimonial.html written.")

gen_testimonial()

# ==============================================================================
# 9. CONTACT.HTML
# ==============================================================================
def gen_contact():
    html = html_head("Contact & Accès | Saveurs d'Agojiés", "Contactez Saveurs d'Agojiés à Porto-Novo : coordonnées, localisation, formulaire et commande express WhatsApp.")
    html += html_nav("contact")
    html += html_page_header("Contactez Saveurs d'Agojiés", "Contact")
    html += """
        <!-- Contact Start -->
        <div class="container-fluid py-5">
            <div class="container">
                <div class="text-center wow fadeInUp" data-wow-delay="0.1s">
                    <h5 class="section-title ff-secondary text-center text-primary fw-normal">Nous Joindre</h5>
                    <h1 class="mb-5">À Votre Écoute Pour Toute Question</h1>
                </div>
                <div class="row g-4 mb-5">
                    <div class="col-md-4 wow fadeInUp" data-wow-delay="0.1s">
                        <div class="bg-light rounded p-4 text-center border h-100">
                            <div class="btn-square bg-primary text-white rounded-circle mx-auto mb-3">
                                <i class="fa fa-map-marker-alt"></i>
                            </div>
                            <h5 class="fw-bold">Adresse & Ferme</h5>
                            <p class="text-muted mb-0">Porto-Novo, République du Bénin</p>
                        </div>
                    </div>
                    <div class="col-md-4 wow fadeInUp" data-wow-delay="0.3s">
                        <div class="bg-light rounded p-4 text-center border h-100">
                            <div class="btn-square bg-whatsapp text-white rounded-circle mx-auto mb-3">
                                <i class="fab fa-whatsapp"></i>
                            </div>
                            <h5 class="fw-bold">WhatsApp & Commandes</h5>
                            <p class="text-muted mb-0">+229 01 00 00 00</p>
                        </div>
                    </div>
                    <div class="col-md-4 wow fadeInUp" data-wow-delay="0.5s">
                        <div class="bg-light rounded p-4 text-center border h-100">
                            <div class="btn-square bg-primary text-white rounded-circle mx-auto mb-3">
                                <i class="fa fa-envelope-open"></i>
                            </div>
                            <h5 class="fw-bold">Courrier Électronique</h5>
                            <p class="text-muted mb-0">contact@saveurs-dagojies.com</p>
                        </div>
                    </div>
                </div>

                <div class="row g-4">
                    <div class="col-md-6 wow fadeIn" data-wow-delay="0.1s">
                        <iframe class="position-relative rounded w-100 h-100 shadow-sm"
                            src="https://maps.google.com/maps?q=Porto-Novo,%20Benin&t=&z=14&ie=UTF8&iwloc=&output=embed"
                            frameborder="0" style="min-height: 400px; border:0;" allowfullscreen="" aria-hidden="false"
                            tabindex="0"></iframe>
                    </div>
                    <div class="col-md-6">
                        <div class="wow fadeInUp" data-wow-delay="0.2s">
                            <h3 class="mb-4">Envoyez-Nous un Message</h3>
                            <form onsubmit="event.preventDefault(); submitContact();">
                                <div class="row g-3">
                                    <div class="col-md-6">
                                        <div class="form-floating">
                                            <input type="text" class="form-control" id="ctName" placeholder="Votre Nom" required>
                                            <label for="ctName">Votre Nom</label>
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div class="form-floating">
                                            <input type="tel" class="form-control" id="ctPhone" placeholder="Téléphone / WhatsApp" required>
                                            <label for="ctPhone">Téléphone / WhatsApp</label>
                                        </div>
                                    </div>
                                    <div class="col-12">
                                        <div class="form-floating">
                                            <select class="form-select" id="ctSubject">
                                                <option value="Commande de Repas">Commande de Repas</option>
                                                <option value="Produits de la Ferme">Achat Animaux / Alevins / Plants</option>
                                                <option value="Devis Traiteur & Événement">Devis Traiteur & Réception</option>
                                                <option value="Inscription Formation">Inscription Formation</option>
                                                <option value="Autre demande">Autre demande</option>
                                            </select>
                                            <label for="ctSubject">Objet du Message</label>
                                        </div>
                                    </div>
                                    <div class="col-12">
                                        <div class="form-floating">
                                            <textarea class="form-control" placeholder="Votre Message" id="ctMessage" style="height: 150px" required></textarea>
                                            <label for="ctMessage">Votre Message</label>
                                        </div>
                                    </div>
                                    <div class="col-12">
                                        <button class="btn btn-whatsapp w-100 py-3 fs-6" type="submit">
                                            <i class="fab fa-whatsapp me-2"></i>Envoyer via WhatsApp
                                        </button>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <script>
        function submitContact() {
            var n = document.getElementById('ctName').value;
            var p = document.getElementById('ctPhone').value;
            var s = document.getElementById('ctSubject').value;
            var m = document.getElementById('ctMessage').value;
            var txt = "*Message Saveurs d'Agojiés*%0A%0A" +
                      "👤 *Nom :* " + encodeURIComponent(n) + "%0A" +
                      "📞 *Tél :* " + encodeURIComponent(p) + "%0A" +
                      "📌 *Objet :* " + encodeURIComponent(s) + "%0A" +
                      "💬 *Message :* " + encodeURIComponent(m);
            window.open("https://wa.me/22901000000?text=" + txt, "_blank");
        }
        </script>
        <!-- Contact End -->
    """
    html += html_footer()
    with open(os.path.join(WEB_ROOT, "contact.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("✓ contact.html written.")

gen_contact()
print("All 9 pages generated successfully!")
