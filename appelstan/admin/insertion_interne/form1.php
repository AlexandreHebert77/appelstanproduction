<?php
//include("NouveauInterne.php");
?>
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
            <div class="classe">Classe : 	<input type="radio" name="classe" value="G"/>   2nde  <input type="radio" name="classe" value="F"/>   1ère  <input type="radio" name="classe" value="G"/>   Term  </div>
            Place : <input type="text" class="form-control" name="place" placeholder="Place"/><br/>
            Image: <input name="userfile" type="file" />
            <input type="submit" class="btn btn-lg" style="margin:10px; color:black;" name="valider" value="OK"/>
        </form>
</div>
        <?php
        if (isset ($_POST['valider'])){
            $file = $_FILES['image']['tmp_name'];
	        if (!isset($file))
		    echo "S'il vous plait sélectionner une image";
	        else
	        {
	        $image = addslashes(file_get_contents($_FILES['image']['tmp_name']));
	        $image_name = addslashes($_FILES['image']['tmp_name']);
	        $image_size = getimagesize($_FILES['image']['tmp_name']);

                if ($image_size==FALSE)
		    echo "Format de l'image invalide";
                else
                {
                    $Nom=$_POST['Nom'];
                    $Prenom=$_POST['Prenom'];
                    $Classe=$_POST['Classe'];
	                $Place=$_POST['Place'];

                    try { $bdd = new PDO('mysql:host=localhost;dbname=ETUDE','root',''); }
                    catch (Exeption $e) { die('Erreur : ' .$e->getMessage())  or die(print_r($bdd->errorInfo())); }
                    $req = $bdd->prepare("INSERT INTO interne VALUES(?,?,?,?,?)");
                    $req->execute(array($Nom,$Prenon,$Classe,$Place,$image));

                    //connectMaBase();
                    //$sql = "INSERT INTO interne VALUES('$Nom','$Prenom','$Classe','$Place','$image')";
                    //conenctMaBase();
                    //mysql_query ($sql) or die ('Erreur SQL !');

            // on ferme la connexion
                    mysql_close();
                }
             }
        }
        ?>
    </body>
</html>
