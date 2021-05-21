# Projet Python

Un écran permettant de visualiser un pétri virtuel. Le pétir est constitué de :
* 200 par 200 case
* les cases de gauches communiquent avec celles de droite
* les cases du haut communiquent avec celles du bas
* c'est le pétri qui gère le temps (les tops d'horloge)

Au sein du pétri, des microbes évoluent. Description des microbes :
* Tous les microbes possèdent les comportements suivants :
  * naitre()
  * mourrir()
  * manger()
  * se reproduire()
  * se déplacer()

* Tous les microbes possèdent les attributs suivants :
  * une couleur (influencée par la quantité d'énergie actuelle, plus vive lorsque l'énergie est élevée)
  * une taille (exprimée en case)
  * une forme
  * une quantité d'énergie actuelle et max (en fonction de la taille)

* Tous les microbes consomment de la même quantité d'énergie en fonction de leurs actions, de leur taille et du temps
* Tous les microbes ont le même objectif : se reprdduire le plus possible
* Certains microbes peuvent être agressifs, d'autres necrophages, d'autres cannibales, ...
* Les microbes se reproduisent seuls, par division (mitose)

L'ensemble des données d'une simulation doit être stockée et enregistré dans une BDD (au choix)

Il doit y avoir une part de hasard dans les "décisions" prises par les microbes.
