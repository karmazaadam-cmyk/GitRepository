poziom = 1
ok = 0
siłe = 0
zręczność = 0
inteligencje = 0
charyzme = 0
percepcje = 0
print("Pisz wszystko łącznie")
print("Zagrajmy w Dungeons and Dragons")
while ok == 0:
    najlepsza_statystyka = str(input("jaka statystyka jest dla ciebie najważniejsza? Wybierz z siła, zręczność, zdrowie, inteligencja, percepcja i charyzma"))
    najlepsza_statystyka = najlepsza_statystyka.upper()
    najlepsza_statystyka = najlepsza_statystyka.strip()
    ok = 1
    if najlepsza_statystyka == "SIŁA":
        print("To masz do wyboru górskiego krasnoluda(+2 do siły + 2 do zdrowia)")
        print("człowieka(+1 do wszystkiego)")
        print("dragonborna(+2 do siły +1 do charyzmy)")
        print("pół elf(+2 do charyzmy oraz +1 do dwóch wybranych artybutów)") 
        print("pół ork (+2 do siły +1 do zdrowia)")
    elif najlepsza_statystyka == "ZRĘCZNOŚĆ":
        print("To masz do wyboru człowieka(+1 do wszystkiego)")
        print("pół elf(+2 do charyzmy oraz +1 do dwóch wybranych artybutów)")
        print("elf wysoki(+2 do zręczności +1 do inteligencji)")
        print("elf leśny(+2 do zręczności +1 percepcepcja)")        
        print("niziołek lekkostopy(+2 do zręczności +1 charyzma)")
        print("gruby niziołek(+2 do zręczności +1 zdrowie)") 
    elif najlepsza_statystyka == "ZDROWIE":
        print("To masz do wyboru człowieka(+1 do wszystkiego)")
        print("pół elf(+2 do charyzmy oraz +1 do dwóch wybranych artybutów)")
        print("gruby niziołek(+2 do zręczności +1 zdrowie)")
        print("Krasnolud górski(+2 do zdrowia +2 do siły)")
        print("Krasnolód wzgórz(+2 do zdrowia +1 do percepcji)")
        print("gnom (+2 do inteligencji +1 zdrowia)")
        print("pół ork(+2 do siły +1 do zdowia)")
    elif najlepsza_statystyka == "INTELIGENCJA":
        print("To masz do wyboru człowieka(+1 do wszystkiego)")
        print("pół elf(+2 do charyzmy oraz +1 do dwóch wybranych artybutów)")
        print("elf wysoki(+2 do zręczności +1 inteligencja)")
        print("gnom (+2 do inteligencji +1 zdrowia)")
        print("tiefling (+1 do inteligencji +2 do haryzmy)")  
    elif najlepsza_statystyka == "PERCEPCJA":
        print("To masz do wyboru człowieka(+1 do wszystkiego)")
        print("pół elf(+2 do charyzmy oraz +1 do dwóch wybranych artybutów)")
        print("elf leśny(+2 do zręczności +1 do percepcji)")
    elif najlepsza_statystyka == "CHARYZMA":
        print("To masz do wyboru człowieka(+1 do wszystkiego)")
        print("pół elf(+2 do charyzmy oraz +1 do dwóch wybranych artybutów)")
        print("tiefling (+1 do inteligencji +2 do haryzmy)")
        print("niziołki lekkostope(+2 do zręczności +1 do charyzmy)") 
        print("dragonborn(+2 do siły +1 do charyzmy)") 
    else:
        print("Abo nie ma tego albo zrobiłeś literówke spróbuj ponownie")
        ok = 0
ok = 0
while ok == 0:
    rasa = str(input("To jaką rase wybierasz wybierasz?                   ")) 
    rasa = rasa.upper()
    ok = 1
    rasa = rasa.strip()
    if rasa == "KRASNOLÓD":
        print("To masz do wyboru górskiego krasnoluda(+2 do siły + 2 do zdrowia)")
        print("oraz krasnolóda wzgórzowy(+2 do siły +1 do percepcji)")
    elif rasa == "ELF":
        print("To masz do wyboru wysokiego elfa(+2 do zręczności + 1 do inteligencji)")
        print("oraz elf leśny(+2 do zręczności +1 do percepcji)")
    elif rasa == "NIZIOŁEK":
        print("To masz do wyboru niziołka lekkostoppa(+2 do     zręczności + 1 do charyzmy)")
        print("oraz niziołka grubego(+2 do zręczności +1 do zdrowia)")
    elif rasa == "CZŁOWIEK":
        print("To masz +1 do wszystkiego")
    elif rasa == "DRAGONBORN":
        print("Jaki smoczy oddech wybierasz?")
        print("To masz +2 do siły i +1 do charyzmy")
        print("Czarny	Kwas	Linia 5 na 30 stóp (Rzut obronny na    Zręczność)")
        print("Niebieski	Błyskawica	Linia 5 na 30 stóp (Rzut obronny na Zręczność)")                             
        print("Mosiądz	Ogień	Linia 5 na 30 stóp (Rzut obronny na    Zręczność)")                                        
        print("Brązowy	Błyskawica	Linia 5 na 30 stóp (Rzut obronny na Zręczność)")                          
        print("Miedź	Kwas	Linia 5 na 30 stóp (Rzut obronny na Zręczność)")
        print("Złoto	Ogień	Stożek 15 stóp (Rzut obronny zręczności)")
        print("Zielony	Trucizna	Stożek 15 stóp (obrona kon.)")
        print("Czerwony	Ogień	Stożek 15 stóp (Rzut obronny zręczności)")    
        print("Srebrny	Zimno	Stożek 15 stóp (obrona kon.)") 
        print("Biały	Zimno	Stożek 15 stóp (obrona kon.)")
        umiejętnośćR = str(input("Jaki smoczy oddech wybierasz?(Będziesz odporny na ten rodzaj obrażeń)")).strip().upper()
    elif rasa == "PÓŁELF":
        print("To masz +2 do charyzmy oraz +1 do dwóch wybranych artybutów")
    elif rasa == "GNOM":
        print("To masz +2 do inteligencji oraz +1 do zdrowia")
    elif rasa == "PÓŁORK":
        print("To masz +2 do siły oraz +1 do zdrowia")
    elif rasa == "TIEFLING":
        print("To masz +2 do charyzmy oraz +1 do inteligencji    (Jesteś ognio odporny)")
    else:
        print("pewnie zrobiłeś literowkę")
        ok = 0
ok = 0
while ok == 0:   
    ok = 1
    if rasa == "KRASNOLÓD" or rasa == "ELF" or rasa == "NIZIOŁEK":
        if rasa == "KRASNOLÓD":
            podrasa = str(input("To którego wybierasz?      "))
            podrasa = podrasa.upper()
            podrasa = podrasa.strip()
        elif rasa == "ELF":
            podrasa = str(input("To którego wybierasz?      "))
            podrasa = podrasa.upper()
            podrasa = podrasa.strip()
        elif rasa == "NIZIOŁEK":
            podrasa = str(input("To którego wybierasz?      "))
            podrasa = podrasa.upper()
            podrasa = podrasa.strip()
        else:
            print("Pewnie zrobileś literówkę")
            ok = 0
ok = 0
print("Jedną statystykne możesz ustawić na 8 jedną na 12 a resztę na 10")
while ok == 0 and siłe != 8 and siłe != 10 and siłe != 12:
    ok = 1
    siłe = int(input("Na ile ustawiasz siłę?"))
ok = 0
while ok == 0 and zręczność != 8 and zręczność != 10 and zręczność != 12:
    ok = 1
    zreczność = int(input("Na ile ustawiasz zręczność? "))
    while zręczność != 10 and zręczność == siłe:
        print("Nie możesz tyle mieć")
        zręczność = int(input("Na ile ustawiasz zręczność?"))
while ok == 0 and zdrowie != 8 and zdrowie != 10 and zdrowie != 12:
    ok = 1
    zdrowie = int(input("Na ile ustawiasz zdrowie? "))
    while zdrowie != 10 and zdrowie == siłe and zdrowie == zręczność:
        print("Nie możesz tyle mieć")
        zdrowie = int(input("Na ile ustawiasz zdrowie?"))
inteligencje = int(input("Na ile ustawiasz inteligencję?"))
if inteligencje != 8 and inteligencje != 10 and inteligencje != 12:
    print("Nie możesz tyle mieć")
    inteligencje = int(input("Na ile ustawiasz inteligencję?"))
    if inteligencje != 8 and inteligencje != 10 and inteligencje != 12:
        inteligencje = int(input("Na ile ustawiasz inteligencję?"))
        if inteligencje != 8 and inteligencje != 10 and inteligencje != 12:
            print("Nie możesz tyle mieć")
            inteligencje = int(input("Na ile ustawiasz inteligencję?"))
if inteligencje != 10 and inteligencje == siłe:
    print("Nie możesz tyle mieć")
    inteligencje = int(input("Na ile ustawiasz inteligencję?"))
    if inteligencje != 10 and inteligencje == siłe:
        print("Nie możesz tyle mieć")
if inteligencje != 10 and inteligencje == zręczność:
    print("Nie możesz tyle mieć")
percepcje = int(input("Na ile ustawiasz percepcję?"))
if percepcje != 8 and percepcje != 10 and percepcje != 12:
    print("Nie możesz tyle mieć")
    percepcje = int(input("Na ile ustawiasz percepcję?"))
    if percepcje != 8 and percepcje != 10 and percepcje != 12:
        percepcje = int(input("Na ile ustawiasz percepcję?"))
        if percepcje != 8 and percepcje != 10 and percepcje != 12:
            print("Nie możesz tyle mieć")
            percepcje = int(input("Na ile ustawiasz percepcję?"))
charyzme = int(input("Na ile ustawiasz charyzmę?"))
if charyzme != 8 and charyzme != 10 and charyzme != 12:
    print("Nie możesz tyle mieć")
    charyzme = int(input("Na ile ustawiasz charyzmę?"))
    if charyzme !=8 and charyzme != 10 and charyzme != 12:
        charyzme = int(input("Na ile ustawiasz charyzmę?"))
        if charyzme != 8 and charyzme != 10 and charyzme != 12:
            print("Nie możesz tyle mieć")
            charyzme = int(input("Na ile ustawiasz charyzmę?"))
if rasa == "KRASNOLÓD":
    if podrasa == "GÓRSKI":
        siłe = siłe + 2
        bonus_siłe = 2
        zdrowie = zdrowie + 2
        bonus_zdrowie = 2
    elif podrasa == "WZGORZOWY":
        siłe = siłe + 2
        bonus_siłe = 2
        zdrowie = zdrowie + 1
        bonus_zdrowie = 1
if rasa == "ELF":
    if podrasa == "WYSOKI":
        zręczność = zręczność + 2
        bonus_zręczności = 2
        inteligencje = inteligencje + 1
        bonus_inteligencji = 1
    elif podrasa == "LEŚNY":
        zręczność = zręczność + 2
        bonus_zręczności = 2
        percepcje = percepcje + 1
        bonus_percepcje = 1
if rasa == "NIZIOŁEK":
    if podrasa == "LEKKOSTOPPY":
        zręczność = zręczność + 2
        bonus_zręczności = 2
        charyzme = charyzme + 1
        bonus_charyzme = 1
    elif podrasa == "GRUBY":
        zręczność = zręczność + 2
        bonus_zręczności = 2
        zdrowie = zdrowie + 1
        bonus_zdrowie = 1
elif rasa == "CZLOWIEK":
    siłe = siłe + 1
    bonus_siłe = 1
    zręczność = zręczność + 1
    bonus_zręczności = 1
    zdrowie = zdrowie + 1
    bonus_zdrowie = 1
    inteligencje = inteligencje + 1
    bonus_inteligencji = 1
    percepcje = percepcje + 1
    bonus_percepcji = 1
    charyzme = charyzme + 1
    bonus_charyzme = 1
elif rasa == "DRAGONBORN":
    umiejętnośćRobr = 12
    siłe = siłe + 2
    bonus_siłe = 2
    charyzme = charyzme + 1
    bonus_charyzme = 1
    if umiejętnośćR == "OGIEŃ":
        odpornośćA = "ogień"
    elif umiejętnośćR == "BŁYSKAWICA":
        odpornośćA = "błyskawica"
    elif umiejętnośćR == "KWAS":
        odpornośćA = "kwas"
    elif umiejętnośćR == "TRUCIZNA":
        odpornośćA = "trucizna" 
    elif umiejętnośćR == "ZIMNO":
        odpornośćA = "zimno"
elif rasa == "GNOM":
    inteligencje = inteligencje + 2
    bonus_inteligencji = 2
    zdrowie = zdrowie + 1
    bonus_zdrowie = 1
elif rasa == "PÓŁELF":
    charyzme = charyzme + 2
    bonus_charyzmy = 2
    bonus = str(input("Co ulepszasz")).upper().strip()
    if bonus == "SIŁA":
        siłe = siłe + 1
        bonus_siłe = 1
    elif bonus == "ZRĘCZNOŚĆ":
        zręczność = zręczność + 1
        bonus_zręczność = 1
    elif bonus == "ZDROWIE":
        zdrowie = zdrowie + 1
        bonus_zdrowie = 1
    elif bonus == "INTELIGENCJA":
        inteligencje = inteligencje + 1
        bonus_inteligencja = 1
    elif bonus == "PERCEPCJA":
        percepcje = percepcje + 1
        bonus_percepcja = 1
    bonus = str(input("Co ulepszasz")).upper().strip()
    if bonus == "SIŁA":
        siłe = siłe + 1
        bonus_siłe = 1
    elif bonus == "ZRĘCZNOŚĆ":
        zręczność = zręczność + 1
        bonus_zręczność = 1
    elif bonus == "ZDROWIE":
        zdrowie = zdrowie + 1
        bonus_zdrowie = 1
    elif bonus == "INTELIGENCJA":
        inteligencje = inteligencje + 1
        bonus_inteligencja = 1
    elif bonus == "PERCEPCJA":
        percepcje = percepcje + 1
        bonus_percepcja = 1
elif rasa == "PÓŁORK":
    siłe = siłe + 2
    bonus_siłe = 2
    zdrowie = zdrowie + 1
    bonus_zdrowie = 1
elif rasa == "TIEFLING":
    inteligencje = inteligencje + 2
    bonus_inteligencji = 2
    charyzme = charyzme + 1
    bonus_charyzme = 1
if najlepsza_statystyka == "SIŁA":
    print("To polecam ci takie klasy jak:")
    print("Wojownika (Mistrz sztuk walki, biegły w posługiwaniu się różnymi rodzajami broni i zbroi)")
    print("Paladyna (Święty wojownik związany świętą przysięgą)")
elif najlepsza_statystyka == "ZRĘCZNOŚĆ":
    print("To polecam ci takie klasy jak:")
    print("Wojownika (Mistrz sztuk walki, biegły w posługiwaniu się różnymi rodzajami broni i zbroi)")
    print("Mnich (Mistrz sztuk walki, wykorzystujący siłę ciała w dążeniu do fizycznej i duchowej doskonałości)")
    print("Leśniczy Wojownik, który wykorzystuje umiejętności bojowe i magię natury, by stawić czoła zagrożeniom na obrzeżach cywilizacji")
    print("Łotrzyk Łotr, który posługuje się podstępem i sprytem, aby pokonywać przeszkody i wrogów")
elif najlepsza_statystyka == "ZDROWIE":
    print("To polecam ci takie klasy jak:")
    print("barbażyńca (Nieustraszony wojownik o prymitywnym pochodzeniu, który może wpaść w szał bitewny)")
elif najlepsza_statystyka == "INTELIGENCJA":
    print("To polecam ci takie klasy jak:")
    print("czarodziej Uczony użytkownik magii, potrafiący manipulować strukturami rzeczywistości")
elif najlepsza_statystyka == "PERCEPCJA":
    print("To polecam ci takie klasy jak:")
    print("Kapłan Kapłański mistrz, który posługuje się magią boską w służbie wyższej mocy")
    print("Druid Kapłan Starej Wiary, władający mocami natury – światłem księżyca i wzrostem roślin, ogniem i błyskawicami – i przyjmujący formy zwierzęc")
    print("Mnich (Mistrz sztuk walki, wykorzystujący siłę ciała w dążeniu do fizycznej i duchowej doskonałości)")
    print("Leśniczy Wojownik, który wykorzystuje umiejętności bojowe i magię natury, by stawić czoła zagrożeniom na obrzeżach cywilizacji")
elif najlepsza_statystyka == "CHARYZMA":                  
    print("To polecam ci takie klasy jak:")
    print("Bard Inspirujący magik, którego moc odzwierciedla muzykę stworzenia")
    print("Paladyna (Święty wojownik związany świętą przysięgą)")
    print("Czarownik (Czarodziej czerpiący z wrodzonej magii wynikającej z daru lub linii krwi)")
    print("Czarnoksiężnik (Osoba władająca magią, która powstała w wyniku umowy z istotą pozaplanarną)")
klasa = str(input("Jaką klasę wybierasz"))
klasa = klasa.upper()
klasa = klasa.strip()
if klasa == "BARBAŻYŃCA":
    AC = 10
    print("Masz +10 do AC gdy nie masz zbroi dużą siekiere K12 obrażeń i dwie jednoręczne po K6 obrażeń")
    ekipunek1 = "Siekiera duża"
    ekipunek1obr = 12
    ekwipunek2obr = 6
    print("Posiadasz furie, 2 razy na długi odpoczynek możesz jej użyć, by zadawać +2 obrażeń")
    umiejętnośćK = "RAGE"
elif klasa == "BARD":
    print("Masz długi miecz (K8 obrażeń), skórzaną zbroję (AC 11), łuk (K8 obrażeń, 20 bełtów)")
    print("Masz bardycką inspirację (+K6 do następnego rzutu dla wybranego gracza)")
    brońA = "Długi miecz"
    brońAobr = 8
    brońB = "Łuk"
    brońBobr = 8
    brońBnaboje = 20
    zbrojaA = "Skórzana zbroja"
    zbrojaAAC = 11
    umiejętnośćK = "INSPIRACJA"
elif klasa == "KAPŁAN":
    print("Masz siekierę jednoręczną (K6 obrażeń), kolczugę łuskową (AC 13), sztylet (K4 obrażeń)")
    print("Zawsze leczysz o 2 więcej")
    brońA = "Maczuga"
    brońAobr = 6
    brońB = "Sztylet"
    brońBobr = 4
    zbrojaA = "Kolczuga"
    zbrojaAAC = 13
elif klasa == "DRUID":
    print("Masz tarczę (+2 AC), siekierę jednoręczną (K6 obrażeń)")
    print("Znasz druiczyny")
    brońA = "Siekiera jednoręczna"
    brońAobr = 6
    zbrojaA = "Tarcza"
    zbrojaAAC = 2
elif klasa == "WOJOWNIK":
    print("Masz tarczę (AC +2) i dwa topory ręczne(po K6 obrażeń)")
    ekwipunek1 = str(input("Wybierasz A) Kolczuga (16 AC) czy B) Skórzana zbroja (11 AC) + łuk (K8 obrażeń, 20 strzał)"))
    ekwipunek1 = ekwipunek1.upper().strip()
    zbrojaB = "Tarcza"
    zbrojaBAC = 2
    brońBobr = 6
    if ekwipunek1 != "A" and ekwipunek1 != "B":
        ekwipunek1 = str(input("Wybierasz A czy B!")).upper().strip()
        if ekwipunek1 == "A":
            zbrojaA = "Kolczuga"
            zbrojaAAC = 16 
            if ekwipunek1 == "B":
                brońA = "Łuk"
                brońAnaboje = 20
                zbrojaA = "Skórzana zbroja"
                zbrojaAAC = 11
    print("Masz umiejętność drugi oddech, raz na długi odpoczynek leczysz k10 + poziom")
    umiejętność = "DRUGIODDECH"
elif klasa == "MNICH":
    print("Masz krótki miecz (K6 obrażeń) i 20 żutek(po K4 obrażeń)")
    print("Masz 10 AC bez zbroi")
    AC = 10
    brońA = "Miecz krótki"
    brońAobr = 6
    brońB = "Żutka"
    brońBnaboje = 20
    brońBobr = 4
elif klasa == "PALADYN":
    print("Masz tarczę (AC +2) i 5 oszczepów (każdy po K8 obrażeń)")    
    brońA = "Oszczep"
    brońAobr = 8
    ekwipunek2 = "Skórzana zbroja"
    zbrojaA = "tarcza"
    zbrojaAAC = 2 
    brońAnaboje = 5
elif klasa == "LEŚNICZY":
    print("Masz kolczugę łuskową (AC 13), długi miecz (K8 obrażeń) i łuk (20 strał K6 obrażeń) morzesz wybrać ulubionego wroga i środowisko")
    zbrojaA = "Kolczuga łuskowa"
    brońA = "Łuk"
    brońAobr = 6
    brońB = "Miecz długi"
    brońBobr = 8
    zbrojaAAC = 13
    brońAnaboje = 20
    umiejętnośćK = "WRÓG"
    wróg = str(input("jaki jest twój ulubiony wróg? wybierz z bestie, istoty niebiańskie, konstrukty, istoty magiczne, potwory, rośliny lub nieumarli"))
    wróg = wróg.upper().strip()
    if wróg != "BESTIA" and wróg != "ISTOTANIEBIAŃSKA" and wróg != "KONSTRUKT" and wróg != "ISTOTAMAGICZNA" and wróg != "POTWOR" and wróg != "ROŚLINA" and wróg != "NIEUMARŁY":
        print("Nie ma takiego lub zrobileś literówkę")
        wróg = str(input("jaki jest twój ulubiony wróg? wybierz z bestie, istoty niebiańskie, konstrukty, istoty magiczne, potwory, rośliny lub nieumarli"))
        wróg = wróg.upper().strip()
        if wróg != "BESTIA" and wróg != "ISTOTANIEBIAŃSKA" and wróg != "KONSTRUKT" and wróg != "ISTOTAMAGICZNA" and wróg != "POTWOR" and wróg != "ROŚLINA" and wróg != "NIEUMARŁY":
            print("Nie ma takiego lub zrobileś literówkę")
    umiejętnośćKB = "TEREN"
    teren = str(input("Jaki jest twoj ulubiony teren wybierz z arktyczny, nadmorski, pustynny, leśny, trawiasty, górski, bagienny lub Podmrok"))
elif klasa == "ŁOTRZYK":
    print("Masz skórzaną zbroję (AC 11)")
    print("Masz sztylet (K4 obrażeń) oraz lekką kuszę (K8 obrażeń, 20 bełtów)")
    print("Potrafisz zrobić: Atak z zaskoczenia (+K6 do obrażeń przy następnym ataku)")
    zbrojaA = "skórzana zbroja"
    zbrojaAAC = 11
    brońA = "Sztylet"
    brońAobr = 4
    brońB = "Lekka kusza"
    brońBobr = 8
    brońBnaboje = 20
elif klasa == "CZAROWNIK":
    print("Masz łuk (K8 obrażeń 20 naboji)")
    brońA = "łuk"
    brońAobr = 8
    brońAnaboje = 20
elif klasa == "CZARNOKSIĘZNIK":
    print("Masz łuk (K8 obrażeń 20 naboji)")
    brońA = "łuk"
    brońAobr = 8
    brońAnaboje = 20
elif klasa == "CZARODZIEJ":
    print("Masz miecz krótki (K6 obrażeń )")
    brońA = "miecz krotki"
    brońAobr = 6
