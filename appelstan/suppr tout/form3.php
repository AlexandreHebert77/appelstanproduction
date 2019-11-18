<?php
include("fonctions.php");
?>
<html>
    <head><title>Formulaire de saisie interne </title></head>
    <body>
        <h1>Suprression de la liste</h1>
        <h2>/!\ Cela est définitif /!\</h2>
        <form name="Etude" method="post" action="form3.php">
            <input type="submit" name="valider" value="supretion de la liste"/>
        </form>
        <?php
        if (isset ($_POST['valider'])){
            connectMaBase();
            $sql = 'DELETE * FROM interne '; 
 
            mysql_query ($sql) or die ('Erreur SQL !'); 
 
            // on ferme la connexion
            mysql_close();
        }
        ?>
    </body>
</html>