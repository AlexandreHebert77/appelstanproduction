<html>
    <head><title>Formulaire de saisie d'un nouvel interne</title>
<link rel="stylesheet" href="../../libs/bootstrap_sans_internet.css">
<link rel="stylesheet" href="../../style/styleForm.css">

    </head>
    <body>
        <h1>Formulaire de saisie d'un nouvel interne</h1>
        <!-- <div class="imgLogo"><img src="../../img/logoStanTransp.png" alt="logo"></div> -->
        <h2>Entrez les données demandées :</h2>



<div class="formulaire">
        <form name="Etude" method="post" action="form1.php">
            Nom : <input class="form-control" type="text" name="Nom" placeholder="NOM"/> <br/>
	         Prenom : <input class="form-control" type="text" name="Prenom" placeholder="Prénom"/> <br/>
            <div class="classe" style="margin-bottom:12px;">Classe : 	<input type="radio" name="classe" value="G"/>   2nde  <input type="radio" name="classe" value="F"/>   1ère  <input type="radio" name="classe" value="G"/>   Term  </div>
            Place : <input type="text" class="form-control" name="place" placeholder="Place"/><br/>
            <div>
            <input type="submit" value="valider">
            </div>
        </form>
</div>
        <?php

        function connectMaBase(){
            $base = mysql_connect ('localhost', 'root', '');
            mysql_select_db ('ETUDE', $base) ;
        }


        if (isset ($_POST['valider'])){
                $Nom=$_POST['Nom'];
                $Prenom=$_POST['Prenom'];
                $Classe=$_POST['Classe'];
                $Place=$_POST['Place'];
                
                connectMaBase();

                $sql = 'INSERT INTO appel (Nom, Prenom, Classe, Place, Etat) VALUES ("'.$Nom.'","'.$Prenom.'","'.$Classe.'","'.$Place.'","ABS")';

                mysql_query ($sql) or die ('Erreur SQL !');

            // on ferme la connexion
                mysql_close();
                }
             }
        }

        ?>
    </body>
</html>

<!--
(Nom, Prenom, Classe, Place, Etat, Image) -->