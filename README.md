# PugliaSostenibileGUI

<img align="right" width="40%" src="https://github.com/claudialorusso/PugliaSostenibileGUI/blob/master/utils/images/COLORPugliaSostenibile746x687.png" alt="Puglia Sostenibile">

Graphical User Interface for **Puglia Sostenibile**.

### What is Puglia Sostenibile

**Puglia Sostenibile** is a portable software that enables the user to monitor semantic consistency with the *Sustainable Development Goals* (also known as *SDGs*) within institutional documents such as, for instance, laws, strategies, planning acts, etc. , written in italian.

### Agenda 2030: A brief introduction

The sensitivity towards the relationships between man and environments, and of individuals among them, as well as the perception of responsibility towards future generations have progressively increased in decision-makers over the last few decades, leading to orient the action of instituzions and individuals in a decisive way towards Sustainable Development.

In September 2015, all 193 <a href="https://www.un.org/en/">United Nations</a> Countries, including Italy, conceived an action plan to contribute to global development, promote human well-being and protect the environment.

The need to guarantee a better present and future for our Planet and the people who inhabit it has resulted in the definition and sharing of **Sustainable Development Goals** - whose acronym is *SDGs* - to be achieved by 2030: this gives rise to the *Agenda 2030* which aims to act collectively in a sustainable way towards 17 goals divided into 169  targets in relation to the various domains of social and economic development.

For further informations consult the <a href="https://sdgs.un.org/goals">United Nations</a> web page.

### Puglia Sostenibile: the outcome

*Computer Science* plays a key role in handle social and environmental challenges with regard to a sustainable future.

Similarly to the *European Commission*'s platform, <a href="https://knowsdgs.jrc.ec.europa.eu/">KnowSDGs</a>, which currently refers to European Regulations, written in English, **Puglia Sostenibile** is capable of verifying how much a document is lexically consistent with what is stated in the *Agenda 2030*.

The software has been "trained", in particular, through the analysis of the more than 2000 *Regional Laws*, enacted in Puglia in the last 50 years.

The activity is part of the institutional collaboration between <a href="https://www.consiglio.puglia.it/">Apulian Regional Council</a>, represented by the President <a href="https://trasparenza.regione.puglia.it/personale/loredana-capone">Loredana Capone</a>, and the <a href = "https://garantedetenuti.consiglio.puglia.it/struttura-di-supporto-al-garante">Study and Support Section for Legislation and Guarantee Policies</a>, at <a href="https://www.uniba.it/">UNIBA</a> (<i>University of Bari, Aldo Moro</i>) and, in particular, it was carried out as a part of an internal internship at the headquarters of the <a href="https://islab.di.uniba.it/">Intelligent Systems Laboratory</a> of the local <a href= "https://www.uniba.it/ricerca/dipartimenti/informatica">DIB</a> (<i>Computer Science Department</i>), chaired by <a href="https://www.uniba.it/portal_memberdata/giuseppe.pirlo">Prof. Giuseppe Pirlo</a> all under the supervision of <a href="https://www.google.com/url?sa=t&source=web&rct=j&url=https://it.linkedin.com/in/michele-chieco-135a0a93&ved=2ahUKEwjEloGmuvD1AhW2hP0HHfE8BK8Qjjh6BAgfEAE&usg=AOvVaw0Tj3ZxfzVm0-2V8-JcMRne">Dr. Michele Chieco</a> and <a href="https://www.uniba.it/docenti/calvano-gabriella">Dr. Gabriella Calvano</a>.

The use of the software, although tested on the Apulian Regional Laws, can be extended to other similar documents of different territorial levels or to other texts in general: by loading the document, the software will return the *SDGs* based on the analysis of the text.

As in the case of the *KnowSDGs* European platform, the analysis carried out by the software is based on the recurrence of words and their associations and not on a content evaluation which can, instead, be the subject of specific comparative studies between the text in question and the *Agenda 2030*.

<p align="center">
  <img src= "https://github.com/claudialorusso/PugliaSostenibileGUI/blob/master/utils/images/collab/trio_collab500x162.png" alt="Trio Collab: UNIBA ISL Apulian Region">
</p>

### Logo

<img align="right" width="30%" src="https://github.com/claudialorusso/PugliaSostenibileGUI/blob/master/utils/images/COLORPugliaSostenibile746x687.png" alt="Logo">

In the foreground of the <i>logo</i> you can notice the shape of a tree that brings to mind the idea of Nature and the complexity of mechanisms and interrelations that connect living beings with each other and with the environment.

In fact, sustainability should not be considered only in reference to acting positively for the sake of the environment but also in relationships, in equity, in mutual care.

Branches emerge from the trunk of the tree, the ends of which are shaped into arrows; each arrow points towards different directions that represent various declinations of sustainability and which, although divergent, all arise from the same principle: the common good can only be reached though common action.

Th Earth, behind the tree, is the presence that must always remind us of our condition of being inhabitants of the same place with limited resources that encourage us to take common action for their protection, if we want its good, and, at the same time, it stimulates to obatin that much-needed change.

And it's exactly for this reason that, behind the tree, we glimpse the Earth which has an ambivalent meaning: it spurs us to act for her good and, at the same time, stimulates a common action to obtain that much-needed change.

The <i>logo</i> was designed by the graphic expert <a href="https://www.linkedin.com/in/nicolasurgo/">Nicola Surgo</a>.


### Usage

**Puglia Sostenibile** is easy as a pie!

And to provide a better experience, it comes with an intelligible yet pleasant graphical user interface.

You can either choose to download the executable <a href="https://github.com/claudialorusso/PugliaSostenibileGUI/raw/master/PugliaSostenibile.exe">PugliaSostenibile.exe</a> or charge it via command line.

If you choose to download the *.exe*, the software is ready to be used while if you choose the command line option please read the section below for a correct execution.

### Command Line Experience

First thing, since the progam is Python 3 based, you need to install it on your machine.

**Beware**: current packages versions are **NOT** compatible with Python 3.10. Please install **Python 3.9** or below.

Open the command prompt and jump to the PugliaSostenibileGUI folder.

Assuming the folder is in "C:\\PugliaSostenibileGUI" you just need to type in the command line the following instructions:

```
cd "C:\\PugliaSostenibileGUI"
py PugliaSostenibile_GUI.py
```

If it is the first launch of the program **or** the program detects missing packages, an installation window will pop-up asking you the authorization to download and install these lasts.
Please make sure that your device has network connectivity.


<p align="center">
  <img width=60% src= "https://user-images.githubusercontent.com/38263840/152874773-366f5dbf-4693-47d2-a25d-cca78c7c4a56.png" alt="Installazione">
</p>

Check the box and click on the "Avanti" button: **Puglia Sostenibile** will, finally, open.

![Welcome](https://user-images.githubusercontent.com/38263840/152880138-151f384b-6b88-4817-837e-eb1c4b32c540.png)

### Puglia Sostenibile Structure

**Puglia Sostenibile** can be divided into six main sections:

<ul>
<li><b>Home Page:</b> it's the main page. You can simply upload the document (allowed extensions: '.pdf', '.docx', 'txt' only) by clicking on the "Seleziona Documento" button. Then, press "Start" and the software will compute the three first most relevant <i>SDGs</i>.
<p align="center">
	<img src= "https://user-images.githubusercontent.com/38263840/152885066-fe5e0ae7-6bf3-46f3-8735-c6a0af434d7c.png" alt="Home Page">
</p>
You can, also, find the occurrences of  a keyphrase: you just need to insert it in the box, click on the "Cerca" button and the software will tell you how many times it occurs into the document;</li>
<li><b>Info Page:</b> In this section you can find informations about the <i>Agenda 2030</i> and <b>Puglia Sostenibile</b>;</li>
<li><b>Advanced Page:</b> In this page you can change some advanced properties:

<p align="center">
	<img src= "https://user-images.githubusercontent.com/38263840/152883238-dfe169a7-ea91-4e78-9186-bf76958657bc.png" alt="Advanced">
</p>
<ul>
<li><b>Grammage:</b> To understand this feature, you need to know that <b>Puglia Sostenibile</b> computes the most relevant <i>SDGs</i> by means of the Cossim Similarity. This last is based on a TFIDF matrix between all of the <i>SDGs</i> and the law. To perform the computation, each content needs to be divided into keyphrases. Is given the user the opportunity to choose the <i>grammage</i> of the keyphrase which is the maximum number of words by which each keyphrase is composed of. By <i>default</i> the <b>Grammage</b> is setted to <b>unigram</b> (each keyphrase is composed by one token, only) but you can also choose <b>bigram</b>, in which case each keyphrase will be composed by one or two tokens.</li>
<li><b>SGDs vs Targets:</b> by <i>default</i> the software reveals the three most relevant <i>SDGs</i>  but it is also given to you the chance to find out the most relevant Targets by checking the pertinent button.
</li>
</ul>
</li>
<li><b>Agenda 2030 Page:</b> in this page you can consult the <i>Agenda 2030</i>;</li>
<li><b>Contacts Page:</b> if you encounter any troubles with something or want to submit some feedback, in this section you can find the contacts you need: any suggestions for improvement are welcome!</li>
<li><b>Browes SDGs Page:</b> at any moment, if you need to consult the <i>SDGs</i> you can simply click on the "Sfoglia gli SDGs" button and a window will instantly pop-up allowing you to discover the related *goal* and *targets*.
  <p align="center">
    <img src= "https://user-images.githubusercontent.com/38263840/152884773-ec6d666c-a3ee-4d8d-86ad-cdd29cb4a507.png" alt="Sfoglia">
  </p>
  </li>
</ul>


### UWP

<b>Puglia Sostenibile</b> is an <b>UWP</b> (<i>Universal Windows Platform</i>) this means that it is compatible with several windows version, according to the <a href="https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/">windows SDK</a> requirements.

### Libraries

The following libraries were used to create <b>Puglia Sostenibile</b>:
<ul>
<li><a href ="https://github.com/explosion/spacy-models/releases/download/it_core_news_sm-3.2.0/it_core_news_sm-3.2.0-py3-none-any.whl">it-core-news-sm</a> module</li>
<li><a href ="https://www.nltk.org/">nltk</a> </li>
<li><a href ="https://numpy.org/">numpy</a></li>
<li><a href ="https://pandas.pydata.org/">pandas</a></li>
<li><a href ="https://github.com/pymupdf/PyMuPDF">PyMuPDF</a> (GUI purposes)</li>
<li><a href ="https://github.com/mstamy2/PyPDF2">PyPDF2</a> </li>
<li><a href ="https://python-docx.readthedocs.io/en/latest/user/documents.html">python-docx</a> </li>
<li><a href ="https://scikit-learn.org/stable/">scikit-learn</a> </li>
<li><a href ="https://scipy.org/">scipy</a> </li>
<li><a href ="https://spacy.io/">spacy</a> </li>
<li><a href ="https://docs.python.org/3/library/tkinter.html">tkinter</a> (GUI purposes) </li>
<li><a href ="https://github.com/Roshanpaswan/tkPDFViewer">tkPDFViewer</a>  (GUI purposes)</li>
</ul>

<details>
  <summary>Italiano</summary>

# PugliaSostenibileGUI

<img align="right" width="40%" src="https://github.com/claudialorusso/PugliaSostenibileGUI/blob/master/utils/images/COLORPugliaSostenibile746x687.png" alt="Puglia Sostenibile">

Interfaccia grafica per <b>Puglia Sostenibile</b>.

### Che cos'è Puglia Sostenibile

**Puglia Sostenibile** è un'applicazione' portabile che permette all'utente di monitorare la coerenza semantica con gli <b>Obiettivi di Sviluppo Sostenibile</b> (acronimo <i>OSS</i> o <i>SDGs</i>) all'interno di documenti istituzionali quali, ad esempio, leggi, strategie, atti di programmazione, ecc., scritti in lingua italiana.


### Agenda 2030: Una breve introduzione

La sensibilità verso le relazioni tra uomo e ambiente, e degli individui tra loro, e la percezione della responsabilità verso le future generazioni sono progressivamente aumentate nei decisori nel corso degli ultimi decenni portando ad orientare l'azione delle istituzioni e dei singoli in modo deciso verso lo Sviluppo Sostenibile.

Nel settembre 2015, tutti i 193 Paesi delle <a href="https://unric.org/it/">Nazioni Unite</a> , tra cui l’Italia, hanno concepito un piano d’azione per contribuire allo sviluppo globale, promuovere il benessere umano e proteggere l’ambiente.

Il bisogno di garantire un presente ed un futuro migliore al nostro Pianeta e alle persone che lo abitano è sfociato nella definizione e condivisione di **Obiettivi di Sviluppo Sostenibile** (*Sustainable Development Goals* – il cui acronimo inglese è *SDGs*) da raggiungere entro il 2030: è nata, così l’Agenda 2030 che si propone di agire collettivamente in modo sostenibile verso 17 obiettivi, o <i>goal</i>, declinati in 169 traguardi, anche detti target, in relazione ai vari domini dello sviluppo sociale ed economico.

Per maggiori informazioni consultare la pagina delle <a href="https://unric.org/it/agenda-2030/">Nazioni Unite</a>.

### Puglia Sostenibile: la nascita

La *Computer Science* gioca un ruolo fondamentale nell’essere d’ausilio a sfide sociali ed ambientali con riguardo ad un futuro sostenibile.

Similarmente a quanto sviluppato dalla *Commissione Europea*, con la sua piattaforma <a href="https://knowsdgs.jrc.ec.europa.eu/">KnowSDGs</a> , che fa attualmente riferimento a normative Europee, scritte in lingua inglese, **Puglia Sostenibile** è un software in grado di verificare quanto un documento sia coerente lessicalmente con quanto enunciato nell'<i>Agenda 2030</i>. Il software è stato "addestrato", in particolare, attraverso l'analisi delle oltre 2000 leggi regionali, emanate in Puglia negli ultimi 50 anni.

L'attività si inquadra nella collaborazione istituzionale tra <a href="https://www.consiglio.puglia.it/">Consiglio Regionale della Puglia</a>, rappresentato dalla Presidente <a href="https://trasparenza.regione.puglia.it/personale/loredana-capone">Loredana Capone</a>, e dalla <a href = "https://garantedetenuti.consiglio.puglia.it/struttura-di-supporto-al-garante">Sezione Studio e Supporto alla Legislazione e alle Politiche di Garanzia</a>, all’<a href="https://www.uniba.it/">UNIBA</a> (<i>Università degli Studi di Bari, Aldo Moro</i>) e, in particolare, è stata svolta nell'ambito di un tirocinio interno approntato presso la sede del <a href="https://islab.di.uniba.it/">Laboratorio di Sistemi Intelligenti</a> della locale <a href= "https://www.uniba.it/ricerca/dipartimenti/informatica">Facoltà di Informatica</a> (<i>DIB</i>), presieduto dal <a href="https://www.uniba.it/portal_memberdata/giuseppe.pirlo">Prof. Giuseppe Pirlo</a> il tutto sotto la supervisione del <a href="https://www.google.com/url?sa=t&source=web&rct=j&url=https://it.linkedin.com/in/michele-chieco-135a0a93&ved=2ahUKEwjEloGmuvD1AhW2hP0HHfE8BK8Qjjh6BAgfEAE&usg=AOvVaw0Tj3ZxfzVm0-2V8-JcMRne">Dr. Michele Chieco</a> e della <a href="https://www.uniba.it/docenti/calvano-gabriella">D.ssa Gabriella Calvano</a>.

L'uso del software, per quanto testato sulle leggi regionali della Puglia, è estendibile ad altri documenti analoghi di diverso livello territoriale o ad altri testi in generale: caricando il documento, il software restituirà gli *SDGs* sulla base dell'analisi del testo.

Come nel caso della piattaforma europea <i>KnowSDGs</i>, l'analisi effettuata dal software è basata sulla ricorrenza di parole e loro associazioni e non su una valutazione contenutistica che può, invece, essere oggetto di studi specifici di comparazione tra il testo in esame e l'<i>Agenda 2030</i>.

<p align="center">
  <img src= "https://github.com/claudialorusso/PugliaSostenibileGUI/blob/master/utils/images/collab/trio_collab500x162.png" alt="Trio Collab: UNIBA ISL Apulian Region">
</p>

### Logo

<img align="right" width="30%" src="https://github.com/claudialorusso/PugliaSostenibileGUI/blob/master/utils/images/COLORPugliaSostenibile746x687.png" alt="Logo">

Nel <i>logo</i>, in primo piano si nota la figura di un albero che richiama alla mente l’idea della Natura e della complessità di meccanismi ed interrelazioni che collegano i viventi tra loro e con l'ambiente.

Infatti, la sostenibilità non va intesa solo in riferimento all’agire positivamente solo per il bene dell’ambiente ma anche nelle relazioni, nell'equità, nella cura reciproca.

Dal tronco dell’albero fuoriescono rami le cui estremità si plasmano in frecce; ogni freccia punta verso direzioni differenti che rappresentano varie declinazioni della sostenibilità e che, seppur divergenti, nascono tutte quante da uno stesso principio: il bene comune è raggiungibile solo tramite un’azione comune.

La Terra, alle spalle dell'albero, è la presenza che deve ricordarci sempre la nostra condizione di essere tutti abitanti di uno stesso luogo con risorse limitate che spronano ad un'azione comune per la loro salvaguardia, se vogliamo il suo bene, ed allo stesso tempo stimola per l’ottenimento di quel tanto agognato cambiamento.

Il <i>logo</i> è stato realizzato dall’esperto di grafica <a href="https://www.linkedin.com/in/nicolasurgo/">Nicola Surgo</a>.

### Utilizzo  
**Puglia Sostenibile** è molto semplice da usare!

Per garantire all'utente una migliore esperienza, l'applicazione dispone di una interfaccia grafica piacevole ed intelligibile.

Puoi decidere se effettuare il download del file eseguibile <a href="https://github.com/claudialorusso/PugliaSostenibileGUI/raw/master/PugliaSostenibile.exe">PugliaSostenibile.exe</a> o se avviarlo via linea di comando.

Se scegli di scaricare il file <i>.exe.</i>, il software è direttamente pronto all'uso mentre se scegli l'opzione della linea di comando puoi leggere la sezione successiva che ti guiderà per una corretta esecuzione.

### Command Line Experience

Per prima cosa, poiché il programma è basato su <b>Python 3</b>, è necessario scaricare quest'ultimo sulla tua macchina.

**Attenzione**: le versioni delle attuali librerie **non sono compatibili** con Python 3.10. Sarà, quindi, necessario installare **Python 3.9** o versioni precedenti.

Apri il prompt dei comandi e vai nella cartella in cui hai scaricato **Puglia Sostenibile**.

Supponendo che la cartella si trovi in "C:\\PugliaSostenibileGUI" devi soltanto riportare le seguenti istruzioni nel prompt:

```
cd "C:\\PugliaSostenibileGUI"
py PugliaSostenibile_GUI.py
```

Se è la prima volta che avvii il programma **oppure** è stata rilevata la mancanza di alcune librerie propedeutiche all'avviamento del software, apparirà una finestra in cui ti vengono chieste le autorizzazioni per scaricare ed installare queste ultime.

Per favore, assicurati di essere connesso ad internet.

<p align="center">
  <img width=60% src= "https://user-images.githubusercontent.com/38263840/152874773-366f5dbf-4693-47d2-a25d-cca78c7c4a56.png" alt="Installazione">
</p>

Spunta la relativa casella e clicca sul pulsante "Avanti": al termine del caricamento si aprirà, finalmente, **Puglia Sostenibile**.

![Benvenuto](https://user-images.githubusercontent.com/38263840/152880138-151f384b-6b88-4817-837e-eb1c4b32c540.png)

### Puglia Sostenibile: com'è strutturato

**Puglia Sostenibile** è diviso in sei sezioni principali:

<ul>
<li><b>Home Page:</b> è la pagina principale. Ti basta caricare il documento (formati: '.pdf', '.docx', 'txt') cliccando semplicemente sul pulsante "Seleziona Documento". In seguito, clicca su "Start" ed il software computerà i primi tre <i>SDGs</i> più rilevanti.
<p align="center">
	<img src= "https://user-images.githubusercontent.com/38263840/152885066-fe5e0ae7-6bf3-46f3-8735-c6a0af434d7c.png" alt="Home Page">
</p>
Puoi anche cercare le occorrenze di una parola chiave: devi soltanto digitarla nell'apposita box, cliccare sul pulsante "Cerca" ed il software ti mostrerà quante volte appare nel testo;</li>
<li><b>Informazioni:</b> In questa sezione puoi scoprire informazioni sull'<i>Agenda 2030</i> e su <b>Puglia Sostenibile</b>;</li>
<li><b>Avanzate:</b> In questa pagina puoi cambiare alcune proprietà avanzate:

<p align="center">
	<img src= "https://user-images.githubusercontent.com/38263840/152883238-dfe169a7-ea91-4e78-9186-bf76958657bc.png" alt="Avanzate">
</p>
<ul>
<li><b>Grammatura (utente esperto):</b> Per capire questa proprietà, devi sapere che <b>Puglia Sostenibile</b> calcola gli <i>SDGs</i> più rilevanti facendo uso della Similarità del Coseno. 
Quest'ultima si basa su di una matrice TFIDF tra tutti gli <i>SDGs</i> e la legge stessa. Per eseguire la computazione, ogni contenuto testuale necessita di essere diviso in parole chiave. È data all'utente l'opportunità di scegliere la <i>grammatura</i> di queste ultime ossia il numero massimo di parole da cui è composta ogni parola chiave. Di <i>default</i> la <b>grammatura</b> è impostata su <b>unigram</b> (ogni parola chiave è composta da una singola parola) ma è, comunque, possibile scegliere l'opzione <b>bigram</b>, nel cui caso ogni parola chiave sarà composta da una o, al massimo, due parole.</li>
<li><b>SGDs vs Targets:</b> di <i>default</i> il software rileva i tre <i>SDGs</i> più rilevanti ma, se l'utente vuole scoprire nello specifico i Target più affini alla legge caricata, lo può fare semplicemente cliccando sull'apposito pulsante.
</li>
</ul>
</li>
<li><b>Agenda 2030:</b> in questa pagina è possibile consultare l'<i>Agenda 2030</i>;</li>
<li><b>Contatti:</b> se riscontri difficoltà o errori nell'utilizzo del software o vuoi semplicemente inviare un feedback, in questa sezione trovi tutti i contatti necessari ogni suggerimento per il miglioramento è benvenuto!</li>
<li><b>Sfoglia gli SDGs:</b> in qualsiasi momento, se hai bisogno di consultare gli <i>SDGs</i> puoi farlo semplicemente cliccando sul pulsante "Sfoglia gli SDGs" ed una finestra comparirà all'istante permettendoti di scoprire l'obiettivo ed i vari traguardi ad esso correlati.
  <p align="center">
    <img src= "https://user-images.githubusercontent.com/38263840/152884773-ec6d666c-a3ee-4d8d-86ad-cdd29cb4a507.png" alt="Sfoglia">
  </p>
  </li>
</ul>

### UWP

<b>Puglia Sostenibile</b> è una <b>UWP</b> (<i>Piattaforma Windows Universale</i>) il che significa che è compatibile con diverse versioni di windows, in accordo ai requisiti di <a href="https://developer.microsoft.com/it-it/windows/downloads/windows-sdk/">windows SDK</a>.

### Libraries

Le librerie utilizzate per la creazione di <b>Puglia Sostenibile</b> sono le seguenti:
<ul>
<li>il modulo <a href ="https://github.com/explosion/spacy-models/releases/download/it_core_news_sm-3.2.0/it_core_news_sm-3.2.0-py3-none-any.whl">it-core-news-sm</a></li>
<li><a href ="https://www.nltk.org/">nltk</a> </li>
<li><a href ="https://numpy.org/">numpy</a></li>
<li><a href ="https://pandas.pydata.org/">pandas</a></li>
<li><a href ="https://github.com/pymupdf/PyMuPDF">PyMuPDF</a> (per la GUI)</li>
<li><a href ="https://github.com/mstamy2/PyPDF2">PyPDF2</a> </li>
<li><a href ="https://python-docx.readthedocs.io/en/latest/user/documents.html">python-docx</a> </li>
<li><a href ="https://scikit-learn.org/stable/">scikit-learn</a> </li>
<li><a href ="https://scipy.org/">scipy</a> </li>
<li><a href ="https://spacy.io/">spacy</a> </li>
<li><a href ="https://docs.python.org/3/library/tkinter.html">tkinter</a> (per la GUI) </li>
<li><a href ="https://github.com/Roshanpaswan/tkPDFViewer">tkPDFViewer</a>  (per la GUI)</li>
</ul>

</details>
