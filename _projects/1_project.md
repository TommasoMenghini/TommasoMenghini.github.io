---
layout: page
title: Sondaggi elettorali in Italia (2018–2024)
description: Distorsioni sistematiche e affidabilità dei sondaggi pre-elettorali
img: assets/img/Screenshot 2026-01-24 165449.png
importance: 1
category: work
related_publications:
  - gelman2021failure
  - shirani2018disentangling
---

<div class="row mt-3">
  <div class="col-md-6">
    <div class="card h-100">
      <div class="card-body">
        <h5 class="card-title">📄 Tesi </h5>
        <p class="card-text"> Tesi magistrale completa in pdf.</p>
        <a href="/assets/pdf/Tesi_corretta.pdf" class="btn btn-primary" target="_blank">
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
        <a href="/assets/pdf/Slide_Tesi_Versione_Completa.pdf" class="btn btn-outline-primary" target="_blank">
          Download PDF
        </a>
      </div>
    </div>
  </div>
</div>


<div class="row mb-5">
  <!-- cards -->
</div>


I sondaggi elettorali rappresentano lo strumento più efficienti per misurare le opinioni di un’intera popolazione, ma costituiscono al contempo un elemento delicato e spesso controverso del processo democratico. È noto in letteratura che i sondaggi pre-elettorali siano affetti da un insieme di errori di campionamento e non, comunemente indicati come total survey error. 

I riferimenti principali di questo lavoro sono stati {% cite gelman2021failure %} e {% cite shirani2018disentangling %}.

In questo studio sono stati analizzati 1676 sondaggi elettorali condotti in Italia tra il 2018 e il 2024. Per ogni sondaggio erano disponibili le principali informazioni strutturali e le stime delle intenzioni di voto per un insieme di partiti politici. L’analisi è stata limitata alle principali forze politiche presenti stabilmente nel periodo considerato e agli istituti demoscopici che disponevano di un numero sufficiente di rilevazioni pre-elettorali per tutte le elezioni analizzate. 

Gli obiettivi dello studio erano comprendere se esistessero distorsioni sistematiche nelle stime delle intenzioni di voto basate su sondaggi pre-elettorali e verificare la presenza di differenze strutturali nell’affidabilità delle principali agenzie demoscopiche operanti in Italia. A tal fine, la discrepanza tra le previsioni derivate dai sondaggi e i risultati ufficiali delle urne ha assunto un ruolo centrale nella definizione della variabile risposta, che doveva consentire un confronto coerente tra partiti caratterizzati da livelli di consenso molto differenti.

È stato quindi introdotto l’errore relativo come indice dell’affidabilità di un’agenzia demoscopica. Tale misura è stata calcolata secondo due approcci alternativi: nel primo caso utilizzando l’ultimo sondaggio disponibile per ciascun istituto; nel secondo caso ricorrendo a una stima interpolata dell’intera serie dei sondaggi fino al giorno dell’elezione, ottenuta mediante l’applicazione del filtro di Kalman a un modello state space binomiale con local linear trend per le intenzioni di voto di ciascun partito e istituto demoscopico. Questo approccio ha consentito di incorporare in modo coerente l’informazione contenuta nell’intera traiettoria dei sondaggi. 

Il dataset utilizzato per l'analisi è composto da tre variabili categoriche indipendenti Istituto, Partito ed Elezione e dalla variabile risposta definita come descritto in precedenza, per un totale di 165 osservazioni corrispondenti alle combinazioni agenzia–partito–elezione. 

La prima analisi ha mostrato che la variabile Istituto non risulta statisticamente significativa nello spiegare l’errore relativo, indicando l’assenza di differenze sistematiche tra le agenzie demoscopiche in termini di affidabilità. Al contrario, sono emerse evidenze chiare di distorsioni sistematiche associate alle combinazioni di Partito ed Elezione, suggerendo che gli errori nelle stime delle intenzioni di voto dipendano dal contesto politico-elettorale e risultino comuni a tutte le agenzie. 

La seconda analisi, basata sul valore assoluto dell’errore relativo, conferma questo risultato: una volta controllato per il contesto attraverso Partito, Elezione e la loro interazione, le agenzie demoscopiche analizzate appaiono sostanzialmente intercambiabili in termini di affidabilità. Alla luce di tali evidenze, si conclude con una discussione critica del Poll of Polls, il quale non rappresenta una soluzione ai limiti strutturali dei sondaggi pre-elettorali. 




