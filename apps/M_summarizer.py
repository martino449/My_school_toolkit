from transformers import pipeline

def generate_summary(text):
    # Carica il modello di riassunto
    summarizer = pipeline("summarization", model="t5-small")

    # Genera il riassunto
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    # Inserisci il testo da riassumere
    text = """
Gli Etruschi (in etrusco: 𐌀𐌍𐌍𐌄𐌔𐌀𐌓 ràsenna, 𐌀𐌍𐌔𐌀𐌓 rasna, o 𐌀𐌍𐌑𐌀𐌓 raśna) sono stati un popolo dell'Italia antica vissuto tra il IX secolo a.C. e il I secolo a.C. in un'area denominata Etruria, corrispondente all'incirca alla Toscana, all'Umbria occidentale e al Lazio settentrionale e centrale, con propaggini anche a nord nella zona padana, nelle attuali Emilia-Romagna, Lombardia sud-orientale e Veneto meridionale, all'isola della Corsica, e a sud, in alcune aree della Campania.

La fase più antica della civiltà etrusca è la cultura villanoviana, attestata a partire dal IX secolo a.C.,[1][2][3][4][5] che deriva, a sua volta, dalla cultura protovillanoviana (XII - X secolo a.C.). Sull'origine e la provenienza degli Etruschi è fiorita una notevole letteratura; tuttavia il consenso tra gli studiosi moderni è che gli Etruschi fossero una popolazione autoctona.[6]
La civiltà etrusca ha avuto una profonda influenza sulla civiltà romana, fondendosi successivamente con essa al termine del I secolo a.C. Questo lungo processo di assimilazione culturale ebbe inizio con la data tradizionale della conquista della città etrusca di Veio da parte dei Romani nel 396 a.C.[7] e terminò nel 27 a.C., primo anno del principato di Ottaviano, con il conferimento del titolo di Augusto.
    """

    # Stampa il riassunto
    print("Riassunto:")
    print(generate_summary(text))


#FINE CODICE
# Disclaimer: Questo software è rilasciato sotto la Licenza EUPL (European Union Public License).
# Utilizzare questo software è soggetto ai termini e alle condizioni della Licenza EUPL.
# Per ulteriori dettagli, consultare il testo completo della licenza.
#
# Copyright (C) Mario Pisano, 2024. Tutti i diritti riservati.