INSERT INTO PERSONAGE(name, description, creationuser, modificationuser)
VALUES ("Jaimito", "Una persona pacífica, y con una inteligencia sobrenatural", "Iker", "Iker");
INSERT INTO PERSONAGE(name, description, creationuser, modificationuser)
VALUES ("Amadeus", "Una persona fuerte y con valentia dispuesto a superar cualquier problema", "Iker", "Iker");
INSERT INTO PERSONAGE(name, description, creationuser, modificationuser)
VALUES ("Elmillor", "Una persona que solo sabe jugar al lol y no hace otra cosa", "Iker", "Iker");


INSERT INTO ADVENTURE(name, description, creationuser, modificationuser)
VALUES ("El Bosque Maldito", "Nos encontramos en un bosque mágico que lleva maldito siglos atrás.", "Iker", "Iker");
INSERT INTO ADVENTURE(name, description, creationuser, modificationuser)
VALUES ("El Mar Hondo", "Nos encontramos en un mar lleno de criaturas malignas y poderosas.", "Iker", "Iker");
INSERT INTO ADVENTURE(name, description, creationuser, modificationuser)
VALUES ("La Vida de Lucas", "La dificil y caotica vida de Lucas se hace cada vez más complicada por culpa del gobierno.", "Iker", "Iker");


INSERT INTO STEP(description, final_step, creationuser, modificationuser)
VALUES ("%personatge% está en el inicio del Bosque Maldito, Donde se encuentra 3 caminos ... ¿por donde irá?", "0","Iker", "Iker");
INSERT INTO STEP(description, final_step, creationuser, modificationuser)
VALUES ("Efectivamente, el puente es el cámino mas corto, no contabas con que el puente se descolgaría, Y no sobrevives a la caida. FIN", "1","Iker", "Iker");
INSERT INTO STEP(description, final_step, creationuser, modificationuser)
VALUES ("Sorteando los peligros, llegas de noche al centro del bosque, y ves clavada en un cadaver una espada llameante que te susurra al oido... ¿Que haces?", "0","Iker", "Iker");
INSERT INTO STEP(description, final_step, creationuser, modificationuser)
VALUES ("Matas a toda tu gente, e invadido por la tristeza, decides arrancarte la vida. FIN", "1", "Iker", "Iker");
INSERT INTO STEP(description, final_step, creationuser, modificationuser)
VALUES ("Mas fuerte que nunca, decides que es el momento de erradicar el mal junto A tu nueva aliada, y te embarcas en una nueva aventura. FIN.", "1", "Iker", "Iker");


INSERT INTO ANSWER (description, creationuser, modificationuser)
VALUES ("Decidido, piensas que es el camino más rapido Para atravesar el bosque.", "Iker", "Iker");
INSERT INTO ANSWER (description, creationuser, modificationuser)
VALUES ("Piensas que para ser digno de la espada de las valkirias, Debes de afrontar tus miedos y peligros que acechan", "Iker", "Iker");
INSERT INTO ANSWER (description, creationuser, modificationuser)
VALUES ("¿Que malo puede pasar?, parece salido de Disney. Con lo que no contabas es que en realidad has entrado al laberinto Sombrio, y al rato vuelves a la misma encruzijada", "Iker", "Iker");
INSERT INTO ANSWER (description, creationuser, modificationuser)
VALUES ("¡La espada es tuya, te invade la ira y la locura y vuelves Al poblado...", "Iker", "Iker");
INSERT INTO ANSWER (description, creationuser, modificationuser)
VALUES ("¡La espada, al ver que eres un hombre fuerte y sensato, que eres capaz lo que dice, se entrega a ti como tu fiel Aliada.", "Iker", "Iker");


INSERT INTO CHOICE (description, id_answer, id_actual_step, id_next_step, creationuser, modificationuser)
VALUES ("Escoge el camino de la izquierda, a lo lejos se ve un puente colgante.",  (select id_answer from ANSWER where id_answer=1), (select id_step from STEP where id_step = 1), (select id_step from STEP where id_step=2), "Iker", "Iker");
INSERT INTO CHOICE (description, id_answer, id_actual_step, id_next_step, creationuser, modificationuser)
VALUES ("Escoge el camino del centro, del que parecen provenir. Ruidos de ramas al romperse y astillarse…",  (select id_answer from ANSWER where id_answer=2), (select id_step from STEP where id_step = 1), (select id_step from STEP where id_step=3), "Iker", "Iker");
INSERT INTO CHOICE (description, id_answer, id_actual_step, id_next_step, creationuser, modificationuser)
VALUES ("Escoge el camino de la derecha, lleno de flores, ardillas…",  (select id_answer from ANSWER where id_answer=3), (select id_step from STEP where id_step = 1), (select id_step from STEP where id_step=1), "Iker", "Iker");
INSERT INTO CHOICE (description, id_answer, id_actual_step, id_next_step, id_previous_step, creationuser, modificationuser)
VALUES ("Arrancas la espada de cuajo, ¡ERES %personaje%!',",  (select id_answer from ANSWER where id_answer=4), (select id_step from STEP where id_step = 3), (select id_step from STEP where id_step = 4), (select id_step from STEP where id_step = 1), "Iker", "Iker");
INSERT INTO CHOICE (description, id_answer, id_actual_step, id_next_step, id_previous_step, creationuser, modificationuser)
VALUES ("Atento a lo que dice la espada, escuchas levemente Las palabras ...matalos a todos ... por lo que decides No cogerla.",  (select id_answer from ANSWER where id_answer=5), (select id_step from STEP where id_step = 3), (select id_step from STEP where id_step = 5), (select id_step from STEP where id_step = 1), "Iker", "Iker");
INSERT INTO CHOICE (id_actual_step, id_previous_step, creationuser, modificationuser)
VALUES ((select id_step from STEP where id_step=2), (select id_step from STEP where id_step=1), "Iker", "Iker");
INSERT INTO CHOICE (id_actual_step, id_previous_step, creationuser, modificationuser)
VALUES ((select id_step from STEP where id_step=4), (select id_step from STEP where id_step=3), "Iker", "Iker");
INSERT INTO CHOICE (id_actual_step, id_previous_step, creationuser, modificationuser)
VALUES ((select id_step from STEP where id_step=5), (select id_step from STEP where id_step=4), "Iker", "Iker");


INSERT INTO STARRING (creationuser, modificationuser, id_adventure, id_personage)
VALUES ("Iker", "Iker", (select id_adventure from ADVENTURE where id_adventure=1), (select id_personage from PERSONAGE where id_personage=1));
INSERT INTO STARRING (creationuser, modificationuser, id_adventure, id_personage)
VALUES ("Iker", "Iker", (select id_adventure from ADVENTURE where id_adventure=1), (select id_personage from PERSONAGE where id_personage=2));
INSERT INTO STARRING (creationuser, modificationuser, id_adventure, id_personage)
VALUES ("Iker", "Iker", (select id_adventure from ADVENTURE where id_adventure=1), (select id_personage from PERSONAGE where id_personage=3));



