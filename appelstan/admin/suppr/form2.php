<?php
include("fonctions.php");
?>
<html>
    <head><title>Formulaire de saisie interne </title>
      <link rel="stylesheet" href="../../libs/bootstrap_sans_internet.css">
      <link rel="stylesheet" href="../../style/styleForm.css">
    </head>
    <body>
        <h1>Suppression de la liste (promotion entière)</h1>
        <h2>/!\ Cela est définitif /!\</h2>
        <form name="Etude" method="post" action="form3.php">
            <input type="submit" class="btn btn-lg" name="valider" style="color:black;" value="Suppression de la liste"/>
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
