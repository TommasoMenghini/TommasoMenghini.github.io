---
layout: page
title: Mercato Immobiliare a Milano
description: Generalized Additive Models per la Previsione dei Prezzi delle Case a Milano
img: assets/img/IMG_6576.JPG
importance: 2
category: work
related_publications:
  - gelman_hill_2006
  - wood2003
---

<div class="row mt-3">
  <div class="col-md-6">
    <div class="card h-100">
      <div class="card-body">
        <h5 class="card-title">📄 Report </h5>
        <p class="card-text"> Report completo in pdf.</p>
        <a href="/assets/pdf/report_menghini.pdf" class="btn btn-primary" target="_blank">
          Download PDF
        </a>
      </div>
    </div>
  </div>

  <div class="col-md-6">
    <div class="card h-100">
      <div class="card-body">
        <h5 class="card-title">🖥️ Slide </h5>
        <p class="card-text">Slide presentazione in pdf.</p>
        <a href="/assets/pdf/Slide_Tesi_Magistrale_Versione_Completa.pdf" class="btn btn-outline-primary" target="_blank">
          Download PDF
        </a>
      </div>
    </div>
  </div>
</div>


<div class="row mb-5">
  <!-- cards -->
</div>


In questo progetto analizzo e modello i prezzi delle abitazioni nella città di Milano utilizzando i **Generalized Additive Models (GAM)**.
L’obiettivo è costruire un modello predittivo interpretabile, in grado di catturare la relazione tra i prezzi delle case e le principali caratteristiche strutturali e contestuali degli immobili.

Il dataset è composto da **8.000** annunci immobiliari relativi alla città di Milano, descritti da 16 covariate che rappresentano caratteristiche strutturali, localizzazione, informazioni sull’edificio e dotazioni dell’abitazione, oltre alla variabile risposta: il prezzo di mercato.

Una delle principali difficoltà del progetto è la presenza di numerosi **valori mancanti** (oltre 5.600), che rende inadeguati approcci semplici come l’eliminazione delle osservazioni incomplete.
Anziché scartare una parte consistente dei dati, ho adottato una strategia di **imputazione iterativa** basata su modelli di regressione, imputando i valori mancanti tramite una sequenza di modelli univariati, selezionati in base alla natura delle variabili da imputare.

Questo approccio consente di mantenere il processo di imputazione statisticamente coerente e interpretabile, preservando al tempo stesso la maggior parte dell’informazione disponibile.

Per garantire previsioni di prezzo positive, la variabile risposta è stata modellata in **scala logaritmica**.
Un primo modello di regressione lineare ha messo in evidenza la presenza di andamenti **non lineari** tra il prezzo delle abitazioni e alcuni predittori chiave, come i metri quadri e le spese condominiali.

Per questo motivo ho utilizzato un **Generalized Additive Model**, che combina componenti smooth non parametriche per le variabili con effetti non lineari e termini lineari per le restanti covariate.

In particolare, i metri quadri, le spese condominiali e il numero totale di piani sono stati modellati tramite *thin plate regression splines*, con selezione dei parametri di smoothing effettuata tramite REML.

Questa scelta consente un buon compromesso tra capacità predittiva e interpretabilità, permettendo di analizzare direttamente l’effetto parziale di ciascun predittore.

Il **GAM** riesce a catturare efficacemente l’effetto marginale decrescente dei metri quadri sul prezzo delle abitazioni, mentre per alcune caratteristiche legate all’edificio emergono effetti più deboli o incerti.
Il modello ottiene un **Mean Absolute Error** di circa 79.000 € sul validation set.

Uno dei principali punti di forza di questo approccio è l’interpretabilità: i grafici degli effetti parziali permettono di studiare come ciascuna covariata influenzi il prezzo mantenendo costanti tutte le altre.

Il codice completo e i dettagli tecnici sono disponibili nella repository GitHub al seguente [link](https://github.com/TommasoMenghini/Milan-Housing).