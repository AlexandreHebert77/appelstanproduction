<?php
$pdo = new PDO('mysql:host=localhost;port=3308; dbname=ETUDE', 'root', '');

      $Nom=$_POST['Nom'];
      $Prenom=$_POST['Prenom'];
      $Classe=$_POST['Classe'];
      $Place=$_POST['Place'];
      $Etat='ABS';
      $stmt = $pdo -> prepare('INSERT INTO appel2(Nom, Prenom, Classe, Place, Etat) VALUES (:Nom, :Prenom, :Classe, :Place, :Etat)');
      $stmt->bindParam(':Nom', $Nom);
      $stmt->bindParam(':Prenom', $Prenom);
      $stmt->bindParam(':Classe', $Classe);
      $stmt->bindParam(':Place', $Place);
      $stmt->bindParam(':Etat', $Etat);
    //  $pdo -> exec('INSERT INTO appel2(Nom, Prenom, Classe, Place, Etat) VALUES (\'pierre\',\'de Gaullier\',\'CM2\',\'321\',\'ABS\')');
      $stmt->execute();
      //$pdo = new PDO('mysql:host=localhost;port=3308; dbname=ETUDE', 'root', '');
      //$pdo -> exec('INSERT INTO appel2(Nom, Prenom, Classe, Place, Etat) VALUES (\'Louis\',\'de Gaullier\',\'CM2\',\'321\',\'ABS\')');
      echo 'L\'interne est pret à souffrir pour les 600 heures d\'étude de l\'année';
?>
