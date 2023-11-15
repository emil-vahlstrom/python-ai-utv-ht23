# Projekt 1: Image recognition (MUST)

## Uppgift
<p>Klassificera bilder på objekt.</p>
Jag ska välja ut ett antal objekt som jag ska träna en AI-model att känna igen. AI-modellen ska kunna klassifiera bilden beroende på vilket objekt som syns.

Jag har några mål:
* Varje klass ska ha lika många bilder för att undvika bias. Det är svårt att säga hur många bilder jag behöver, men jag kommer satsa på 2000-5000 bilder för inlärning och ytterligare 300-1000 bilder för test/verifiering.
* Jag ska eftersträva samma storlek på bilderna
* Jag vill ha en träffsäkerhet på > 70%
* Jag kommer ha minst 10 klasser för att predictions ska kunna vara statistisk signifikanta. 
* Jag vill kunna utföra AI-träningen på min dator, men överväger att i extremfallet att träna på datorkraft i molnet, t.ex. Google Colab. Det gäller speciellt om bilderna är stora. 

## AI-modellens syfte
AI-modellen kommer utföra object recognition, d.v.s. att hela bilden skickas in i ett neuralt nätverk som spottar ut en tagg som visar hur säker modellen är på vad det är för objekt.
### Avgränsningar
AI-modellen kommer inte:
- Göra object detection (bounding boxes) eller object segmentation (rita konturer runt objektet)

## Dataset
Jag har bestämt mig att gå all-in på OpenImages v7, med en fallback på OpenImages v4 som ingår som ett Tensorflow-dataset. 

### Mer om datasetet
* Datat är av varierad kvalitét och innehåller ibland orelevanta bilder. T.ex. kan kategorin björnar innehålla gummibjörnar. En del bilder saknar segmentation/detection. 
* Datasetet är väldigt stort och det kan saknas värden, t.ex. så kan det saknas labels eller bounding boxes. Man får filtrera på de premisser man har och ladda ner ett subset av datasetet, då det innehåller 9m bilder och jag endast behöver ett fåtal av dessa.
* Förutom bilderna är metadatat CSV-format. Här följer en enklare beskrivning av en delmängd av datat som jag behöver:
  * I datat för boxarna som jag använder för att skära ut objektet ur bilder kommer jag använda:
    - ImageID: Kommer användas för att koppla ihop olika CSV-filer, samt för att ladda ner bilder via ett API.
    - XMin,Xmax,Ymin,Ymax: koordinater för rektangeln
    - IsOccluded: Om 1 kommer jag filtrera bort dessa
  * Det finns även beskrivning av de olika klasserna:
    - LabelName: Ett unikt ID för klassen, t.ex: /m/01dws
    - DisplayName: Klartext för klassen, t.ex. Bear
* Bilderna har varierad storlek och kan dessutom vara uppemot 1024 pixlar i bredd eller höjd. Det kommer krävas en del behandling av bilderna:
  * Jag kommer förminska bilderna till 100x100 pixlar
  * Innan förminskning kommer jag lägga till padding för att behålla aspekt ratio

## Tillvägagångssätt

Ungefär såhär ser min plan ut:
* Jag kommer studera metadatat för bounding boxes och välja ut klasser som förekommer ofta i datasetet. När jag valt ut 10 klasser behöver jag läsa CSV-filerna för att fånga upp id:t för de bilder jag är intresserad av. Dessa ID:n behöver sparas ner i nya filer.
* Jag kommer använda ett hjälpscript från OpenImages för att ladda ner de bilder jag är intresserad av.
* Jag kommer behöva efterbehandla bilderna så de får rätt storlek. Troligtvis behöver jag spara nya bilder då det kommer ta ett tag att behandla uppemot 60000 bilder. Jag behåller originalbilderna om ytterligare efterbehandling behöver göras. 
* Jag behöver skapa datastrukturer som passar med model.fit, ergo: X_train, y_train, X_test, y_test
* Träningen kommer ske med Tensorflow Keras och Conv2D.
* För att det inte ska bli så tråkigt så vill jag kunna visualera progressen. Jag kommer använda matplotlib.pyplot för att :
  * visa ett subset av bilderna
  * vilken prediction som har gjorts och med hur stor sannolikhet i procent.
  * Om prediction var korrekt eller fel
  * Visualisera ett confusion-matrix som visar antalet felgissning och korrekta gissningar per klass.

# Projekt 2: Reinforcement learning (WANT)

## Uppgift
I mån av tid kommer jag att försöka mig på reinforcement learning för ett arkadspel. Det här är någonting som jag vill göra, men sannolikt inte hinner.

## Tillvägagångssätt

Det här är planen:
* Hitta öppen källkod för ett arkadspel skrivet med pygame.
* Modifiera spelet så det går att starta som en AI-spelare
* Hitta de states som hjälper modellen att träna och ta beslut
* Utför träning och förbättra beslutstagandet.

Möjliga spel:
* Pacman
* Space invaders
* Pong