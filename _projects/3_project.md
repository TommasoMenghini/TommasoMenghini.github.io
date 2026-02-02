---
layout: page
title: Clustering Bayesiano con Modelli di Mistura di Processi di Dirichlet
description: Salso e Greedy Search: algoritmi a confronto per l’ottimizzazione bayesiana del clustering dei dati attraverso processo decisionale
img: assets/img/7.jpg
importance: 3
category: work
related_publications:
  - wade2018
---

Questo progetto è stato sviluppato in collaborazione con il mio amico e compagno d'università Tommaso Pozzi.

Il **clustering** è una disciplina della statistica e del machine learning ampiamente utilizzata per individuare pattern nascosti in dati complessi, difficilmente osservabili a occhio nudo.
Gli algoritmi di clustering più classici, come **k-means** o i metodi gerarchici, vengono spesso applicati in contesti in cui non si dispone di informazioni preliminari sulla struttura dei dati. Tuttavia, questi approcci presentano alcune limitazioni rilevanti, come la sensibilità ai minimi locali e la necessità di specificare a priori il numero di cluster.

Un’alternativa più flessibile è rappresentata dai **modelli di mistura**, che assumono una distribuzione probabilistica per descrivere la struttura dei gruppi presenti nei dati. In questo progetto si sono studiati metodi di clustering bayesiani non parametrici, seguendo l’impostazione proposta da {% cite wade2018 %}, che consente di incorporare informazioni a priori e di modellare in modo esplicito l’incertezza.

I modelli di mistura non parametrici, come i **Dirichlet Process Mixture Models**, assumono un numero teoricamente infinito di componenti. Questa caratteristica li rende particolarmente flessibili, poiché il numero di cluster può crescere con la dimensione del campione, senza essere fissato in anticipo. L’approccio bayesiano permette inoltre di costruire una distribuzione a posteriori sullo spazio delle partizioni, offrendo una rappresentazione completa dell’**incertezza** associata al clustering.

Un tema centrale del progetto è la sintesi della distribuzione a posteriori delle partizioni. Poiché l’output del modello non è una singola soluzione di clustering, ma un insieme di partizioni plausibili, è necessario adottare un criterio decisionale per individuare una partizione rappresentativa.

A questo scopo si sono analizzati diversi approcci basati sulla **posterior similarity matrix**, implementando e confrontando differenti funzioni di perdita in particolare la **Binder loss** - e la sua versione generalizzata- e la **Variation of Information (VI) loss**. Queste funzioni permettono di confrontare partizioni diverse e di selezionare quella che minimizza la perdita attesa a posteriori.

Nel progetto si sono confrontati due algoritmi di ottimizzazione della partizione. Il **Greedy**, un algoritmo deterministico basato su miglioramenti locali e il **SALSO**, un approccio più recente progettato per essere più efficiente su dataset di grandi dimensioni.

Attraverso uno studio di simulazione si è analizzato il comportamento dei due algoritmi al variare della dimensione campionaria e di alcuni parametri del modello. I risultati mostrano che, pur producendo soluzioni simili in termini di qualità del clustering, **SALSO** risulta più efficiente per campioni numerosi, mentre **Greedy** si dimostra più adatto a dataset più piccoli o strutture più semplici.

Viene proposto anche un'applicazione ad un dataset reale, **Country Help**, contenente indicatori socio-economici di diversi paesi.
L’obiettivo è individuare gruppi di nazioni con caratteristiche simili senza imporre a priori il numero di cluster.

Il modello bayesiano consente di identificare cluster interpretabili di paesi, evidenziare osservazioni ambigue o di confine, quantificare l’incertezza associata alla soluzione di clustering.

<figure>
  <img src="/assets/img/gg_world.png"
       alt="Clustering bayesiano Country Help">
  <figcaption>
    Clustering bayesiano dei paesi nel dataset <em>Country Help</em>.
  </figcaption>
</figure>

Il grafico mostra il risultato del clustering ottenuto. Vengono individuati **sei** gruppi distinti di paesi.

Il cluster **verde** raccoglie le nazioni più sviluppate dal punto di vista socio-economico e sanitario, appartenenti al cosiddetto “Occidente” in senso politico ed economico, indipendentemente dalla posizione geografica. Ne fanno parte, ad esempio, Giappone, Corea del Sud e Australia.

Il cluster **rosso** include paesi che nel 2010 potevano essere associati al cosiddetto Secondo Mondo, caratterizzati da economie fortemente industrializzate ma con standard di vita non sempre elevati. Esempi significativi sono la Federazione Russa e il Brasile, economie fortemente dipendenti dall’esportazione di materie prime.

Il cluster **giallo** è concentrato prevalentemente nell’Africa subsahariana e nel subcontinente indiano e identifica paesi meno sviluppati dal punto di vista economico, politico e sociale.

Il cluster **arancione** comprende un numero ristretto di stati della Penisola Arabica (tra cui Arabia Saudita, Qatar ed Emirati Arabi Uniti), accomunati da un’elevata ricchezza derivante dall’esportazione di petrolio, ma caratterizzata da una forte disuguaglianza nella distribuzione delle risorse.

Gli ultimi due cluster **(viola e blu)** raccolgono paesi con caratteristiche più eterogenee o specifiche, come piccoli stati altamente finanziarizzati e fiscalmente attrattivi.

Nel complesso, il risultato mostra come il clustering bayesiano riesca a catturare pattern socio-economici globali coerenti e interpretabili, senza imporre a priori il numero di gruppi.

Il codice completo e l’analisi dettagliata dell’esempio applicativo sono disponibili nella
repository GitHub a questo [link](https://github.com/TommasoMenghini/DPM-Models-for-Bayesian-Clustering/tree/main).
