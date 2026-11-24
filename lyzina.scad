// =====================================================================
//  Lyzina (kolejnice) supliku - parametricky model pro 3D tisk
//  Jednotky: mm. Upravte parametry nize a exportujte STL (F6, F7).
// =====================================================================

/* [Hlavni rozmery] */
delka          = 200;   // celkova vnejsi delka vcetne oblych koncu
sirka_zadni    = 16;    // vnejsi sirka zadni (spodni) strany
sirka_predni   = 15;    // vnejsi sirka na otevrene predni strane
vyska_bok      = 8;     // vyska bocni steny
tloustka       = 2;     // tloustka plastu (dno i steny)
r_konec        = 6;     // vnejsi polomer zaobleni koncu (pudorys)

/* [Vystupky (cepy se skrutkou)] */
vystupek_od_praveho_1 = 20;   // stred 1. vystupku od praveho konce
rozestup_1_2          = 97;   // stred 2. vystupku od 1. vystupku
vystupek_od_leveho_3  = 20;   // stred 3. vystupku od leveho konce
vystupek_vyska        = 7;    // vyska vystupku nad zadni plochou
vystupek_prumer       = 8;    // vnejsi prumer vystupku
dira_prumer           = 3;    // prumer diry pro sroub (pro tisk spise 3.2-3.4)
patka_zesileni        = 0.5;  // kuzelove zesileni paty vystupku (0 = vypnuto)
srazeni_spicky        = 0.5;  // sraz hrany na konci vystupku

/* [Tisk] */
tiskova_orientace = true;  // true = otevrena strana na podlozce, vystupky nahoru
$fn = 64;

// ---------------------------------------------------------------------
zuzeni = (sirka_zadni - sirka_predni) / 2;   // ubytek na kazde strane (0.5)
e = 0.01;

module obrys(off=0) {               // pudorys - obdelnik se zaoblenymi konci
    offset(delta=off)
        offset(r=r_konec) offset(delta=-r_konec)
            translate([0, -sirka_zadni/2]) square([delka, sirka_zadni]);
}

module plast(z0, z1, off0, off1) {   // zkoseny "hranol" mezi dvema obrysy
    hull() {
        translate([0,0,z0]) linear_extrude(e) obrys(off0);
        translate([0,0,z1-e]) linear_extrude(e) obrys(off1);
    }
}

function off_v(z) = -zuzeni * z / vyska_bok;  // vnejsi odsazeni v dane vysce

pozice = [ delka - vystupek_od_praveho_1,
           delka - vystupek_od_praveho_1 - rozestup_1_2,
           vystupek_od_leveho_3 ];

module vystupek() {
    // vystupek smeruje do -Z (ze zadni strany ven)
    translate([0,0,-vystupek_vyska]) {
        cylinder(d=vystupek_prumer - 2*srazeni_spicky, h=srazeni_spicky+e);
        translate([0,0,srazeni_spicky])
            cylinder(d=vystupek_prumer, h=vystupek_vyska - srazeni_spicky + e);
    }
    if (patka_zesileni > 0)
        translate([0,0,-patka_zesileni])
            cylinder(d1=vystupek_prumer, d2=vystupek_prumer + 2*patka_zesileni,
                     h=patka_zesileni + e);
}

module lyzina() {
    difference() {
        union() {
            // vnejsi tvar: zadni strana z=0 (16 mm), predni z=vyska_bok (15 mm)
            plast(0, vyska_bok, 0, off_v(vyska_bok));
            for (x = pozice) translate([x, 0, 0]) vystupek();
        }
        // vnitrni dutina (tloustka steny 2 mm kolmo na zkosenou stenu)
        plast(tloustka, vyska_bok + 1,
              off_v(tloustka) - tloustka, off_v(vyska_bok + 1) - tloustka);
        // diry pro sroub skrz vystupek i dno
        for (x = pozice)
            translate([x, 0, -vystupek_vyska - 1])
                cylinder(d=dira_prumer, h=vystupek_vyska + tloustka + 2);
    }
}

if (tiskova_orientace)
    translate([0,0,vyska_bok]) rotate([180,0,0]) lyzina();
else
    lyzina();
