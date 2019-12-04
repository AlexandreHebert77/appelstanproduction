<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
	</head>
	<body>
		<h1>Ajouter un interne</h1>
		<form method="post" action="form.php">
			Nom: <label>Nom</label> <input type="text" name="Nom">
			Prenom: <label>Prénom</label> <input type="text" name="Prenom">
            <div class="classe">Classe : 	<input type="radio" name="classe" value="G"/>   2nde  <input type="radio" name="classe" value="F"/>   1ère  <input type="radio" name="classe" value="G"/>   Term  </div>
			Place: <label>Place</label> <input type="email" name="Classe">
            Image: <input name="userfile" type="file" />
			<input type="submit" value="Ajouter">

		<p>
		<?php
		if (isset($_POST['prenom'])) {

            if (isset ($_POST['valider'])){
            $file = $_FILES['image']['tmp_name'];
	        if (!isset($file))
		    echo "S'il vous plait sélectionnez une image";
	        else
	        {
	        $image = addslashes(file_get_contents($_FILES['image']['tmp_name']));
	        $image_name = addslashes($_FILES['image']['tmp_name']);
	        $image_size = getimagesize($_FILES['image']['tmp_name']);

                if ($image_size==FALSE)
		        echo "Format de l'image invalide";
                else
                {

			    $mysqli = new mysqli('localhost', 'root', 'root', 'ETUDE');
			    $mysqli->set_charset('utf8');
			    $requete='INSERT INTO appel VALUES("'.$_POST['Nom'].'","'.$_POST['Prenom'].'","'.$_POST['Classe'].'","'.$_POST['Place'].'",'ABS',"'.$image.'" )';
			    $resultat = $mysqli->query($requete);
			    if ($resultat)
				    echo 'L interne a été ajouté';
			    else
				    echo 'Erreur';
                }
            }
		}
		?>
		</p>
	</body>
</html>
