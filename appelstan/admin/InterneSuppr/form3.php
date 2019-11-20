<?php
include("fonctions.php");
?>
<html>
    <head><title>Formulaire de saisie interne </title>
      <link rel="stylesheet" href="../../libs/bootstrap_sans_internet.css">
      <link rel="stylesheet" href="../../style/styleForm.css">
    </head>
    <body>
        <h1>Inscription interne</h1>
        <h2>Entrez les données demandées :</h2>

<div class="formulaire">


        <p><form name="Etude" method="post" action="form2.php">
            Nom : <input class="form-control" type="text" name="Nom"/> <br/>
			Prenom : <input class="form-control" type="text" name="Prenom"/> <br/>
            Classe 	<input type="radio" name="classe" value="G"/>2nd<input type="radio" name="classe" value="F"/>1er<input type="radio" name="classe" value="G"/>Term<br/>
            Place : <input class="form-control" type="text" name="place"/><br/>
            <input type="submit" class="btn btn-lg" style="color:black;" name="valider" value="OK"/>
        </form></p>
</div>
        <?php
        if (isset ($_POST['valider'])){
            //On récupère les valeurs entrées par l'utilisateur :
            $Nom=$_POST['Nom'];
            $Prenom=$_POST['Prenom'];
            $Classe=$_POST['Classe'];
			$Place=$_POST['Place'];


            try { $bdd = new PDO('mysql:host=localhost;dbname=ETUDE','root',''); }
            catch (Exeption $e) { die('Erreur : ' .$e->getMessage())  or die(print_r($bdd->errorInfo())); }
            $req = $bdd->prepare('DELETE FROM interne WHERE Nom=? and Prenom=?');
            $req->execute(array($Nom,$Prenon));

            //connectMaBase();
            //$sql = 'DELETE FROM interne WHERE Nom="'.$Nom.'" and Prenom="'.$Prenom.'"';
            //mysql_query ($sql) or die ('Erreur SQL !');

            // on ferme la connexion
            mysql_close();
        }
        ?>
    </body>
</html>
