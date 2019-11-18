<?php
//include("fonctions.php");
?>
<html>
    <head><title>Formulaire de recherche d'interne </title></head>
    <body>
        <h1>Recherche d'un interne</h1>
        <h2>Entrez les données demandées :</h2>
        <form name="Etude" method="post" action="form4.php">
            Nom : <input type="text" name="Nom"/> <br/>
			Prenom : <input type="text" name="Prenom"/> <br/>
            <input type="submit" name="recherche" value="OK"/>
        </form>
        <?php
        if (isset ($_POST['valider'])){
            //On récupère les valeurs entrées par l'utilisateur :
            $Nom=$_POST['Nom'];
            $Prenom=$_POST['Prenom'];            
            
            
            try { $bdd = new PDO('mysql:host=localhost;dbname=ETUDE','root',''); }
            catch (Exeption $e) { die('Erreur : ' .$e->getMessage())  or die(print_r($bdd->errorInfo())); }
            $req = $bdd->prepare('SELECT place WHERE Nom=? and Prenom=?');
            $req->execute(array($Nom,$Prenon,));
        
            //connectMaBase();
            //$sql = ''; 
             //mysql_query ($sql) or die ('Erreur SQL !'); 
 
            // on ferme la connexion
            mysql_close();
			
			//travaille sur la syntaxe
			$page1 = "place"
			$place2 = strval($place)
			$page2 = ".html"
			$page = $page1 + $place2 + $page2
			href = $page
        }
        ?>
        
    </body>
</html>