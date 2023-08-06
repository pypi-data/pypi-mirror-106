# pytntprog

pytntprog displays the program of tnt tv in France

## install

``pip3 install pytntprog``
or
``pip install pytntprog``

## use

``pytntprog`` display the tnt programm for the current day with id index

example :

```
~ pytntprog
[00349] 00:00 W9 Enquête d'action Vol à l'étalage : comment les commerçants ripostent
[00692] 00:00 Gulli Zig & Sharko Coup de foudre
[00925] 00:00 Franceinfo France 24 
[00651] 00:03 CSTAR Storage Wars : enchères surprises Les robes flamenco
[00213] 00:05 France 3 Météo 
[...]
[00516] 23:52 CNEWS La sélection 
[00134] 23:55 France 5 Cinéma de minuit Cycle cinéma italien
[00404] 23:55 TMC 90' Enquêtes Un été sous haute tension pour les gendarmes du Sud
[00587] 23:55 NRJ 12 Young Sheldon Albert Einstein et l'histoire d'une autre Marie
[00795] 23:55 Gulli Kirikou et la sorcière 
[00812] 23:55 Chérie 25 The Closer : L.A. enquêtes prioritaires Comme chien et chat
[00517] 23:57 CNEWS Météo du soir 
[00518] 23:59 CNEWS Boucle de nuit 
```

``pytntprog -i [id]`` display the details of the programm with id

example:
```
~ pytntprog -i 795        
titre       : Kirikou et la sorcière 
chaine      : Gulli
jour        : 20210515
heure debut : 23:55
heure fin   : 01:21
resume      : Très impatient de découvrir le monde, Kirikou vient au monde par ses propres moyens et coupe lui-même le cordon ombilical qui le relie à sa mère. Celle-ci lui apprend que son père a disparu, comme d'ailleurs tous les autres hommes du village. La sorcière Karaba n'est pas étrangère à ces disparitions, elle qui a fait main basse sur toutes les richesses du pays, affamant ainsi la région. La rumeur prétend même qu'elle aurait mangé tous les hommes du village après les avoir fait prisonniers. Le petit Kirikou décide alors de rencontrer la sorcière pour comprendre les raisons de sa méchanceté et délivrer les siens...
episode     : 
date        : 1998
categorie   : film d'animation
age         : Tout public
```

``pytntprog -c`` display current programm
```
~ pytntprog -c      
[00687] 14:00 BFMTV Non Stop 
[00068] 14:40 Canal+ Rugby : Top 14 (Bordeaux Bègles / Castres) 
[00341] 14:40 M6 Chasseurs d'appart' 
[00610] 15:15 C8 Le poids des souvenirs 
[00919] 15:20 TF1 Séries Films Associées contre notre ex 
[00323] 16:00 LCI LCI tout info 
[...]
[00826] 17:25 RMC Découverte Mécanos express Projet pirate
[00860] 17:25 RMC Story New York police judiciaire L'éternel refrain
[00674] 17:26 CSTAR Au coeur de l'enquête Gumball Race : 100 jours dans la course des milliardaires sans limites (n°3)
[00307] 17:30 Arte Les hommes du désert : Dans les pas des chameliers du Sahara 
[00642] 17:30 TFX Familles nombreuses : la vie en XXL 
[00545] 17:31 La Chaîne parlementaire Allons plus loin 
[00944] 17:32 Franceinfo Cultissime 

```


``pytntprog -a`` display all tnt programm (current day by default)
example :
```
~ pytntprog -a
[...]
[08715] 20210525 23:45 RMC Découverte Mécanos express Une nouvelle aventure
[08827] 20210525 23:45 Franceinfo La chronique culture 
[08177] 20210525 23:50 France 5 C dans l'air 
[08206] 20210525 23:50 France 4 Culturebox les nuits 
[08695] 20210525 23:50 Chérie 25 Snapped : les femmes tueuses Deborah Huiett
[08828] 20210525 23:52 Franceinfo Le 23h 
[08457] 20210525 23:59 CNEWS Boucle de nuit 
```

``pytntprog -f "TF1"`` display the tnt programm for the current day with filter TF1
example :
```
~ pytntprog -f "TF1"
[00366] 01:30 TF1 Tirage de l'Euro Millions 
[00367] 01:35 TF1 Programmes de la nuit 
[...]
[00381] 19:55 TF1 Météo 
[00382] 20:00 TF1 Journal 
[00383] 20:40 TF1 Habitons demain 
[00384] 20:45 TF1 Tirage du Loto 
[00385] 20:50 TF1 Quotidien express 
[00922] 20:55 TF1 Séries Films Petits plats en équilibre 
[00386] 21:00 TF1 Météo 
[00923] 21:00 TF1 Séries Films Joséphine, ange gardien Profession menteur
[00387] 21:05 TF1 The Voice, la plus belle voix Finale
[00924] 22:45 TF1 Séries Films Joséphine, ange gardien La comédie du bonheur
[00388] 23:40 TF1 The Voice Finale
```

``pytntprog -f "Stade 2" "France 3"`` display the tnt programm for the current day with filter Stade 2 + France 3

``-n`` or ``--no-chache`` download the distant xml file event if the cache is not finished (24h by default)

## update 

``pytntprog -u`` to update pytntprog

## changelog

### 0.4.0

- Increase performance and time response
