
Inlämningsuppgift 2: Iteration och slumptal.

1. Turtle Graphics
krav bör uppfyllas:
Rita upp minst två olika typer av figurer
Alla figurer ska bestå av mer än en enda cirkel eller rektangel. Exempel på lämpliga figurer kan vara träd, stjärnor, hus, människor, snögubbar…
Samma figur ska upprepas flera gånger.

Låt användaren ange hur många figurer av olika slag som ska ritas upp.
Använd loopar för att placera ut figurerna upprepade gånger.
utnyttja random för att variera placeringen och utseendet på dina figurer (storlek etc).
Beroende på typ av figurer utnyttja loopar som en del av algoritmen för att rita ut en enskild figur => nästlade loopar. Exempel: En loop där varje iteration ritar ut en solstråle runt en sol.
Figurernas placering och stjärnornas storlek kan variera här slumpmässigt.
#1 figurer i rymdscenen
* Stjärnor
    * Rita med en loop (t.ex. 5-uddiga stjärnor eller strålformade stjärnor).
    * Placeras slumpmässigt på himlen, olika storlekar.
* Planeter
    * Cirklar i olika färger.
    * Vissa kan ha en "ring" (saturnus-stil) ritad med en loop.
* Raket
    * Enkel figur byggd av rektanglar (kropp), triangel (nos), små cirklar (motorer).
    * Kan stå på en "startplatta" eller sväva fritt.
* Måne eller galax
    * En stor cirkel eller ett mönster av stjärnor i en spiral (mer avancerad loop → imponerande!).


* Random: Varje gång du kör koden får du en ny unik rymdscen.
* Flera figurer: Inte bara en typ, utan en hel liten värld.
* Nästlade loopar: Används för stjärnor och ev. galax.






2. The Nightmare Crawl
Gör ett spel där spelaren befinner sig på en mörk plats.
Någonstans i mörkret finns en ficklampa som spelaren behöver för att rädda sig och vinna spelet.
Spelaren söker efter ficklampan genom att treva sig runt i mörkret.
Spelplanen kan vara kvadratisk eller rektangulär.
Vi tänker oss att väggar eller murar begränsar spelplanens storlek.
När spelet börjar ska ficklampan och spelaren placeras ut på en slumpmässig plats på spelplanen. I exemplet nedan befinner sig spelaren (=P) på rad 3, kolumn 2 medan ficklampan (=F) befinner sig på rad 2, kolumn 5. Om spelaren nu går t.ex. tre steg österut och ett steg norrut hittar hen ficklampan.

Spelet behöver alltså hålla reda på spelarens och ficklampans positioner.
Det är då enklast att använda sig av totalt fyra variabler: två variabler (rad/kolumn) för spelaren och två variabler (rad/kolumn) för ficklampan.
Värden för dessa slumpas fram med någon lämplig funktion från modulen random då programmet startar.
Programmet bör gärna se till att spelaren och ficklampan inte placeras i samma startruta.
Låt spelaren ange riktning (t.ex. med w/a/s/d) och flytta spelaren i vald riktning.
rita upp spelplanen och spelarens position (men inte ficklampan!) med tecken- eller sköldpaddsgrafik.
Tips: du kan sätta in en “fuskutskrift” som avslöjar ficklampans position redan i början av spelet.

Om spelaren hittar ficklampan slutar spelet med vinst för spelaren.
Spelet borde också förhindra spelaren att gå utanför spelplanen.

Spelet bör också ha någon sorts game-over mekanism som gör att spelaren inte kan söka efter ficklampan i all oändlighet.
Hitta själv på en sådan utmaning/begränsning!

Obs: I spelet behöver du inte skriva/rita ut spelplanen - istället kan du skriva ut instruktioner och information i stil med
Vart vill du gå (w/a/s/d)? w
Du kravlar norrut.
Vart vill du gå (w/a/s/d)? w
Du slår huvudet i väggen. Aj.
Vart vill du gå (w/a/s/d)? d
Du kravlar österut.
Du hittade ficklampan!

#2
Start: Spelaren vaknar upp i totalt mörker.
1. Tidsbegränsning / antal drag
* Exempel: spelaren har max 20 drag på sig att hitta ficklampan, annars "tar mörkret över".
* Ger spänning och gör spelet mer utmanande.
2. Fällor eller hinder
* Några rutor kan slumpas som "fällor" (=X). Om spelaren går dit → förlorar spelet.
* Detta gör att spelaren inte bara kan vandra planlöst.
3. Ledtrådar
* spelaren får små ledtrådar om ficklampan är nära.



När du är klar:
Ladda upp dina .py-filer här på Canvas, eller en länk till din Notebook.
Lämna också in en självbedömning för varje deluppgift. Använd skalan 0-4 och ge också en kort motivering:
0: Inte påbörjad.
1: Har en början (skrivit litet kod) men det mesta av uppgiften återstår.
2: Ungefär halvvägs, är en bra bit på väg.
3: Nästan klar, det mesta fungerar enligt specifikationen men finns ännu kvar någon bugg.
4: Fungerar enligt specifikationen.
Lämna in självbedömningen som en "Canvas-kommentar" i samband med inlämningen.
Exempel på hur du kan resonera och skriva motiveringar:
Uppgift 1) 2 (Fick till några snögubbar men jag hann inte lägga till ytterligare en figur)
Uppgift 2) 3 (Fungerar nästan perfekt men ibland verkar man kunna gå utanför spelplanen, hittar inte buggen)
=> Totalt 5/8 = 63%

